"""
Font Grabber - Installation Verification Test
Run this to verify everything is working before first use.
"""
import sys
from pathlib import Path


def test_python_version():
    """Check Python version."""
    print("Testing Python version...", end=" ")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} (need 3.8+)")
        return False


def test_imports():
    """Test required imports."""
    print("\nTesting dependencies:")
    
    modules = {
        "customtkinter": "CustomTkinter",
        "requests": "Requests",
        "thefuzz": "TheFuzz",
    }
    
    all_ok = True
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name} - NOT INSTALLED")
            all_ok = False
    
    return all_ok


def test_project_structure():
    """Verify project files exist."""
    print("\nTesting project structure:")
    
    required_files = [
        "main.py",
        "config.py",
        "core/__init__.py",
        "core/manager.py",
        "core/sources/__init__.py",
        "core/sources/base.py",
        "core/sources/google.py",
        "requirements.txt",
    ]
    
    all_ok = True
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - MISSING")
            all_ok = False
    
    return all_ok


def test_google_fonts_api():
    """Test Google Fonts API connectivity."""
    print("\nTesting Google Fonts API...", end=" ")
    
    try:
        import requests
        import os
        api_key = os.getenv("GOOGLE_FONTS_API_KEY")
        
        if not api_key:
            print("✗ GOOGLE_FONTS_API_KEY environment variable not set")
            print("  Set it with: set GOOGLE_FONTS_API_KEY=your_api_key_here")
            return False
            
        response = requests.get(
            f"https://www.googleapis.com/webfonts/v1/webfonts?sort=popularity&key={api_key}",
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            font_count = len(data.get("items", []))
            print(f"✓ Connected ({font_count} fonts available)")
            return True
        else:
            print(f"✗ Status {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ {str(e)}")
        return False


def test_core_functionality():
    """Test core manager and sources."""
    print("\nTesting core functionality:")
    
    try:
        from core import FontManager
        print("  ✓ FontManager import")
        
        manager = FontManager()
        print("  ✓ FontManager initialization")
        
        sources = manager.get_available_sources()
        print(f"  ✓ Font sources loaded: {sources}")
        
        # Test search
        results = manager.search("Roboto")
        if results:
            print(f"  ✓ Search working (found results)")
            return True
        else:
            print("  ✗ Search returned no results")
            return False
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Font Grabber - Installation Verification")
    print("=" * 60)
    
    tests = [
        ("Python Version", test_python_version),
        ("Dependencies", test_imports),
        ("Project Structure", test_project_structure),
        ("API Connectivity", test_google_fonts_api),
        ("Core Functionality", test_core_functionality),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ {name} failed with error: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {name}")
    
    print("\n" + "=" * 60)
    
    if passed == total:
        print("✓ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nYou're ready to go! Run: python main.py")
        return 0
    else:
        print(f"✗ {total - passed} TESTS FAILED")
        print("=" * 60)
        print("\nFix the issues above, then try again.")
        print("Common fixes:")
        print("  - Install dependencies: pip install -r requirements.txt")
        print("  - Check internet connection for API tests")
        return 1


if __name__ == "__main__":
    sys.exit(main())
