"""Render 21 chapter schematics (rbse10_san_01.png .. rbse10_san_21.png) and 4 PYQ visual diagrams
for RBSE Class 10 Sanskrit (Subject Code 71) at 1400x960 resolution using local Pillow with Devanagari font."""

from pathlib import Path
import math
import runpy
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/images"

FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/Nirmala.ttf"),
    Path("C:/Windows/Fonts/mangal.ttf"),
    Path("C:/Windows/Fonts/aparaj.ttf"),
    Path("C:/Windows/Fonts/segoeui.ttf"),
]
BOLD_CANDIDATES = [
    Path("C:/Windows/Fonts/NirmalaB.ttf"),
    Path("C:/Windows/Fonts/mangalb.ttf"),
    Path("C:/Windows/Fonts/aparajb.ttf"),
    Path("C:/Windows/Fonts/segoeuib.ttf"),
]

FONT_PATH = next((p for p in FONT_CANDIDATES if p.exists()), FONT_CANDIDATES[-1])
BOLD_PATH = next((p for p in BOLD_CANDIDATES if p.exists()), BOLD_CANDIDATES[-1])

BG = "#F8FAFC"
INK = "#1E293B"
BLUE = "#1D4ED8"
TEAL = "#0F766E"
AMBER = "#B45309"
PURPLE = "#6D28D9"
BORDER = "#CBD5E1"


def font(size, bold=False):
    return ImageFont.truetype(str(BOLD_PATH if bold else FONT_PATH), size)


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


def draw_header_footer(draw, title_hi, subtitle_en, footer_label):
    draw.rounded_rectangle((40, 24, 1360, 132), radius=18, fill="#EFF6FF", outline="#BFDBFE", width=3)
    text(draw, (700, 62), title_hi, size=31 if len(title_hi) < 48 else 26, fill=BLUE, bold=True)
    text(draw, (700, 104), subtitle_en, size=22, fill=TEAL, bold=False)
    text(draw, (700, 925), footer_label, size=20, fill="#64748B")


def draw_flow(draw, labels, accent=BLUE):
    positions = [(700, 225 + i * 168) for i in range(len(labels))]
    for idx, (p, label) in enumerate(zip(positions, labels), 1):
        x, y = p
        draw.rounded_rectangle((x - 560, y - 54, x + 560, y + 54), radius=20, fill="white", outline=BORDER, width=3)
        draw.ellipse((x - 535, y - 32, x - 471, y + 32), fill=accent)
        text(draw, (x - 503, y), str(idx), size=26, fill="white", bold=True)
        text(draw, (x + 25, y), label, size=27 if len(label) < 52 else 23, fill=INK, bold=True)
    for a, b in zip(positions, positions[1:]):
        arrow(draw, (a[0], a[1] + 56), (b[0], b[1] - 56), fill=TEAL, width=5)


def draw_clock(draw, cx, cy, r, hour, minute, label_top, label_sanskrit, label_sub, color=BLUE):
    draw.rounded_rectangle((cx - 145, cy - 195, cx + 145, cy + 225), radius=22, fill="white", outline=color, width=4)
    text(draw, (cx, cy - 158), label_top, size=25, fill=color, bold=True)
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="#F8FAFC", outline=INK, width=4)
    for m in range(12):
        ang = math.radians(m * 30 - 90)
        x1 = cx + (r - 12) * math.cos(ang)
        y1 = cy + (r - 12) * math.sin(ang)
        x2 = cx + (r - 4) * math.cos(ang)
        y2 = cy + (r - 4) * math.sin(ang)
        draw.line((x1, y1, x2, y2), fill=INK, width=3 if m % 3 == 0 else 1)
    for num, deg in [(12, -90), (3, 0), (6, 90), (9, 180)]:
        rad = math.radians(deg)
        nx = cx + (r - 28) * math.cos(rad)
        ny = cy + (r - 28) * math.sin(rad)
        text(draw, (nx, ny), str(num), size=19, fill=INK, bold=True)
    # Hour hand
    h_angle = math.radians(((hour % 12) + minute / 60.0) * 30 - 90)
    hx = cx + (r * 0.52) * math.cos(h_angle)
    hy = cy + (r * 0.52) * math.sin(h_angle)
    draw.line((cx, cy, hx, hy), fill=INK, width=6)
    # Minute hand
    m_angle = math.radians(minute * 6 - 90)
    mx = cx + (r * 0.76) * math.cos(m_angle)
    my = cy + (r * 0.76) * math.sin(m_angle)
    draw.line((cx, cy, mx, my), fill=color, width=4)
    draw.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=AMBER)
    text(draw, (cx, cy + 142), label_sanskrit, size=25, fill=INK, bold=True)
    text(draw, (cx, cy + 185), label_sub, size=20, fill=TEAL)


def render_ghatika_panel(draw):
    clocks = [
        (210, 465, 10, 0, "१०:०० (पूर्ण समय)", "दशवादने", "संख्या + वादने", BLUE),
        (537, 465, 8, 15, "८:१५ (सवा — १५ मि.)", "सपादाष्टवादने", "सपाद + संख्या + वादने", TEAL),
        (863, 465, 9, 30, "९:३० (साढ़े — ३० मि.)", "सार्धनववादने", "सार्ध + संख्या + वादने", PURPLE),
        (1190, 465, 5, 45, "५:४५ (पौने — ४५ मि.)", "पादोनषड्वादने", "पादोन + अगली संख्या!", AMBER),
    ]
    for cx, cy, h, m, top, san, sub, col in clocks:
        draw_clock(draw, cx, cy, 102, h, m, top, san, sub, col)
    draw.rounded_rectangle((70, 735, 1330, 865), radius=18, fill="#FEF3C7", outline=AMBER, width=3)
    text(draw, (700, 775), "स्वर्णिम नियम (:45 पादोन): ५:४५ को 'पादोनपञ्चवादने' न लिखें — ६ में १५ मिनट कम होने से 'पादोनषड्वादने' लिखें!", size=25, fill=INK, bold=True)
    text(draw, (700, 825), "शताधिक संख्या सूत्र: [इकाई-दहाई] + अधिक + शतम् → १०५ = पञ्चाधिकशतम् • १०८ = अष्टाधिकशतम् • १५० = पञ्चाशदधिकशतम्", size=23, fill=TEAL, bold=True)


def render_vachya_panel(draw):
    cards = [
        (
            265,
            "१. कर्तृवाच्यम् (1 — 2 — 1)",
            BLUE,
            [
                "कर्ता: प्रथमा विभक्ति (१)",
                "कर्म: द्वितीया विभक्ति (२)",
                "क्रिया: कर्ता के अनुसार (१)",
                "उदा.: मोहनः ग्रामं गच्छति।",
                "उदा.: अहं ग्रन्थं पठामि।",
            ],
        ),
        (
            700,
            "२. कर्मवाच्यम् (3 — 1 — 1)",
            TEAL,
            [
                "कर्ता: तृतीया विभक्ति (३)",
                "कर्म: प्रथमा विभक्ति (१)",
                "क्रिया: कर्मानुसार (-यते / -यन्ते)",
                "उदा.: मोहनेन ग्रामः गम्यते।",
                "उदा.: मया ग्रन्थः पठ्यते।",
            ],
        ),
        (
            1135,
            "३. भाववाच्यम् (3 — 0 — 1)",
            PURPLE,
            [
                "कर्ता: तृतीया विभक्ति (३)",
                "कर्म: अकर्मक (० — अभाव)",
                "क्रिया: सदैव एकवचन (-यते)",
                "उदा.: तेन हस्यते / सुप्यते।",
                "उदा.: बालकैः हस्यते।",
            ],
        ),
    ]
    for cx, heading, col, lines in cards:
        draw.rounded_rectangle((cx - 195, 185, cx + 195, 680), radius=22, fill="white", outline=col, width=4)
        draw.rounded_rectangle((cx - 195, 185, cx + 195, 255), radius=22, fill=col)
        text(draw, (cx, 220), heading, size=24, fill="white", bold=True)
        for i, line in enumerate(lines):
            text(draw, (cx, 315 + i * 75), line, size=23, fill=INK, bold=(i >= 3))
    draw.rounded_rectangle((70, 725, 1330, 865), radius=18, fill="white", outline=BORDER, width=3)
    text(draw, (700, 768), "सर्वनाम परिवर्तन: अहम् ↔ मया • त्वम् ↔ त्वया • सः ↔ तेन • सा ↔ तया • वयम् ↔ अस्माभिः • यूयम् ↔ युष्माभिः", size=24, fill=BLUE, bold=True)
    text(draw, (700, 822), "विशेष धातु रूप: पा → पीयते • दा → दीयते • गा → गीयते • कृ → क्रियते • शृ → श्रूयते • स्वप् → सुप्यते", size=23, fill=TEAL, bold=True)


def render_sandhi_panel(draw):
    boxes = [
        (370, 295, "१. जश्त्व संधि (झलां जशोऽन्ते)", "१-४ वर्ण → तृतीय वर्ण (ग, ज, ड, द, ब)", "वाक् + ईशः = वागीशः • जगत् + ईशः = जगदीशः", BLUE),
        (1030, 295, "२. श्चुत्व व ष्टुत्व संधि", "स्/तवर्ग → श्/चवर्ग अथवा ष्/टवर्ग", "सत् + चित् = सच्चित् • तत् + टीका = तट्टीका", TEAL),
        (370, 520, "३. अनुस्वार व परसवर्ण संधि", "पदान्त म् → अनुस्वार • मध्य → पंचम वर्ण", "हरिम् + वन्दे = हरिं वन्दे • सम् + जाता = सञ्जाता", PURPLE),
        (1030, 520, "४. उत्व, रत्व व सत्व विसर्ग संधि", "अः→ओ (मनोहरः) • इ/उः→र् • +खर्→स्/श्/ष्", "मनः+हरः = मनोहरः • पितुर्गृहम् • नमः+ते = नमस्ते", AMBER),
    ]
    for cx, cy, h, sub1, sub2, col in boxes:
        draw.rounded_rectangle((cx - 300, cy - 90, cx + 300, cy + 90), radius=20, fill="white", outline=col, width=4)
        text(draw, (cx, cy - 46), h, size=25, fill=col, bold=True)
        text(draw, (cx, cy + 4), sub1, size=22, fill=INK)
        text(draw, (cx, cy + 48), sub2, size=22, fill=TEAL, bold=True)
    draw.rounded_rectangle((70, 665, 1330, 860), radius=18, fill="#EFF6FF", outline=BLUE, width=3)
    text(draw, (700, 715), "RBSE 2026 मुख्य व पूरक परीक्षा में पूछे गए संधि प्रश्न:", size=25, fill=BLUE, bold=True)
    text(draw, (700, 768), "लोके + अस्मिन् = लोकेऽस्मिन् (पूर्वरूप) • खलु + एतत् = खल्वेतत् (यण्) • इति + उक्त्वा = इत्युक्त्वा (यण्)", size=23, fill=INK, bold=True)
    text(draw, (700, 818), "सम् + जाता = सञ्जाता (परसवर्ण) • सत् + चित् = सच्चित् (श्चुत्व) • वाक् + ईशः = वागीशः (जश्त्व)", size=23, fill=TEAL, bold=True)


def render_samasa_panel(draw):
    items = [
        (265, 295, "१. अव्ययीभावः", "पूर्वपद अव्यय व प्रधान", "उप=समीपम् • निर्=अभावः", "प्रतिगृहम् = गृहं गृहं प्रति", BLUE),
        (700, 295, "२. तत्पुरुषः", "उत्तरपद प्रधान (विभक्ति लोप)", "द्वितीया से सप्तमी कारक", "राजपुरुषः = राज्ञः पुरुषः", TEAL),
        (1135, 295, "३. कर्मधारयः", "विशेषण-विशेष्य / उपमान", "महान् च असौ / इव-एव", "महावृक्षः • नीलकमलम्", PURPLE),
        (265, 560, "४. द्विगुः", "संख्यापूर्वो द्विगुः (समूह)", "षष्ठी बहुवचन + समाहारः", "चतुर्युगम् • पञ्चवटी", AMBER),
        (700, 560, "५. द्वन्द्वः", "उभयपद प्रधान ('च' प्रयोग)", "इतरेतर (-औ) व समाहार (-म्)", "मातापितरौ • पिककाकयोः", BLUE),
        (1135, 560, "६. बहुव्रीहिः", "अन्यपदार्थ प्रधान", "'यस्य सः / यस्याः सा'", "दशाननः • विमूढधीः", TEAL),
    ]
    for cx, cy, h, l1, l2, l3, col in items:
        draw.rounded_rectangle((cx - 195, cy - 105, cx + 195, cy + 105), radius=20, fill="white", outline=col, width=4)
        text(draw, (cx, cy - 62), h, size=25, fill=col, bold=True)
        text(draw, (cx, cy - 15), l1, size=21, fill=INK)
        text(draw, (cx, cy + 25), l2, size=20, fill="#475569")
        text(draw, (cx, cy + 68), l3, size=22, fill=col, bold=True)
    draw.rounded_rectangle((70, 715, 1330, 860), radius=18, fill="white", outline=BORDER, width=3)
    text(draw, (700, 760), "अव्ययीभाव ६ सूत्र: अनु = योग्यम्/पश्चात् • उप = समीपम् • स = सहितम् • निर् = अभावः • प्रति = द्विरुक्ति • यथा = अनतिक्रम्य", size=23, fill=INK, bold=True)
    text(draw, (700, 815), "परीक्षा सावधानी: 'दशाननः' (दश आननानि यस्य सः — रावणः) में बहुव्रीहि समास है, द्विगु नहीं!", size=24, fill=AMBER, bold=True)


def render():
    chapters = runpy.run_path(str(ROOT / "10th rbse/06_sanskrit/source.py"))["CHAPTERS"]
    OUT.mkdir(parents=True, exist_ok=True)
    for c in chapters:
        n = c["number"]
        im = Image.new("RGB", (1400, 960), BG)
        d = ImageDraw.Draw(im)
        draw_header_footer(
            d,
            c["title"],
            c["english"],
            f"SETU LEARNING • RBSE CLASS 10 SANSKRIT (CODE 71) • CHAPTER {n:02} • ORIGINAL SCHEMATIC",
        )
        if n == 11:
            render_sandhi_panel(d)
        elif n == 12:
            render_samasa_panel(d)
        elif n == 15:
            render_ghatika_panel(d)
        elif n == 16:
            render_vachya_panel(d)
        else:
            draw_flow(d, c["diagram"], accent=BLUE if n <= 10 else TEAL)
        im.save(OUT / f"rbse10_san_{n:02}.png", optimize=True)

    # Also render 4 dedicated PYQ figures for Chapter 22
    pyq_specs = [
        (
            "pyq_san_ghatika.png",
            "बोर्ड परीक्षा घटिका समय-लेखनम् (2014–2026)",
            "RBSE Board Clock Time Representation — Purna, Sapada, Sardha & Padona",
            render_ghatika_panel,
        ),
        (
            "pyq_san_sandhi.png",
            "बोर्ड परीक्षा संधि-प्रकरणम् सार-मानचित्र (2014–2026)",
            "RBSE Board Sandhi Summary — Hal, Visarga & Key Vowel Sandhis",
            render_sandhi_panel,
        ),
        (
            "pyq_san_samasa.png",
            "बोर्ड परीक्षा षड्-समास निर्णय-चक्र (2014–2026)",
            "RBSE Board Six Samasa Classification & Vigraha Rules",
            render_samasa_panel,
        ),
        (
            "pyq_san_vachya.png",
            "बोर्ड परीक्षा वाच्य-परिवर्तनम् सूत्र (121 ↔ 311 ↔ 301)",
            "RBSE Board Voice Transformation Matrix (2014–2026)",
            render_vachya_panel,
        ),
    ]
    for fname, title_hi, sub_en, fn in pyq_specs:
        im = Image.new("RGB", (1400, 960), BG)
        d = ImageDraw.Draw(im)
        draw_header_footer(
            d,
            title_hi,
            sub_en,
            "SETU LEARNING • RBSE CLASS 10 SANSKRIT PYQ ARCHIVE (2014–2026) • ORIGINAL SCHEMATIC",
        )
        fn(d)
        im.save(OUT / fname, optimize=True)

    print(f"Rendered {len(chapters)} core chapter schematics + {len(pyq_specs)} PYQ schematics.")


if __name__ == "__main__":
    render()
