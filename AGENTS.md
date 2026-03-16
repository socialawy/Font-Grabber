# Agent Info: Font Grabber

## Project Overview
Font Grabber is a desktop Python application (using CustomTkinter) designed to search and download fonts from Google Fonts. It uses a plugin architecture for font sources.

## Tech Stack
- **Language**: Python 3.8+
- **UI**: CustomTkinter
- **API**: Google Fonts Developer API
- **Dependencies**: `requests`, `thefuzz`, `python-Levenshtein`

## Architecture
- `main.py`: Entry point and GUI.
- `config.py`: Settings management (`config.json`).
- `core/manager.py`: Orchestrates search and download.
- `core/sources/`: contains font source implementations (e.g., `google.py`).

## Guidelines for Jules
1. **Maintainability**: Follow PEP 8 standards.
2. **Plugins**: When adding new font sources, ensure they inherit from `FontSource` in `core/sources/base.py`.
3. **Safety**: Never hardcode API keys. Use environment variables or `config.json`.
4. **UI**: Keep the UI clean and responsive. Use `customtkinter` components.

## Current Goals
- Improve search speed.
- Add more font sources (Font Squirrel, Fontsource).
- Implement font preview in search results.
