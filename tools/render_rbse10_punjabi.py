"""Render 22 chapter schematics (rbse10_pun_01.png .. rbse10_pun_22.png) and 4 PYQ visual diagrams
for RBSE Class 10 Punjabi (Subject Code 75) at 1400x960 resolution using local Pillow with Nirmala UI (Gurmukhi + Devanagari)."""

from pathlib import Path
import math
import runpy
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/images"

NIRMALA_TTC = Path("C:/Windows/Fonts/Nirmala.ttc")

BG = "#F8FAFC"
INK = "#1E293B"
BLUE = "#1D4ED8"
TEAL = "#0F766E"
AMBER = "#B45309"
PURPLE = "#6D28D9"
BORDER = "#CBD5E1"


def font(size, bold=False):
    if NIRMALA_TTC.exists():
        return ImageFont.truetype(str(NIRMALA_TTC), size, index=1 if bold else 0)
    return ImageFont.load_default()


def text(draw, xy, value, size=28, fill=INK, bold=False, anchor="mm"):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def arrow(draw, start, end, fill=BLUE, width=5):
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    points = [
        end,
        (end[0] - 16 * math.cos(angle - 0.5), end[1] - 16 * math.sin(angle - 0.5)),
        (end[0] - 16 * math.cos(angle + 0.5), end[1] - 16 * math.sin(angle + 0.5)),
    ]
    draw.polygon(points, fill=fill)


def draw_header_footer(draw, title_pa, subtitle_en, footer_label):
    draw.rounded_rectangle((40, 24, 1360, 132), radius=18, fill="#EFF6FF", outline="#BFDBFE", width=3)
    text(draw, (700, 62), title_pa, size=28 if len(title_pa) < 55 else 23, fill=BLUE, bold=True)
    text(draw, (700, 104), subtitle_en, size=21, fill=TEAL, bold=False)
    text(draw, (700, 925), footer_label, size=19, fill="#64748B")


def draw_flow(draw, labels, accent=BLUE):
    positions = [(700, 225 + i * 168) for i in range(len(labels))]
    for idx, (p, label) in enumerate(zip(positions, labels), 1):
        x, y = p
        draw.rounded_rectangle((x - 580, y - 54, x + 580, y + 54), radius=20, fill="white", outline=BORDER, width=3)
        draw.ellipse((x - 555, y - 32, x - 491, y + 32), fill=accent)
        text(draw, (x - 523, y), str(idx), size=26, fill="white", bold=True)
        text(draw, (x + 25, y), label, size=24 if len(label) < 62 else 20, fill=INK, bold=True)
    for a, b in zip(positions, positions[1:]):
        arrow(draw, (a[0], a[1] + 56), (b[0], b[1] - 56), fill=TEAL, width=5)


def render_upbhasha_panel(draw):
    cards = [
        (
            265,
            "1. ਮਾਝੀ (ਟਕਸਾਲੀ ਆਧਾਰ)",
            BLUE,
            [
                "ਖੇਤਰ: ਰਾਵੀ ਤੇ ਬਿਆਸ ਵਿਚਕਾਰ",
                "ਜ਼ਿਲ੍ਹੇ: ਅੰਮ੍ਰਿਤਸਰ, ਤਰਨਤਾਰਨ,",
                "ਗੁਰਦਾਸਪੁਰ, ਪਠਾਨਕੋਟ",
                "ਵਿਸ਼ੇਸ਼ਤਾ: ਪੰਜਾਬੀ ਦੀ ਮਿਆਰੀ",
                "(ਟਕਸਾਲੀ) ਸਾਹਿਤਕ ਬੋਲੀ",
            ],
        ),
        (
            700,
            "2. ਮਲਵਈ (ਮਾਲਵਾ ਖੇਤਰ)",
            TEAL,
            [
                "ਖੇਤਰ: ਸਤਲੁਜ ਦੇ ਦੱਖਣ ਵੱਲ",
                "ਜ਼ਿਲ੍ਹੇ: ਬਠਿੰਡਾ, ਲੁਧਿਆਣਾ, ਪਟਿਆਲਾ,",
                "ਫ਼ਿਰੋਜ਼ਪੁਰ, ਸੰਗਰੂਰ, ਮੁਕਤਸਰ,",
                "ਸ੍ਰੀ ਗੰਗਾਨਗਰ ਤੇ ਹਨੂੰਮਾਨਗੜ੍ਹ",
                "ਵਿਸ਼ੇਸ਼ਤਾ: ਸਭ ਤੋਂ ਵੱਡਾ ਖੇਤਰ",
            ],
        ),
        (
            1135,
            "3. ਦੁਆਬੀ ਤੇ ਪੁਆਧੀ",
            PURPLE,
            [
                "ਦੁਆਬੀ: ਬਿਆਸ ਤੇ ਸਤਲੁਜ ਵਿਚਕਾਰ",
                "(ਜਲੰਧਰ, ਹੁਸ਼ਿਆਰਪੁਰ, ਕਪੂਰਥਲਾ)",
                "ਪੁਆਧੀ: ਪੂਰਬੀ ਪੰਜਾਬ (ਰੋਪੜ,",
                "ਮੁਹਾਲੀ, ਰਾਜਪੁਰਾ, ਅੰਬਾਲਾ)",
                "ਪੋਠੋਹਾਰੀ/ਮੁਲਤਾਨੀ: ਲਹਿੰਦਾ ਪੰਜਾਬ",
            ],
        ),
    ]
    for cx, heading, col, lines in cards:
        draw.rounded_rectangle((cx - 195, 185, cx + 195, 680), radius=22, fill="white", outline=col, width=4)
        draw.rounded_rectangle((cx - 195, 185, cx + 195, 255), radius=22, fill=col)
        text(draw, (cx, 220), heading, size=23, fill="white", bold=True)
        for i, line in enumerate(lines):
            text(draw, (cx, 315 + i * 75), line, size=21, fill=INK, bold=(i == 0 or i == 4))
    draw.rounded_rectangle((70, 725, 1330, 865), radius=18, fill="#EFF6FF", outline=BLUE, width=3)
    text(draw, (700, 768), "ਭਾਸ਼ਾ ਦੇ 2 ਰੂਪ: (1) ਮੌਖਿਕ ਭਾਸ਼ਾ (ਬੋਲ-ਚਾਲ ਦੀ ਬੋਲੀ) • (2) ਲਿਖਤੀ ਭਾਸ਼ਾ (ਸਾਹਿਤਕ/ਟਕਸਾਲੀ ਬੋਲੀ)", size=24, fill=BLUE, bold=True)
    text(draw, (700, 822), "RBSE ਬੋਰਡ ਸੂਤਰ: ਰਾਵੀ–ਬਿਆਸ = ਮਾਝੀ • ਬਿਆਸ–ਸਤਲੁਜ = ਦੁਆਬੀ • ਸਤਲੁਜ ਤੋਂ ਦੱਖਣ (ਰਾਜਸਥਾਨ ਸਮੇਤ) = ਮਲਵਈ", size=22, fill=TEAL, bold=True)


def render_lipi_panel(draw):
    boxes = [
        (370, 295, "1. ਗੁਰਮੁਖੀ ਵਰਣਮਾਲਾ (41 ਅੱਖਰ)", "ਪਹਿਲਾਂ 35 ਅੱਖਰ ('ਪੈਂਤੀ') + 6 ਨਵੀਨ ਟੋਲੀ = 41", "8 ਵਰਗ: ਮੁੱਖ ਵਰਗ ਤੋਂ ਨਵੀਨ ਵਰਗ (ਸ਼, ਖ਼, ਗ਼, ਜ਼, ਫ਼, ਲ਼)", BLUE),
        (1030, 295, "2. ਸਵਰ ਅਤੇ ਵਿਅੰਜਨ ਧੁਨੀਆਂ", "ਮੂਲ ਸਵਰ-ਵਾਹਕ 3 (ੳ, ਅ, ੲ) • ਸਵਰ ਧੁਨੀਆਂ 10", "ਅਨੁਨਾਸਕੀ (ਨਾਸਕੀ) ਵਿਅੰਜਨ 5: ਙ, ਞ, ਣ, ਨ, ਮ", TEAL),
        (370, 520, "3. ਲਗਾਂ-ਮਾਤਰਾਵਾਂ (10 ਲਗਾਂ)", "ਨਿਯਮ 3-4-3: ੳ (3), ਅ (4), ੲ (3) ਨਾਲ ਲਗਾਂ", "ਮੁਕਤਾ, ਕੰਨਾ, ਸਿਹਾਰੀ, ਬਿਹਾਰੀ, ਔਂਕੜ, ਦੁਲੈਂਕੜ, ਲਾਂ, ਦੁਲਾਵਾਂ, ਹੋੜਾ, ਕਨੌੜਾ", PURPLE),
        (1030, 520, "4. ਲਗਾਖਰ (3) ਅਤੇ ਦੁੱਤ ਅੱਖਰ (3)", "ਲਗਾਖਰ 3: ਬਿੰਦੀ (ਂ), ਟਿੱਪੀ (ੰ), ਅੱਧਕ (ੱ)", "ਦੁੱਤ (ਪੈਰੀਂ) ਅੱਖਰ 3: ਹ (੍ਹ), ਰ (੍ਰ), ਵ (੍ਵ)", AMBER),
    ]
    for cx, cy, h, sub1, sub2, col in boxes:
        draw.rounded_rectangle((cx - 305, cy - 90, cx + 305, cy + 90), radius=20, fill="white", outline=col, width=4)
        text(draw, (cx, cy - 46), h, size=24, fill=col, bold=True)
        text(draw, (cx, cy + 4), sub1, size=21, fill=INK, bold=True)
        text(draw, (cx, cy + 48), sub2, size=19, fill=TEAL, bold=False)
    draw.rounded_rectangle((70, 665, 1330, 860), radius=18, fill="#FEF3C7", outline=AMBER, width=3)
    text(draw, (700, 715), "ਗੁਰਮੁਖੀ ਲਿਪੀ ਅਤੇ ਅਰਥ-ਬੋਧ ਦੇ ਬੋਰਡ ਪ੍ਰੀਖਿਆ ਸੂਤਰ (15 ਅੰਕ):", size=24, fill=AMBER, bold=True)
    text(draw, (700, 768), "ਬਿੰਦੀ = 6 ਲਗਾਂ ਨਾਲ • ਟਿੱਪੀ = 4 ਲਗਾਂ ਨਾਲ • ਅੱਧਕ = 3 ਲਗਾਂ ਨਾਲ (ਆਵਾਜ਼ ਦੁੱਗਣੀ ਕਰਨ ਲਈ)", size=22, fill=INK, bold=True)
    text(draw, (700, 818), "ਵਿਰੋਧੀ ਸ਼ਬਦ: ਉਸਤਤ × ਨਿੰਦਿਆ • ਆਸਤਕ × ਨਾਸਤਕ • ਸੰਜੋਗ × ਵਿਯੋਗ • ਸੱਖਣਾ × ਭਰਿਆ • ਸੱਜਣ × ਦੁਰਜਨ", size=22, fill=TEAL, bold=True)


def render_kile_panel(draw):
    items = [
        (265, 295, "1. ਚਿਤੌੜਗੜ੍ਹ ਕਿਲ੍ਹਾ", "ਨਿਰਮਾਤਾ: ਚਿਤਰਾਗਦ ਮੌਰਿਆ", "3 ਇਤਿਹਾਸਕ ਸਾਕੇ (1303, 1534, 1567)", "ਵਿਜੇ ਸਤੰਭ ਅਤੇ ਕੀਰਤੀ ਸਤੰਭ", BLUE),
        (700, 295, "2. ਜੈਸਲਮੇਰ (ਸੁਨਾਰ ਕਿਲ੍ਹਾ)", "ਨਿਰਮਾਤਾ: ਰਾਵ ਜੈਸਲ (1155 ਈ.)", "ਭਾਟੀ ਰਾਜਪੂਤ • ਪੀਲੇ ਪੱਥਰ", "ਬਿਨਾਂ ਚੂਨੇ-ਸੀਮਿੰਟ ਤੋਂ ਉਸਾਰੀ", TEAL),
        (1135, 295, "3. ਗਾਗਰੌਣ (ਜਲ-ਦੁਰਗ)", "ਕਾਲੀ ਸਿੰਧ + ਆਹੂ ਨਦੀਆਂ ਸੰਗਮ", "ਡੋਡ ਰਾਜਪੂਤ (ਡੋਡਗੜ੍ਹ)", "ਗਾਗਰੌਣੀ ਤੋਤੇ (ਮਨੁੱਖੀ ਆਵਾਜ਼)", PURPLE),
        (265, 560, "4. ਜੂਨਾਗੜ੍ਹ (ਬੀਕਾਨੇਰ)", "ਨਿਰਮਾਤਾ: ਰਾਜਾ ਰਾਏ ਸਿੰਘ", "33 ਕਰੋੜ ਦੇਵੀ-ਦੇਵਤਿਆਂ ਦਾ ਮੰਦਰ", "ਹਰਮੰਦਰ ਤੇ ਅਨੂਪ ਮਹਿਲ", AMBER),
        (700, 560, "5. ਮਹਿਰਾਨਗੜ੍ਹ (ਜੋਧਪੁਰ)", "ਨਿਰਮਾਤਾ: ਰਾਵ ਜੋਧਾ ਜੀ", "ਚਿੜੀਆ ਟੂੰਕ ਪਹਾੜੀ ਉੱਤੇ ਸਥਿਤ", "ਜੈਪੋਲ, ਲੋਹਾਪੋਲ, ਫ਼ਤਿਹਪੋਲ", BLUE),
        (1135, 560, "6. ਤਾਰਾਗੜ੍ਹ, ਆਮੇਰ, ਰਣਥੰਭੋਰ", "ਤਾਰਾਗੜ੍ਹ ਬੂੰਦੀ: ਰਾਵ ਨਰ ਸਿੰਘ 1354", "ਆਮੇਰ ਜੈਪੁਰ: ਸ਼ਿਲਾ ਦੇਵੀ ਮੰਦਰ", "ਰਣਥੰਭੋਰ: ਰਣ+ਥੰਭ ਪਹਾੜੀਆਂ", TEAL),
    ]
    for cx, cy, h, l1, l2, l3, col in items:
        draw.rounded_rectangle((cx - 195, cy - 105, cx + 195, cy + 105), radius=20, fill="white", outline=col, width=4)
        text(draw, (cx, cy - 62), h, size=23, fill=col, bold=True)
        text(draw, (cx, cy - 15), l1, size=20, fill=INK, bold=True)
        text(draw, (cx, cy + 25), l2, size=19, fill="#475569")
        text(draw, (cx, cy + 68), l3, size=20, fill=col, bold=True)
    draw.rounded_rectangle((70, 715, 1330, 860), radius=18, fill="white", outline=BORDER, width=3)
    text(draw, (700, 760), "ਲੇਖਕ: ਬਲਜਿੰਦਰ ਸਿੰਘ ਭੁੱਲਰ • ਕੁੰਭਲਗੜ੍ਹ (ਮਹਾਰਾਣਾ ਕੁੰਭਾ) • ਨਾਹਰਗੜ੍ਹ ਜੈਪੁਰ (ਸਵਾਈ ਜੈ ਸਿੰਘ)", size=23, fill=INK, bold=True)
    text(draw, (700, 815), "RBSE 2024–2026 ਪ੍ਰਸ਼ਨ: ਸੁਨਾਰ ਕਿਲ੍ਹਾ = ਜੈਸਲਮੇਰ • ਜੂਨਾਗੜ੍ਹ = ਬੀਕਾਨੇਰ • ਮਹਿਰਾਨਗੜ੍ਹ = ਰਾਵ ਜੋਧਾ (ਜੋਧਪੁਰ)", size=22, fill=AMBER, bold=True)


def render_gangnahar_panel(draw):
    boxes = [
        (370, 295, "1. ਮਹਾਰਾਜਾ ਗੰਗਾ ਸਿੰਘ ਜੀ (ਬੀਕਾਨੇਰ)", "ਜਨਮ: 13 ਅਕਤੂਬਰ 1880 ਈ. (ਦੁਸਹਿਰੇ ਵਾਲੇ ਦਿਨ)", "ਪਿਤਾ: ਮਹਾਰਾਜਾ ਲਾਲ ਸਿੰਘ • ਭਰਾ: ਡੂੰਗਰ ਸਿੰਘ", BLUE),
        (1030, 295, "2. ਛੱਪਨੀਆ ਅਕਾਲ (1899 ਈ. / ਸੰਮਤ 1956)", "ਭਿਆਨਕ ਕਾਲ ਨਾਲ ਬੀਕਾਨੇਰ ਵਿੱਚ ਤਬਾਹੀ", "ਸਤਲੁਜ ਦਾ ਪਾਣੀ ਮਾਰੂਥਲ ਵਿੱਚ ਲਿਆਉਣ ਦਾ ਪ੍ਰਣ", AMBER),
        (370, 520, "3. ਨੀਂਹ-ਪੱਥਰ ਅਤੇ ਉਦਘਾਟਨ", "ਨੀਂਹ-ਪੱਥਰ: 5 ਦਸੰਬਰ 1925 (ਹੁਸੈਨੀਵਾਲਾ ਹੈੱਡ)", "ਉਦਘਾਟਨ: 26 ਅਕਤੂਬਰ 1927 (ਲਾਰਡ ਇਰਵਿਨ, ਸ਼ਿਵਪੁਰ ਹੈੱਡ)", TEAL),
        (1030, 520, "4. ਸ੍ਰੀ ਗੰਗਾਨਗਰ ਦੀ ਖੁਸ਼ਹਾਲੀ", "84 ਮੀਲ ਚੂਨੇ-ਕੰਕਰੀਟ ਦੀ ਪੱਕੀ ਨਹਿਰ", "ਰੇਤ ਦੇ ਟਿੱਬਿਆਂ ਵਿੱਚ ਕਣਕ, ਨਰਮਾ, ਕਿੰਨੂ ਤੇ ਸਰ੍ਹੋਂ ਦੇ ਖੇਤ", PURPLE),
    ]
    for cx, cy, h, sub1, sub2, col in boxes:
        draw.rounded_rectangle((cx - 305, cy - 90, cx + 305, cy + 90), radius=20, fill="white", outline=col, width=4)
        text(draw, (cx, cy - 46), h, size=24, fill=col, bold=True)
        text(draw, (cx, cy + 4), sub1, size=21, fill=INK, bold=True)
        text(draw, (cx, cy + 48), sub2, size=20, fill=TEAL, bold=False)
    draw.rounded_rectangle((70, 665, 1330, 860), radius=18, fill="#EFF6FF", outline=BLUE, width=3)
    text(draw, (700, 715), "ਨਿਬੰਧਕਾਰ: ਹਰਪਾਲ ਸਿੰਘ ਲੱਖੀਆਂ ('ਗੰਗ ਨਹਿਰ ਅਤੇ ਮਹਾਰਾਜਾ ਗੰਗਾ ਸਿੰਘ')", size=24, fill=BLUE, bold=True)
    text(draw, (700, 768), "ਉਪਾਧੀ: ਮਾਰੂਥਲ ਵਿੱਚ ਗੰਗਾ ਲਿਆਉਣ ਕਾਰਨ ਮਹਾਰਾਜਾ ਗੰਗਾ ਸਿੰਘ ਨੂੰ 'ਆਧੁਨਿਕ ਭਾਗੀਰਥ' ਕਿਹਾ ਜਾਂਦਾ ਹੈ।", size=22, fill=INK, bold=True)
    text(draw, (700, 818), "ਰਾਮਨਗਰ ਕਸਬੇ ਨੂੰ ਉਹਨਾਂ ਦੇ ਨਾਂ ਉੱਤੇ 'ਸ੍ਰੀ ਗੰਗਾਨਗਰ' ਵਸਾਇਆ ਗਿਆ (ਰਾਜਸਥਾਨ ਦਾ ਅੰਨ-ਭੰਡਾਰ)।", size=22, fill=TEAL, bold=True)


def render():
    chapters = runpy.run_path(str(ROOT / "10th rbse/07_punjabi/source.py"))["CHAPTERS"]
    OUT.mkdir(parents=True, exist_ok=True)
    for c in chapters:
        n = c["number"]
        im = Image.new("RGB", (1400, 960), BG)
        d = ImageDraw.Draw(im)
        draw_header_footer(
            d,
            c["title"],
            c["english"],
            f"SETU LEARNING • RBSE CLASS 10 PUNJABI (CODE 75) • CHAPTER {n:02} • ORIGINAL SCHEMATIC",
        )
        if n == 11:
            render_gangnahar_panel(d)
        elif n == 12:
            render_kile_panel(d)
        elif n == 19:
            render_upbhasha_panel(d)
        elif n == 20:
            render_lipi_panel(d)
        else:
            draw_flow(d, c["diagram"], accent=BLUE if n <= 13 else TEAL)
        im.save(OUT / f"rbse10_pun_{n:02}.png", optimize=True)

    # Also render 4 dedicated PYQ figures for Chapter 23
    pyq_specs = [
        (
            "pyq_pun_upbhasha.png",
            "ਬੋਰਡ ਪ੍ਰੀਖਿਆ: ਪੰਜਾਬੀ ਦੀਆਂ ਉਪ-ਭਾਸ਼ਾਵਾਂ ਅਤੇ ਖੇਤਰ (2014–2026)",
            "RBSE Board Punjabi Dialects Map — Majhi, Malwai, Doabi & Puadhi",
            render_upbhasha_panel,
        ),
        (
            "pyq_pun_lipi.png",
            "ਬੋਰਡ ਪ੍ਰੀਖਿਆ: ਗੁਰਮੁਖੀ ਲਿਪੀ-ਬੋਧ ਅਤੇ ਅਰਥ-ਬੋਧ ਸੂਤਰ (2014–2026)",
            "RBSE Board Gurmukhi Script (41 Letters, 10 Laga, 3 Lagakhar) & Semantics",
            render_lipi_panel,
        ),
        (
            "pyq_pun_kile.png",
            "ਬੋਰਡ ਪ੍ਰੀਖਿਆ: ਰਾਜਸਥਾਨ ਦੇ ਪ੍ਰਸਿੱਧ ਕਿਲ੍ਹੇ — ਤੁਲਨਾਤਮਕ ਚਿੱਤਰ (2014–2026)",
            "RBSE Board Famous Forts of Rajasthan — Builders & Features",
            render_kile_panel,
        ),
        (
            "pyq_pun_gangnahar.png",
            "ਬੋਰਡ ਪ੍ਰੀਖਿਆ: ਗੰਗ ਨਹਿਰ ਅਤੇ ਮਹਾਰਾਜਾ ਗੰਗਾ ਸਿੰਘ (1925–1927)",
            "RBSE Board Gang Canal & Maharaja Ganga Singh Timeline",
            render_gangnahar_panel,
        ),
    ]
    for fname, title_pa, sub_en, fn in pyq_specs:
        im = Image.new("RGB", (1400, 960), BG)
        d = ImageDraw.Draw(im)
        draw_header_footer(
            d,
            title_pa,
            sub_en,
            "SETU LEARNING • RBSE CLASS 10 PUNJABI PYQ ARCHIVE (2014–2026) • ORIGINAL SCHEMATIC",
        )
        fn(d)
        im.save(OUT / fname, optimize=True)

    print(f"Rendered {len(chapters)} core chapter schematics + {len(pyq_specs)} PYQ schematics.")


if __name__ == "__main__":
    render()
