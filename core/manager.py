"""
Font Manager - Orchestrates font searching and downloading.
"""
from typing import List, Dict, Optional
from pathlib import Path
from .sources import FontSource, GoogleFontsSource


class FontManager:
    """Manages font sources and coordinates search/download operations."""
    
    def __init__(self, output_dir: str = "./fonts", config=None):
        """
        Initialize the font manager.
        
        Args:
            output_dir: Default directory for downloaded fonts
            config: Optional Config object for API keys
        """
        self.output_dir = Path(output_dir)
        self.config = config
        self.sources: List[FontSource] = []
        
        # Register default sources
        self._register_default_sources()
    
    def _register_default_sources(self):
        """Register built-in font sources."""
        # Google Fonts with API key from config or environment
        api_key = None
        if self.config:
            api_key = self.config.get("api_keys", {}).get("google_fonts")
        
        self.sources.append(GoogleFontsSource(api_key))
    
    def add_source(self, source: FontSource):
        """
        Add a custom font source.
        
        Args:
            source: FontSource implementation
        """
        self.sources.append(source)
    
    def search(self, query: str) -> Dict[str, List[Dict]]:
        """
        Search all available sources for fonts.
        
        Args:
            query: Font name or search term
            
        Returns:
            Dictionary mapping source names to search results
        """
        results = {}
        
        for source in self.sources:
            if not source.is_available():
                continue
            
            try:
                matches = source.search(query)
                if matches:
                    results[source.name] = matches
            except Exception as e:
                print(f"Error searching {source.name}: {str(e)}")
                continue
        
        return results
    
    def download(self, source_name: str, font_id: str, 
                 output_dir: Optional[str] = None) -> List[str]:
        """
        Download a font from a specific source.
        
        Args:
            source_name: Name of the source to download from
            font_id: Font identifier from search results
            output_dir: Optional custom output directory
            
        Returns:
            List of downloaded file paths
        """
        # Find the source
        source = next((s for s in self.sources if s.name == source_name), None)
        if not source:
            raise ValueError(f"Source '{source_name}' not found")
        
        # Use custom output dir or default
        target_dir = output_dir or str(self.output_dir)
        
        # Download
        return source.download(font_id, target_dir)
    
    def get_available_sources(self) -> List[str]:
        """
        Get list of currently available source names.
        
        Returns:
            List of source names
        """
        return [s.name for s in self.sources if s.is_available()]
