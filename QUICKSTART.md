# Font Grabber - Quick Start Guide ⚡

## 60-Second Setup

### 1. Get Google Fonts API Key (Required)
Visit: https://console.cloud.google.com/apis/credentials
```bash
# Set environment variable
# Windows
set GOOGLE_FONTS_API_KEY=your_api_key_here

# macOS/Linux  
export GOOGLE_FONTS_API_KEY=your_api_key_here
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python main.py
```

### 4. Get Fonts
1. Type font name (e.g., "Roboto")
2. Click "Download"
3. Done! ✅

---

## Your First Font in 3 Steps

**Example: Getting "Montserrat" for your project**

```
Step 1: python main.py
Step 2: Search "Montserrat"
Step 3: Click Download → Check ./fonts/ folder
```

**Time:** ~15 seconds per font

---

## Common Fonts to Try

- **Roboto** - Clean, modern sans-serif
- **Montserrat** - Geometric, versatile
- **Inter** - UI/interface design
- **Lato** - Friendly, professional
- **Poppins** - Rounded, approachable
- **Open Sans** - Highly readable
- **Raleway** - Elegant thin/light weights
- **Playfair Display** - Serif, high-contrast
- **Source Code Pro** - Monospace for code

---

## Troubleshooting (30 seconds)

**App won't start?**
```bash
python --version  # Must be 3.8+
pip install -r requirements.txt --upgrade
```

**No results?**
- Check spelling
- Try simpler name: "Roboto" not "Roboto Light"

**Download failed?**
- Check internet connection
- Check output folder permissions (Settings ⚙)

---

## Building Standalone .exe

**Want to run without Python?**
```bash
python build.py
```

Your .exe appears in `dist/FontGrabber.exe` - fully portable!

---

## Next Steps

- Change output folder: Click ⚙ → Output Directory
- Switch theme: Click ⚙ → Theme
- Read full docs: See README.md

---

**You're ready! Start grabbing fonts. 🎨**
