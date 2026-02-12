# Font Grabber 🔤

A professional, production-ready tool for quickly searching and downloading fonts from Google Fonts. Built for creators who need fonts fast.

## Features

✅ **Search 1000+ Google Fonts** with fuzzy matching (handles typos)  
✅ **One-click downloads** - all font variants automatically  
✅ **Clean, modern GUI** - dark/light themes  
✅ **Configurable output** - save fonts where you need them  
✅ **Plugin architecture** - easily add more font sources later  
✅ **Environment variable support** - secure API key management  

---

## Quick Start

### Option 1: Run from Source (Recommended for First Use)

1. **Install Python 3.8+** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation

2. **Download Font Grabber**
   - Extract this folder to your preferred location

3. **Get Google Fonts API Key** (Required)
   - Visit: https://console.cloud.google.com/apis/credentials
   - Create a new API key
   - Set environment variable:
     ```bash
     # Windows
     set GOOGLE_FONTS_API_KEY=your_api_key_here
     
     # macOS/Linux
     export GOOGLE_FONTS_API_KEY=your_api_key_here
     ```

4. **Install Dependencies**
   ```bash
   # Open terminal/command prompt in the font-grabber folder
   pip install -r requirements.txt
   ```

5. **Run the App**
   ```bash
   python main.py
   ```

### Option 2: Build Standalone Executable

Create a portable .exe (Windows) that runs without Python installed:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name="FontGrabber" --icon=assets/icon.ico main.py

# Your .exe will be in the 'dist' folder
```

**Note:** First launch may be slow (Windows Defender scanning). Subsequent launches are instant.

---

## How to Use

### Basic Workflow

1. **Launch the app**
   - Double-click `main.py` (if Python is associated) or run `python main.py`

2. **Search for a font**
   - Type the font name (e.g., "Roboto", "Inter", "Montserrat")
   - Press Enter or click "Search"
   - Fuzzy matching handles typos: "Roboto" finds "Roboto", "Roboto Mono", etc.

3. **Download**
   - Click "Download" on the font you want
   - All variants (Regular, Bold, Italic, etc.) download automatically
   - Files save to your configured output directory

4. **Find your fonts**
   - Default location: `./fonts` (in the app folder)
   - Change in Settings (⚙ button)

### Settings

Click the ⚙ button to configure:

- **Output Directory**: Where fonts are saved
- **Theme**: Dark, Light, or System default

---

## Usage Examples

### For Your Media Project Workflow

Based on your asset list (`FNT_PRIMARY`):

```
1. Launch Font Grabber
2. Search "Montserrat" (or your desired font)
3. Download → Files appear in ./fonts/
4. Import to your video editor/design tool
5. Mark FNT_PRIMARY ✅ in your tracker
```

**Batch workflow for multiple projects:**
- Keep Font Grabber open
- Search → Download → Next font
- ~15 seconds per font

---

## Technical Details

### Project Structure

```
font-grabber/
├── main.py              # Application entry point
├── config.py            # Configuration management
├── core/
│   ├── manager.py       # Font search/download orchestration
│   └── sources/         # Plugin-style font providers
│       ├── base.py      # Abstract source class
│       ├── google.py    # Google Fonts implementation
├── requirements.txt     # Python dependencies
├── config.json          # Generated on first run (settings)
└── fonts/               # Default download location
```

### Adding New Font Sources

The plugin architecture makes it easy to add new sources:

1. Create a new file in `core/sources/` (e.g., `fontsquirrel.py`)
2. Inherit from `FontSource` base class
3. Implement `search()` and `download()` methods
4. Register in `manager.py`

**Example:**
```python
from .base import FontSource

class FontSquirrelSource(FontSource):
    @property
    def name(self) -> str:
        return "Font Squirrel"
    
    def search(self, query: str) -> List[Dict]:
        # Your search logic
        pass
    
    def download(self, font_id: str, output_dir: str) -> List[str]:
        # Your download logic
        pass
```

---

## Troubleshooting

### "No results found"
- Check spelling (fuzzy matching helps but has limits)
- Try a simpler search: "Roboto" instead of "Roboto Light"
- Google Fonts API might be temporarily down (rare)

### "Failed to download"
- Check internet connection
- Antivirus might be blocking downloads
- Output directory permissions (try changing in Settings)

### Application won't start
- Verify Python 3.8+ is installed: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt --upgrade`
- Check for error messages in terminal

### Downloads are slow
- Normal for fonts with many variants (10+ files)
- Network speed dependent
- First download per session may be slower (cache warming)

### .exe is flagged by antivirus
- False positive (common with PyInstaller)
- Add exception in your antivirus
- Or run from source: `python main.py`

---

## Configuration File

`config.json` is auto-generated on first run:

```json
{
  "output_dir": "./fonts",
  "theme": "dark",
  "window_size": "600x500",
  "api_keys": {
    "google_fonts": ""
  }
}
```

**Notes:**
- `api_keys.google_fonts` is optional (not required for basic usage)
- If you hit API rate limits (unlikely), get a free key from [Google Cloud Console](https://console.cloud.google.com/)

---

## System Requirements

- **OS**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 20.04+)
- **Python**: 3.8 or higher
- **RAM**: 100 MB
- **Disk**: 50 MB + space for downloaded fonts
- **Network**: Internet connection required

---

## Dependencies

- **customtkinter** (5.2.2) - Modern UI framework
- **requests** (2.31.0) - HTTP client for API calls
- **thefuzz** (0.22.1) - Fuzzy string matching
- **python-Levenshtein** (0.25.0) - Fast fuzzy matching backend

---

## Known Limitations

- **Google Fonts only** (for now) - other sources coming in future versions
- **No font preview** in search results (planned feature)
- **No batch download** from list (planned feature)
- **No auto-install** to system fonts (manual installation required)

---

## Roadmap

Future enhancements:

- [ ] Additional sources (Font Squirrel, Fontsource)
- [ ] Font preview in search results
- [ ] Batch download from CSV/text file
- [ ] Auto-install fonts to system
- [ ] Recently downloaded history
- [ ] Favorites/bookmarks
- [ ] LLM-powered font recommendations

---

## License

This software is provided as-is for personal and commercial use.

**Font Licenses:**
- All fonts from Google Fonts are open-source and free for commercial use
- Check individual font licenses in the Google Fonts catalog
- Font Grabber does not modify or redistribute font files

---

## Support

**Issues/Bugs:**
- Check this README first (especially Troubleshooting section)
- Verify you're using the latest version
- Report issues with full error messages

**Feature Requests:**
- Font sources you'd like added
- UI/UX improvements
- Workflow optimizations

---

## Credits

Built with:
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky
- [Google Fonts API](https://developers.google.com/fonts/docs/developer_api)
- [TheFuzz](https://github.com/seatgeek/thefuzz) for fuzzy matching

---

## Version

**v1.0.0** - Initial Release
- Google Fonts integration
- Fuzzy search
- One-click downloads
- Settings management

---

**Happy font hunting! 🎨**
