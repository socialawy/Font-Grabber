# Changelog

All notable changes to Font Grabber will be documented in this file.

## [1.1.0] - 2026-02-12

### Features
- ✅ **API Key Management System**
  - In-app API key dialog for first-time setup
  - Settings menu with API key configuration (⚙)
  - Persistent API key storage in config.json
  - Fallback to environment variable support
  - Welcome message shows API key status
- ✅ **Improved User Experience**
  - Seamless executable usage without manual environment setup
  - Clear API key status indicators
  - User-friendly error messages
- ✅ **Enhanced Security**
  - No hardcoded API keys in source code
  - Secure local storage in config.json
  - Environment variable support for advanced users

#### Technical
- Updated config.py with API key methods
- Modified Google Fonts source for key priority
- Enhanced GUI with API key dialogs
- Updated documentation with setup instructions

#### Documentation
- Added in-app setup instructions to START_HERE.md
- Updated API key workflow documentation

---

## [1.0.0] - 2026-02-12

### Initial Release

#### Features
- ✅ Google Fonts integration (1000+ fonts)
- ✅ Fuzzy search with typo tolerance
- ✅ One-click download (all variants automatically)
- ✅ Modern GUI with CustomTkinter
- ✅ Dark/Light/System theme support
- ✅ Configurable output directory
- ✅ Plugin-based architecture for future sources
- ✅ Settings management
- ✅ Background download threads (non-blocking UI)
- ✅ Match scoring display
- ✅ Comprehensive error handling

#### Technical
- Python 3.8+ support
- Cross-platform (Windows, macOS, Linux)
- PyInstaller support for standalone executables
- Clean MVC-style architecture
- Documented codebase

#### Documentation
- Complete README with troubleshooting
- Quick start guide
- Usage examples with real workflows
- Installation verification test script
- Build script for executables

---

## [Planned] - Future Versions

### v1.1.0 (Q2 2026)
- [ ] Font preview in search results
- [ ] Additional sources (Font Squirrel, Fontsource)
- [ ] Download history
- [ ] Favorites/bookmarks

### v1.2.0 (Q3 2026)
- [ ] Batch download from CSV/text file
- [ ] Font recommendations (LLM-powered)
- [ ] Auto-install to system fonts
- [ ] Font comparison view

### v2.0.0 (Q4 2026)
- [ ] Cloud sync for settings/favorites
- [ ] Font manager (view installed fonts)
- [ ] Project-based font collections
- [ ] Advanced filtering (weight, style, language support)

---

**Note:** Roadmap is subject to change based on user feedback and requests.
