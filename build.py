"""
Build script for creating standalone executable.
Run: python build.py
"""
import subprocess
import sys
from pathlib import Path


def build():
    """Build the executable using PyInstaller."""
    print("=" * 60)
    print("Font Grabber - Build Script")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller found")
    except ImportError:
        print("✗ PyInstaller not found")
        print("\nInstalling PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller installed")
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=FontGrabber",
        "main.py"
    ]
    
    # Add icon if it exists
    icon_path = Path("assets/icon.ico")
    if icon_path.exists():
        cmd.insert(-1, f"--icon={icon_path}")
    
    print("\nBuilding executable...")
    print(f"Command: {' '.join(cmd)}\n")
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 60)
        print("✓ Build successful!")
        print("=" * 60)
        print("\nExecutable location: dist/FontGrabber.exe")
        print("\nYou can now:")
        print("1. Run dist/FontGrabber.exe directly")
        print("2. Move it to any location (it's portable)")
        print("3. Create a desktop shortcut")
    except subprocess.CalledProcessError as e:
        print("\n" + "=" * 60)
        print("✗ Build failed!")
        print("=" * 60)
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build()
