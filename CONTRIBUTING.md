# Contributing to Font Grabber

First off, thank you for considering contributing to Font Grabber! It's people like you who make it a great tool for everyone.

## How to Contribute

### Reporting Bugs
- Use the **Bug Report** template when opening an issue.
- Provide a clear, descriptive title.
- List steps to reproduce the issue.

### Suggesting Enhancements
- Use the **Feature Request** template.
- Explain why this enhancement would be useful.

### Pull Requests
1. **Fork the repository** and create your branch from `main`.
2. **Setup the environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Make your changes**. Ensure your code follows the existing style (type hints, PEP 8).
4. **Test your changes**:
   ```bash
   python test_installation.py
   ```
5. **Submit a Pull Request** with a comprehensive description of your changes.

## Development Setup

- **Language**: Python 3.8+
- **UI Framework**: CustomTkinter
- **Style**: Use type hints for all function signatures.

## Community

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).
