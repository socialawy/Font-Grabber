# 🚀 START HERE - Font Grabber

## Welcome!

Font Grabber is your production-ready tool for grabbing fonts from Google Fonts in seconds. Built for creators who need fonts fast.

---

## ⚡ Get Started in 60 Seconds

### Step 0: Get Google Fonts API Key (Required)
1. Visit: https://console.cloud.google.com/apis/credentials
2. Create a new API key
3. Set environment variable:
   ```bash
   # Windows
   set GOOGLE_FONTS_API_KEY=your_api_key_here
   
   # macOS/Linux
   export GOOGLE_FONTS_API_KEY=your_api_key_here
   ```

**Why required:** Google Fonts API now requires authentication for access.

### Step 1: Verify Installation (Optional but Recommended)
```bash
python test_installation.py
```

This checks:
- ✅ Python version (3.8+)
- ✅ Dependencies installed
- ✅ Google Fonts API accessible
- ✅ Core functionality working

**If tests fail:** Follow the fix suggestions shown

### Step 2: Install Dependencies (if needed)
```bash
pip install -r requirements.txt
```

**First-time users:** This downloads the required libraries (~10 MB)

### Step 3: Launch Font Grabber
```bash
python main.py
```

**First launch:** May take 3-5 seconds to load

### Step 4: Get Your First Font
1. Type: `Roboto` (or any font name)
2. Press: `Enter` or click `Search`
3. Click: `Download` on the best match
4. Done! ✅

**Fonts saved to:** `./fonts/` folder

---

## 📋 Quick Reference

### Your Workflow (Based on Asset List)
```
FNT_PRIMARY needed → Launch Font Grabber
                  → Search font name
                  → Download (15 seconds)
                  → Mark ✅ in tracker
                  → Next asset
```

### Common Searches
- **Sans-serif:** Roboto, Inter, Montserrat, Poppins, Lato
- **Monospace:** Roboto Mono, Source Code Pro
- **Serif:** Playfair Display, Merriweather
- **Display:** Bebas Neue, Raleway

### Settings (Click ⚙ Button)
- Change output folder
- Switch theme (Dark/Light)

---

## 📚 Documentation Files

Depending on what you need:

1. **QUICKSTART.md** ← Fast 3-step guide (60 seconds)
2. **README.md** ← Complete documentation (detailed)
3. **EXAMPLES.md** ← Real-world usage scenarios
4. **CHANGELOG.md** ← Version history & roadmap

**Stuck?** Check README.md → Troubleshooting section

---

## 🎯 Your First Session (Recommended)

Try these to learn the interface:

```
1. Search: "Roboto"
   → See fuzzy matching in action
   → Notice variant count
   → Download it
   
2. Search: "monserrat" (typo)
   → See it still finds "Montserrat"
   → Fuzzy matching handles errors
   
3. Change Settings:
   → Click ⚙
   → Browse to a different folder
   → Save
   → Next download goes to new location
   
4. Try your actual font needs:
   → Search FNT_PRIMARY from your list
   → Download
   → Import to your project
   → Mark ✅ done
```

**Time invested:** 2-3 minutes
**Value:** Confident use for all future projects

---

## 🔨 Building a Standalone .exe (Optional)

Want to run without Python installed?

```bash
python build.py
```

**Result:** `dist/FontGrabber.exe` (fully portable)

**Benefits:**
- No Python needed on target machine
- Single-file distribution
- Desktop shortcut-friendly

**Note:** First .exe launch may be slow (Windows Defender scan)

---

## ✅ Pre-Flight Checklist

Before starting your actual project:

- [ ] Run `python test_installation.py` (all tests pass)
- [ ] Launch `python main.py` (GUI appears)
- [ ] Test search with "Roboto" (results appear)
- [ ] Test download (files appear in `./fonts/`)
- [ ] Check output directory setting (Settings ⚙)

**All checked?** You're production-ready! 🎉

---

## 🎬 Your Project Workflow

Based on your assets list:

```
BEFORE: FNT_PRIMARY - Google Fonts (Free) ❌

1. python main.py
2. Search: [your chosen font name]
3. Download
4. Import to video editor/design tool
5. Mark: FNT_PRIMARY - Google Fonts (Free) ✅

Time: ~20 seconds per font
```

**Multiple projects today?** Keep Font Grabber open, just keep searching and downloading.

---

## 💡 Pro Tips

1. **Speed:** Don't close the app between searches (saves 2-3 sec startup)
2. **Typos:** Don't fix them, fuzzy matching handles it
3. **Variants:** One download = entire font family (bold, italic, etc.)
4. **Organization:** Download all to `./fonts/`, organize into projects later

---

## 🆘 Need Help?

**Quick fixes:**
- App won't start → `pip install -r requirements.txt --upgrade`
- No results → Check spelling (try simpler name)
- Download fails → Check internet, folder permissions

**Detailed help:**
- See README.md → Troubleshooting section
- Check EXAMPLES.md → Real user scenarios

---

## 🚀 You're Ready!

```bash
python main.py
```

Start grabbing fonts. Your FNT_PRIMARY asset is 20 seconds away. 🎨

---

**Questions?** Check the docs. Everything you need is in:
- README.md (comprehensive)
- QUICKSTART.md (condensed)
- EXAMPLES.md (real workflows)

**Happy creating! 🎬**
