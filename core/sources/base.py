"""
Base abstract class for font sources.
All font source plugins must inherit from this class.
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Optional


class FontSource(ABC):
    """Abstract base class for font source providers."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the display name of this source."""
        pass
    
    @abstractmethod
    def search(self, query: str) -> List[Dict]:
        """
        Search for fonts matching the query.
        
        Args:
            query: Font name or search term
            
        Returns:
            List of font dictionaries with keys:
            - name: Font family name
            - variants: List of available variants (e.g., ['regular', 'bold'])
            - source_id: Unique identifier for downloading
            - preview_url: Optional URL for font preview
        """
        pass
    
    @abstractmethod
    def download(self, font_id: str, output_dir: str) -> List[str]:
        """
        Download a font and all its variants.
        
        Args:
            font_id: The source_id from search results
            output_dir: Directory to save font files
            
        Returns:
            List of downloaded file paths
        """
        pass
    
    def is_available(self) -> bool:
        """
        Check if this source is currently available.
        Override if your source requires API keys or network checks.
        
        Returns:
            True if source is available, False otherwise
        """
        return True
