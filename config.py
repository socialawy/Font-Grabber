"""
Configuration management for Font Grabber.
"""
import json
from pathlib import Path
from typing import Dict, Any


class Config:
    """Handles application configuration."""
    
    DEFAULT_CONFIG = {
        "output_dir": "./fonts",
        "theme": "dark",
        "window_size": "600x500",
        "api_keys": {
            "google_fonts": ""
        }
    }
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize configuration.
        
        Args:
            config_path: Path to config file
        """
        self.config_path = Path(config_path)
        self.data = self._load()
    
    def _load(self) -> Dict[str, Any]:
        """Load configuration from file or create default."""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    loaded = json.load(f)
                # Merge with defaults (in case new keys were added)
                config = self.DEFAULT_CONFIG.copy()
                config.update(loaded)
                return config
            except Exception as e:
                print(f"Error loading config: {e}. Using defaults.")
                return self.DEFAULT_CONFIG.copy()
        else:
            return self.DEFAULT_CONFIG.copy()
    
    def save(self):
        """Save current configuration to file."""
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self.data.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a configuration value and save."""
        self.data[key] = value
        self.save()
    
    @property
    def output_dir(self) -> str:
        """Get output directory."""
        return self.data.get("output_dir", "./fonts")
    
    @output_dir.setter
    def output_dir(self, value: str):
        """Set output directory."""
        self.set("output_dir", value)
    
    def get_google_fonts_api_key(self) -> str:
        """Get Google Fonts API key."""
        return self.data.get("api_keys", {}).get("google_fonts", "")
    
    def set_google_fonts_api_key(self, api_key: str):
        """Set Google Fonts API key and save."""
        if "api_keys" not in self.data:
            self.data["api_keys"] = {}
        self.data["api_keys"]["google_fonts"] = api_key
        self.save()
