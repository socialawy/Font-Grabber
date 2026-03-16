"""
Google Fonts source implementation.
Provides access to 1000+ free fonts from Google Fonts.
"""
import os
import requests
from pathlib import Path
from typing import List, Dict, Optional
from thefuzz import fuzz
from .base import FontSource


class GoogleFontsSource(FontSource):
    """Google Fonts API source provider."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Google Fonts source.
        
        Args:
            api_key: Optional API key (can be set via GOOGLE_FONTS_API_KEY env var or config)
        """
        self.api_key = api_key or os.getenv("GOOGLE_FONTS_API_KEY", "")
        self.base_url = "https://www.googleapis.com/webfonts/v1/webfonts"
        self._cache = None
    
    @property
    def name(self) -> str:
        return "Google Fonts"
    
    def _fetch_font_list(self) -> List[Dict]:
        """Fetch and cache the font list from Google Fonts API."""
        if self._cache is not None:
            return self._cache
        
        params = {"sort": "popularity"}
        if self.api_key:
            params["key"] = self.api_key
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            self._cache = response.json().get("items", [])
            return self._cache
        except Exception as e:
            raise Exception(f"Failed to fetch Google Fonts: {str(e)}")
    
    def search(self, query: str) -> List[Dict]:
        """
        Search for fonts using fuzzy matching.
        
        Returns top 5 matches sorted by similarity score.
        """
        fonts = self._fetch_font_list()
        query_lower = query.lower().strip()
        
        # Calculate similarity scores
        matches = []
        for font in fonts:
            family = font["family"]
            score = fuzz.ratio(query_lower, family.lower())
            
            # Also check partial matches
            partial_score = fuzz.partial_ratio(query_lower, family.lower())
            final_score = max(score, partial_score)
            
            if final_score >= 60:  # Minimum threshold
                matches.append({
                    "name": family,
                    "variants": list(font.get("files", {}).keys()),
                    "source_id": family,
                    "preview_url": None,
                    "score": final_score,
                    "_raw": font
                })
        
        # Sort by score (descending) and return top 5
        matches.sort(key=lambda x: x["score"], reverse=True)
        return matches[:5]
    
    def download(self, font_id: str, output_dir: str) -> List[str]:
        """
        Download all variants of a font.
        
        Args:
            font_id: Font family name
            output_dir: Directory to save files
            
        Returns:
            List of downloaded file paths
        """
        # Find the font in cache
        fonts = self._fetch_font_list()
        font = next((f for f in fonts if f["family"] == font_id), None)
        
        if not font:
            raise ValueError(f"Font '{font_id}' not found")
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        downloaded_files = []
        files = font.get("files", {})
        
        for variant, url in files.items():
            try:
                # Download font file
                response = requests.get(url, timeout=30)
                response.raise_for_status()
                
                # Determine file extension from URL
                ext = "ttf"  # Default
                if "woff2" in url:
                    ext = "woff2"
                elif "woff" in url:
                    ext = "woff"
                
                # Save file
                filename = f"{font['family'].replace(' ', '_')}_{variant}.{ext}"
                file_path = output_path / filename
                file_path.write_bytes(response.content)
                downloaded_files.append(str(file_path))
                
            except Exception as e:
                print(f"Warning: Failed to download variant '{variant}': {str(e)}")
                continue
        
        if not downloaded_files:
            raise Exception(f"Failed to download any variants for '{font_id}'")
        
        return downloaded_files
    
    def is_available(self) -> bool:
        """Check if Google Fonts API is accessible."""
        try:
            params = {"sort": "popularity"}
            if self.api_key:
                params["key"] = self.api_key
            response = requests.get(self.base_url, params=params, timeout=5)
            return response.status_code == 200
        except:
            return False
