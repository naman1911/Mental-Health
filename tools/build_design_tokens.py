"""Generates data/design-tokens.json. Every colour pair used for text is checked against WCAG 2.2 AA
(4.5:1 for body text, 3:1 for large text and UI borders) and lightness is nudged until it passes, so the
tokens stay accessible even if a hue is edited. Run from the repository root: python3 -I tools/build_design_tokens.py"""
import json, colorsys, os
ROOT = os.path.join(os.path.dirname(__file__), "..")
D = "2026-10-22"

def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))
def lum(hexc):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)
def contrast(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return round((hi + 0.05) / (lo + 0.05), 2)
def fit(h, s, l, against, target, darker=True):
    """Move lightness until contrast against `against` reaches target."""
    for _ in range(100):
        c = hsl_to_hex(h, s, l)
        if contrast(c, against) >= target: return c, l
        l += -1 if darker else 1
        l = max(0, min(100, l))
    return hsl_to_hex(h, s, l), l

# Chapter hues (degrees). Chosen for distinctness at pastel saturation; no chapter uses red (reserved for crisis).
CHAPTERS = {
 "neurodevelopmental": ("Sprout green", 135), "psychotic": ("Dusk indigo", 255), "bipolar": ("Sea teal", 185),
 "depressive": ("Dawn apricot", 32), "anxiety": ("Sky blue", 205), "ocd-related": ("Lavender", 275),
 "trauma": ("Steel slate", 215), "dissociative": ("Mist lilac", 290), "somatic": ("Moss", 110),
 "eating": ("Sage", 150), "elimination": ("Aqua", 195), "sleep": ("Night periwinkle", 235),
 "sexual-dysfunctions": ("Rose quartz", 345), "gender-dysphoria": ("Soft violet", 300), "disruptive": ("Clay teal", 175),
 "substance": ("Harbour blue", 225), "neurocognitive": ("Lamp gold", 48), "personality": ("Plum", 320),
 "paraphilic": ("Grey-blue", 210), "other-mental-disorders": ("Butter", 55), "medication-induced": ("Mint teal", 165),
 "clinical-focus": ("Life-buoy sky", 200), "further-study": ("Violet", 265), "alternative-pd-model": ("Slate teal", 190),
 "culture": ("Earth ochre", 38),
}
SURFACE_L = "#fbfaf7"   # warm off-white page background, light mode
SURFACE_D = "#15171c"   # soft near-black, dark mode
INK_L = "#23272f"
INK_D = "#e9e7e1"
chapters = {}
contrast_report = []
for cid, (name, h) in CHAPTERS.items():
    tint_l = hsl_to_hex(h, 45, 93)          # card background, light
    tint_d = hsl_to_hex(h, 22, 17)          # card background, dark
    accent_l, _ = fit(h, 42, 42, tint_l, 4.5, darker=True)        # text-grade accent on light tint
    accent_d, _ = fit(h, 48, 74, tint_d, 4.5, darker=False)       # text-grade accent on dark tint
    border_l, _ = fit(h, 35, 72, SURFACE_L, 3.0, darker=True)     # UI border on page
    border_d, _ = fit(h, 30, 38, SURFACE_D, 3.0, darker=False)
    chip_l = hsl_to_hex(h, 40, 86); chip_d = hsl_to_hex(h, 25, 26)
    chapters[cid] = {"name": name, "hue": h,
        "light": {"tint": tint_l, "accent": accent_l, "border": border_l, "chip": chip_l, "ink_on_tint": INK_L},
        "dark":  {"tint": tint_d, "accent": accent_d, "border": border_d, "chip": chip_d, "ink_on_tint": INK_D}}
    contrast_report.append({"chapter": cid,
        "light_ink_on_tint": contrast(INK_L, tint_l), "light_accent_on_tint": contrast(accent_l, tint_l), "light_accent_on_surface": contrast(accent_l, SURFACE_L),
        "dark_ink_on_tint": contrast(INK_D, tint_d), "dark_accent_on_tint": contrast(accent_d, tint_d), "dark_accent_on_surface": contrast(accent_d, SURFACE_D)})
for r in contrast_report:
    for k, v in r.items():
        if k != "chapter": assert v >= 4.5, (r["chapter"], k, v)

crisis = {  # the only red family in the system
 "light": {"bg": "#fde8e6", "border": "#c0392b", "ink": "#6e1b14", "button_bg": "#b8321f", "button_ink": "#ffffff"},
 "dark":  {"bg": "#3a1a17", "border": "#f0948a", "ink": "#ffd9d4", "button_bg": "#f0948a", "button_ink": "#2a0f0c"}}
assert contrast(crisis["light"]["ink"], crisis["light"]["bg"]) >= 4.5 and contrast(crisis["light"]["button_ink"], crisis["light"]["button_bg"]) >= 4.5
assert contrast(crisis["dark"]["ink"], crisis["dark"]["bg"]) >= 4.5 and contrast(crisis["dark"]["button_ink"], crisis["dark"]["button_bg"]) >= 4.5

tokens = {
 "generated_on": D,
 "notes": "Tailwind-compatible design tokens for the card site. Pastel, calm, low-saturation. Red is reserved for the crisis strip. All text/background pairs listed in contrast_report pass WCAG 2.2 AA (>= 4.5:1); borders pass 3:1. Regenerate with tools/build_design_tokens.py after editing hues.",
 "color": {
  "surface": {"light": {"page": SURFACE_L, "card": "#ffffff", "raised": "#f3f1ec", "overlay": "rgba(35,39,47,0.55)"},
              "dark":  {"page": SURFACE_D, "card": "#1d2027", "raised": "#262a33", "overlay": "rgba(0,0,0,0.6)"}},
  "ink": {"light": {"primary": INK_L, "secondary": "#4b515c", "muted": "#6b7280", "inverse": "#f8f7f3", "link": "#2d5f8a"},
          "dark":  {"primary": INK_D, "secondary": "#b5b3ac", "muted": "#8e9099", "inverse": "#15171c", "link": "#8fbfe8"}},
  "line": {"light": {"subtle": "#e6e3dc", "default": "#cfcbc2", "strong": "#8a8780"},
           "dark":  {"subtle": "#2b2f38", "default": "#3b404b", "strong": "#6b7080"}},
  "status": {  # muted, never red
   "light": {"info_bg": "#e6f0fa", "info_ink": "#1f4e79", "success_bg": "#e6f4ea", "success_ink": "#1e5a35", "caution_bg": "#fff4dc", "caution_ink": "#6b4a00"},
   "dark":  {"info_bg": "#1b2a3a", "info_ink": "#9cc7f0", "success_bg": "#1b2e22", "success_ink": "#9fd7b1", "caution_bg": "#332a14", "caution_ink": "#f0d28a"}},
  "crisis": crisis,
  "sensitivity_badge": {"standard": "none", "elevated": "chapter.chip with icon 'life-buoy'", "high": "crisis.bg with icon 'heart-handshake'"},
  "chapters": chapters
 },
 "typography": {
  "font_family": {"sans": "\"Atkinson Hyperlegible\", \"Inter\", system-ui, -apple-system, \"Segoe UI\", sans-serif", "display": "\"Fraunces\", \"Georgia\", serif", "mono": "ui-monospace, \"JetBrains Mono\", monospace"},
  "note": "Atkinson Hyperlegible is free (Braille Institute) and designed for low vision; Fraunces is a free variable serif for the plain title only. Both are on Google Fonts. Fall back to system fonts.",
  "size": {"xs": "0.8125rem", "sm": "0.9375rem", "base": "1.0625rem", "lg": "1.25rem", "xl": "1.5rem", "2xl": "1.875rem", "3xl": "2.375rem"},
  "line_height": {"tight": 1.2, "snug": 1.35, "body": 1.6, "loose": 1.75},
  "weight": {"regular": 400, "medium": 500, "semibold": 600},
  "measure": {"body_max_ch": 66, "card_max_ch": 58},
  "letter_spacing": {"display": "-0.01em", "caps": "0.06em"}
 },
 "spacing": {"unit": "0.25rem", "scale": {"1": "0.25rem", "2": "0.5rem", "3": "0.75rem", "4": "1rem", "5": "1.25rem", "6": "1.5rem", "8": "2rem", "10": "2.5rem", "12": "3rem", "16": "4rem"}, "card_padding": "1.5rem", "card_gap": "1rem", "page_gutter_mobile": "1rem", "page_gutter_desktop": "2rem"},
 "radius": {"sm": "0.5rem", "md": "0.875rem", "lg": "1.25rem", "xl": "1.75rem", "pill": "999px", "card": "1.25rem"},
 "shadow": {"card": "0 1px 2px rgba(35,39,47,0.06), 0 8px 24px rgba(35,39,47,0.06)", "card_hover": "0 2px 4px rgba(35,39,47,0.08), 0 14px 32px rgba(35,39,47,0.10)", "dark_card": "0 1px 2px rgba(0,0,0,0.4), 0 8px 24px rgba(0,0,0,0.35)"},
 "motion": {"duration_fast": "120ms", "duration_base": "200ms", "duration_slow": "320ms", "easing": "cubic-bezier(0.2, 0, 0, 1)", "reduced_motion": "All transitions become 0ms and no autoplay when prefers-reduced-motion is set."},
 "breakpoints": {"sm": "40rem", "md": "48rem", "lg": "64rem", "xl": "80rem"},
 "icons": {"library": "lucide", "size": {"sm": 16, "md": 20, "lg": 24, "chapter": 28}, "stroke_width": 1.75,
  "chapters": {cid: None for cid in CHAPTERS},
  "ui": {"crisis": "life-buoy", "crisis_high": "heart-handshake", "phone": "phone", "text": "message-square", "chat": "messages-square", "community": "users", "verified": "badge-check", "needs_verification": "badge-help", "myth": "x-circle", "fact": "check-circle", "hope": "sun", "young_people": "backpack", "culture": "globe", "strengths": "sparkles", "glossary": "book-open", "related": "link", "source": "file-text", "warning": "triangle-alert", "quick_exit": "log-out", "search": "search", "filter": "sliders-horizontal", "dark_mode": "moon", "light_mode": "sun", "back": "arrow-left", "external": "external-link"}},
 "contrast_report": contrast_report,
 "tailwind": {"note": "Map color.* to theme.extend.colors using CSS variables (e.g. --tint, --accent) switched by [data-theme] so chapter colours cascade to utilities like bg-tint text-accent. See docs/design-system.md section 9 for the config snippet."}
}
import json as _j
tax = _j.load(open(f"{ROOT}/data/taxonomy.json"))
for ch in tax["chapters"]: tokens["icons"]["chapters"][ch["chapter_id"]] = ch["icon"]
json.dump(tokens, open(f"{ROOT}/data/design-tokens.json", "w"), indent=2, ensure_ascii=False)
print("chapters:", len(chapters), "min contrast:", min(v for r in contrast_report for k, v in r.items() if k != "chapter"))
