# Font Grabber - Usage Examples

## Real-World Scenarios

### Scenario 1: Video Production Asset List

**Your asset list:**
```
FNT_PRIMARY - Google Fonts (Free) ❌
```

**Workflow:**
1. Launch Font Grabber: `python main.py`
2. Search: "Montserrat" (or your chosen font)
3. Results show instantly with fuzzy matching
4. Click "Download" on best match
5. All variants (Regular, Bold, Italic, etc.) download to `./fonts/`
6. Import to your video editor
7. Mark in tracker: `FNT_PRIMARY - Google Fonts (Free) ✅`

**Time:** 15-20 seconds total

---

### Scenario 2: Multiple Projects in One Day

**You have 3 demos, each needs 2 fonts:**

```python
# Project 1: Corporate Video
- FNT_PRIMARY: "Inter" 
- FNT_SECONDARY: "Roboto Mono"

# Project 2: Creative Showcase  
- FNT_PRIMARY: "Poppins"
- FNT_SECONDARY: "Playfair Display"

# Project 3: Tutorial Series
- FNT_PRIMARY: "Open Sans"
- FNT_SECONDARY: "Source Code Pro"
```

**Workflow:**
1. Keep Font Grabber open
2. Batch search and download:
   - Search "Inter" → Download
   - Search "Roboto Mono" → Download
   - Search "Poppins" → Download
   - (continue...)
3. All fonts accumulate in `./fonts/`
4. Organize into project folders afterward

**Time:** ~2 minutes for 6 fonts

---

### Scenario 3: Fuzzy Matching Saves Time

**You type:** "robto" (typo)
**Font Grabber finds:**
- Roboto (95% match)
- Roboto Mono (87% match)
- Roboto Slab (85% match)

**You type:** "monserrat" (typo)  
**Font Grabber finds:**
- Montserrat (92% match)

No need to fix typos - just click the best match!

---

### Scenario 4: Exploring Font Variants

**Search:** "Roboto"

**Results show:**
```
Roboto
  12 variants: regular, 100, 100italic, 300, 300italic, 
               italic, 500, 500italic, 700, 700italic, 
               900, 900italic
  [Download] ← Downloads ALL 12 automatically
```

One click = complete font family. No manual variant selection needed.

---

### Scenario 5: Project-Specific Output Directories

**Different projects need different locations:**

1. **Setup:** Click ⚙ Settings
2. **Change:** Output Directory → Browse → `D:/Projects/VideoDemo1/Assets/Fonts`
3. **Download:** Fonts now go directly to project folder
4. **Next project:** Change setting again

**Alternative:** Use default `./fonts/`, then copy/move to projects later.

---

### Scenario 6: Quick Font Comparison

**Finding the right sans-serif:**

```
Search: "inter"     → Preview top result
Search: "roboto"    → Compare
Search: "lato"      → Compare  
Search: "poppins"   → Compare
```

Download top 2-3 candidates, test in your editor, keep the winner.

**Time:** 1 minute to have 3 options ready to test

---

## Command Line Alternative (Future)

While Font Grabber is GUI-focused, you can use the core modules directly:

```python
from core import FontManager

# Quick script
manager = FontManager(output_dir="./my_fonts")
results = manager.search("Roboto")

# Download first match
if results:
    source = list(results.keys())[0]
    font_id = results[source][0]["source_id"]
    files = manager.download(source, font_id)
    print(f"Downloaded {len(files)} files")
```

---

## Tips & Tricks

### Speed Optimization
- **Keep app open:** Restarting takes 2-3 seconds, searching takes 0.5 seconds
- **Fuzzy search:** Don't overthink spelling, type fast and click the match
- **Batch mode:** Queue your searches mentally, download in sequence

### Organization
- **Default approach:** Download all fonts to `./fonts/`, sort later
- **Per-project:** Change output directory in Settings for each project
- **Naming:** Fonts download as `FontName_variant.ttf` - easy to identify

### Font Selection
- **Popular choices:** Roboto, Inter, Montserrat, Open Sans, Poppins
- **Code/mono:** Roboto Mono, Source Code Pro, Fira Code
- **Serif:** Playfair Display, Merriweather, Lora
- **Display/Creative:** Bebas Neue, Raleway, Josefin Sans

### Troubleshooting Common Searches
- ❌ "Helvetica" → Not in Google Fonts (commercial)
  - ✅ Try: "Inter", "Roboto", "Public Sans"
- ❌ "Arial" → Not in Google Fonts (commercial)
  - ✅ Try: "Open Sans", "Lato"
- ❌ "Times New Roman" → Not in Google Fonts  
  - ✅ Try: "Merriweather", "Lora", "Crimson Text"

---

## Real User Flow (Timed)

**Task:** Get 5 fonts for a new project

```
00:00 - Launch Font Grabber (python main.py)
00:03 - App ready, type "Inter"
00:04 - Press Enter, results appear
00:05 - Click Download
00:08 - Download complete (5 variants)
00:09 - Type "Poppins"
00:10 - Press Enter  
00:11 - Click Download
00:15 - Download complete (9 variants)
00:16 - Type "Roboto Mono"
00:17 - Press Enter
00:18 - Click Download
00:22 - Download complete (7 variants)
00:23 - Type "Playfair"
00:24 - Results show "Playfair Display"
00:25 - Click Download
00:30 - Download complete (6 variants)
00:31 - Type "Source Code Pro"
00:32 - Press Enter
00:33 - Click Download
00:40 - Download complete (8 variants)
```

**Total:** 40 seconds for 5 complete font families (35 individual font files)

**Average:** 8 seconds per font family

---

## Advanced: Building a Font Library

**Goal:** Create a curated library of go-to fonts

**Approach:**
1. One-time setup: Download 15-20 frequently-used fonts
2. Store in `D:/FontLibrary/` or similar
3. Change Font Grabber output to this directory (Settings)
4. Build your collection over time
5. Import entire library into each new project

**Recommended starter library:**
```
Sans-Serif:
- Roboto, Inter, Open Sans, Lato, Poppins, Montserrat

Monospace:
- Roboto Mono, Source Code Pro, Fira Code

Serif:  
- Merriweather, Playfair Display, Lora

Display:
- Bebas Neue, Raleway, Oswald
```

**Time to build:** ~5 minutes
**Value:** Never search for basic fonts again

---

**Happy font hunting! 🎨**
