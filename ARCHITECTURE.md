# Font Grabber - Technical Architecture

## Overview

Font Grabber uses a plugin-based architecture to support multiple font sources with a unified interface.

---

## Architecture Diagram

```
┌─────────────────────────────────────────┐
│          main.py (GUI Layer)            │
│  - CustomTkinter Interface              │
│  - User Input Handling                  │
│  - Threading for Downloads              │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│      config.py (Configuration)          │
│  - JSON config management               │
│  - Settings persistence                 │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│   core/manager.py (Orchestration)       │
│  - Coordinates all sources              │
│  - Aggregates search results            │
│  - Routes download requests             │
└───────────────┬─────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
┌──────────────┐  ┌──────────────┐
│ Source: Base │  │ Source: Base │
│  (Abstract)  │  │  (Abstract)  │
└──────┬───────┘  └──────┬───────┘
       │                 │
       ▼                 ▼
┌──────────────┐  ┌──────────────┐
│    Google    │  │  (Future)    │
│    Fonts     │  │   Sources    │
└──────────────┘  └──────────────┘
```

---

## Core Components

### 1. GUI Layer (main.py)

**Purpose:** User interface and interaction handling

**Key Classes:**
- `FontGrabber(ctk.CTk)` - Main application window
- `SettingsDialog(ctk.CTkToplevel)` - Settings modal

**Responsibilities:**
- Render UI components
- Handle user input (search, download, settings)
- Manage threading for non-blocking operations
- Display search results and status updates

**Threading Strategy:**
```python
def _search(self):
    def search_thread():
        results = self.manager.search(query)
        self.after(0, lambda: self._display_results(results))
    
    threading.Thread(target=search_thread, daemon=True).start()
```

**Why:** Prevents UI freezing during network operations

---

### 2. Configuration Layer (config.py)

**Purpose:** Settings persistence and management

**Key Class:**
- `Config` - Configuration manager

**Storage Format:** JSON (`config.json`)

**Schema:**
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

**Features:**
- Auto-creates default config on first run
- Merges user config with defaults (forward compatibility)
- Property accessors for common settings

---

### 3. Orchestration Layer (core/manager.py)

**Purpose:** Coordinate multiple font sources

**Key Class:**
- `FontManager` - Central orchestrator

**Methods:**
```python
search(query: str) -> Dict[str, List[Dict]]
  # Returns: {source_name: [font_results]}

download(source_name: str, font_id: str, output_dir: str) -> List[str]
  # Returns: [file_paths]

get_available_sources() -> List[str]
  # Returns: [source_names]
```

**Source Registration:**
```python
def _register_default_sources(self):
    self.sources.append(GoogleFontsSource())
    # Future: self.sources.append(FontSquirrelSource())
```

**Design Pattern:** Strategy Pattern (interchangeable sources)

---

### 4. Source Plugin Layer (core/sources/)

**Purpose:** Abstract font source implementations

**Base Class:** `FontSource` (ABC)

**Required Methods:**
```python
@property
def name(self) -> str:
    """Display name of source"""

def search(self, query: str) -> List[Dict]:
    """Search for fonts, return standardized results"""

def download(self, font_id: str, output_dir: str) -> List[str]:
    """Download font, return file paths"""

def is_available(self) -> bool:
    """Check if source is accessible"""
```

**Standardized Result Schema:**
```python
{
    "name": "Font Family Name",
    "variants": ["regular", "bold", "italic"],
    "source_id": "unique_identifier",
    "preview_url": "optional_url",
    # Plugin-specific fields (prefixed with _)
    "_raw": {...}  # Original API response
}
```

---

## Plugin Development Guide

### Creating a New Font Source

**Example: Font Squirrel**

```python
# core/sources/fontsquirrel.py

from .base import FontSource
import requests
from pathlib import Path

class FontSquirrelSource(FontSource):
    
    @property
    def name(self) -> str:
        return "Font Squirrel"
    
    def search(self, query: str) -> List[Dict]:
        # 1. Query Font Squirrel API/scrape
        # 2. Parse results
        # 3. Return standardized format
        
        results = []
        # ... your search logic ...
        
        for font in raw_results:
            results.append({
                "name": font["family"],
                "variants": font["styles"],
                "source_id": font["id"],
                "preview_url": font.get("preview"),
                "_raw": font  # Keep original for download
            })
        
        return results
    
    def download(self, font_id: str, output_dir: str) -> List[str]:
        # 1. Find font by ID (from _raw or re-query)
        # 2. Download files
        # 3. Save to output_dir
        # 4. Return list of paths
        
        downloaded_files = []
        # ... your download logic ...
        
        return downloaded_files
    
    def is_available(self) -> bool:
        try:
            response = requests.get("https://fontsquirrel.com", timeout=5)
            return response.status_code == 200
        except:
            return False
```

**Registration:**
```python
# core/manager.py

def _register_default_sources(self):
    self.sources.append(GoogleFontsSource())
    self.sources.append(FontSquirrelSource())  # Add here
```

**That's it!** The GUI automatically:
- Shows results from both sources
- Handles downloads from either
- Manages availability checking

---

## Data Flow

### Search Flow

```
User Input: "Roboto"
    ↓
GUI: _search()
    ↓
Manager: search("Roboto")
    ↓
Source 1: GoogleFonts.search("Roboto")
    → Returns: [{name: "Roboto", variants: [...]}]
Source 2: FontSquirrel.search("Roboto")
    → Returns: [{name: "Roboto", variants: [...]}]
    ↓
Manager: Aggregate results
    → Returns: {
        "Google Fonts": [...],
        "Font Squirrel": [...]
      }
    ↓
GUI: _display_results()
    → Render result cards
```

### Download Flow

```
User Click: Download "Roboto" from "Google Fonts"
    ↓
GUI: _download_font(source_name="Google Fonts", font={...})
    ↓
Manager: download("Google Fonts", "Roboto", "./fonts")
    ↓
GoogleFontsSource: download("Roboto", "./fonts")
    → Network requests for font files
    → Save to disk
    → Returns: ["/fonts/Roboto_regular.ttf", ...]
    ↓
Manager: Return file paths
    ↓
GUI: _download_success(files=[...])
    → Show success message
```

---

## Error Handling Strategy

### Levels of Error Handling

**1. Source Level**
```python
def search(self, query: str) -> List[Dict]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return self._parse_results(response.json())
    except Exception as e:
        # Log error, return empty list
        print(f"Search error: {e}")
        return []
```

**2. Manager Level**
```python
def search(self, query: str) -> Dict[str, List[Dict]]:
    results = {}
    for source in self.sources:
        try:
            matches = source.search(query)
            if matches:
                results[source.name] = matches
        except Exception as e:
            # Continue to next source
            print(f"Error in {source.name}: {e}")
    return results
```

**3. GUI Level**
```python
def _search(self):
    def search_thread():
        try:
            results = self.manager.search(query)
            self.after(0, lambda: self._display_results(results))
        except Exception as e:
            self.after(0, lambda: self._search_error(str(e)))
    threading.Thread(target=search_thread, daemon=True).start()
```

**Philosophy:** Graceful degradation - if one source fails, others continue

---

## Testing Strategy

### Unit Tests (Future)

```python
# tests/test_sources.py
def test_google_fonts_search():
    source = GoogleFontsSource()
    results = source.search("Roboto")
    assert len(results) > 0
    assert results[0]["name"] == "Roboto"

# tests/test_manager.py
def test_manager_multi_source():
    manager = FontManager()
    results = manager.search("Roboto")
    assert "Google Fonts" in results
```

### Integration Tests

Current approach: `test_installation.py` verifies:
- Dependencies installed
- API connectivity
- Core functionality

---

## Performance Considerations

### Caching Strategy

**Google Fonts list cached in memory:**
```python
class GoogleFontsSource(FontSource):
    def __init__(self):
        self._cache = None  # Cache full font list
    
    def _fetch_font_list(self):
        if self._cache is not None:
            return self._cache
        # Fetch and cache
```

**Why:** Font list changes infrequently, reduces API calls

### Threading

**All network operations run in background threads:**
- Search operations
- Download operations

**Why:** Keeps GUI responsive

### Fuzzy Matching Optimization

**Uses two algorithms:**
```python
score = fuzz.ratio(query, font_name)           # Full match
partial = fuzz.partial_ratio(query, font_name) # Substring match
final = max(score, partial)
```

**Threshold:** 60% minimum (configurable in code)

---

## Security Considerations

### API Keys
- Stored in `config.json` (local file)
- Optional for Google Fonts
- **TODO:** Encrypt sensitive keys in future versions

### Downloads
- Files saved to user-specified directory
- No executable files downloaded (only fonts)
- File extensions validated

### Network Requests
- HTTPS only
- Timeout limits (5-30 seconds)
- Exception handling for all network ops

---

## Extensibility Points

### Easy to Add:

1. **New font sources** → Create plugin in `core/sources/`
2. **New themes** → Add to `config.py` defaults
3. **New export formats** → Extend source download methods
4. **Font preview** → Add preview method to `FontSource` base class

### Medium Difficulty:

1. **LLM recommendations** → New service layer
2. **Batch operations** → Extend manager with queue system
3. **Font comparison** → New UI component

### Complex:

1. **Cloud sync** → Backend service + auth layer
2. **Font rendering** → PIL/Pillow integration + canvas component
3. **Auto-install to system** → OS-specific implementations

---

## Build & Distribution

### PyInstaller Configuration

**Command:**
```bash
pyinstaller --onefile --windowed --name="FontGrabber" main.py
```

**Options:**
- `--onefile`: Single executable
- `--windowed`: No console window
- `--name`: Custom exe name
- `--icon`: Application icon (if provided)

**Output:** `dist/FontGrabber.exe`

### Dependencies Bundled:
- Python runtime
- customtkinter
- requests
- thefuzz
- All standard library modules

**Size:** ~15-25 MB (compressed)

---

## Code Style Guide

### Conventions Used

**Type Hints:**
```python
def search(self, query: str) -> List[Dict]:
```

**Docstrings:** Google style
```python
def method(param: str) -> bool:
    """
    Brief description.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
    """
```

**Naming:**
- Classes: `PascalCase`
- Functions/Methods: `snake_case`
- Constants: `UPPER_CASE`
- Private: `_leading_underscore`

**Imports:**
```python
# Standard library
import sys
from pathlib import Path

# Third-party
import requests
import customtkinter as ctk

# Local
from .base import FontSource
```

---

## Future Architecture Improvements

### v2.0 Vision

**Service Layer:**
```
GUI ↔ Manager ↔ Services ↔ Sources
                    ↓
                [Cache]
                [Analytics]
                [Recommendations]
```

**Database Layer:**
```
SQLite:
  - Download history
  - Favorites
  - Font metadata cache
  - User preferences
```

**API Layer:**
```
REST API for:
  - Remote control
  - Automation scripts
  - CI/CD integration
```

---

## Development Workflow

### Local Development

```bash
# Setup
git clone <repo>
cd font-grabber
pip install -r requirements.txt

# Test
python test_installation.py

# Run
python main.py

# Build
python build.py
```

### Adding Features

1. Update relevant layer (Source/Manager/GUI)
2. Update tests
3. Update documentation
4. Test manually
5. Build and test exe

---

## Dependencies Deep Dive

### CustomTkinter (GUI Framework)

**Why chosen:**
- Modern appearance (vs tkinter)
- Cross-platform consistency
- Active development
- MIT license

**Alternatives considered:**
- PyQt5: Too heavy, GPL license
- Kivy: Mobile-focused
- tkinter: Outdated appearance

### Requests (HTTP Client)

**Why chosen:**
- Industry standard
- Simple API
- Reliable

**No alternatives needed**

### TheFuzz (Fuzzy Matching)

**Why chosen:**
- Best-in-class fuzzy matching
- Handles typos well
- Fast with C extension (python-Levenshtein)

**Trade-off:**
- GPL license (acceptable for end-user app)

---

## Troubleshooting Common Dev Issues

### Import Errors
- Check `__init__.py` files exist in all packages
- Verify `requirements.txt` dependencies installed

### GUI Not Updating
- Ensure using `self.after()` for thread → GUI communication
- Never update GUI directly from background thread

### Download Failures
- Verify URL format (https://)
- Check timeout values
- Validate file paths (Path object recommended)

---

**For Contributors:**

See this document before making changes. Understanding the architecture prevents breaking changes and maintains code quality.

**Questions?** Check inline comments in source code - extensively documented.
