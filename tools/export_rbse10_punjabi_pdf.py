"""Export the complete RBSE Class 10 Punjabi Guide (Book 7, 23 Chapters + 26 Diagrams)
to a print-ready, teacher-review PDF with full HarfBuzz Gurmukhi & Devanagari shaping."""

from pathlib import Path
import html
import json
import re
import subprocess
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
BOOK_JSON = ROOT / "assets/content/rbse10_punjabi/punjabi_book1.json"
IMAGES_DIR = ROOT / "assets/images"
OUT_DIR = ROOT / "10th rbse/07_punjabi"
HTML_PATH = ROOT / "artifacts/rbse10_punjabi/RBSE_Class10_Punjabi_Complete_Guide.html"
PDF_PATH = OUT_DIR / "RBSE_Class10_Punjabi_Complete_Guide.pdf"
ARTIFACT_PDF_PATH = ROOT / "artifacts/rbse10_punjabi/RBSE_Class10_Punjabi_Complete_Guide.pdf"


def inline_md(text: str) -> str:
    """Convert inline markdown (**bold**, [link](url)) to safe HTML."""
    escaped = html.escape(text)
    # Links: [label](url)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{m.group(2)}" class="ext-link">{m.group(1)}</a>',
        escaped,
    )
    # Bold: **text**
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def render_text_block(value: str) -> str:
    """Render a text block (which may contain markdown tables or paragraphs) to HTML."""
    lines = value.strip().splitlines()
    # Check if this block is a markdown table
    if len(lines) >= 2 and lines[0].strip().startswith("|") and "---" in lines[1]:
        headers = [c.strip() for c in lines[0].strip().strip("|").split("|")]
        rows_html = []
        for row_line in lines[2:]:
            if not row_line.strip().startswith("|"):
                continue
            cells = [c.strip() for c in row_line.strip().strip("|").split("|")]
            tds = "".join(f"<td>{inline_md(c)}</td>" for c in cells)
            rows_html.append(f"<tr>{tds}</tr>")
        ths = "".join(f"<th>{inline_md(h)}</th>" for h in headers)
        return (
            f'<table class="guide-table"><thead><tr>{ths}</tr></thead>'
            f"<tbody>{''.join(rows_html)}</tbody></table>"
        )

    paragraphs = value.strip().split("\n\n")
    out = []
    for p in paragraphs:
        p_lines = [inline_md(line.strip()) for line in p.splitlines() if line.strip()]
        out.append(f"<p>{'<br>'.join(p_lines)}</p>")
    return "\n".join(out)


def section_badge(ch_id: str) -> tuple[str, str]:
    if ch_id.startswith("pun_kav_"):
        return ("ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਕਾਵਿ ਭਾਗ (काव्य खंड · 15 अंक)", "#7C2D12")
    if ch_id.startswith("pun_nib_"):
        return ("ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਨਿਬੰਧ ਭਾਗ (निबंध खंड · 15 अंक)", "#0369A1")
    if ch_id.startswith("pun_kah_"):
        return ("ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਕਹਾਣੀ ਭਾਗ (कहानी खंड · 15 अंक)", "#047857")
    if ch_id.startswith("pun_vya_"):
        return ("ਪੰਜਾਬੀ ਵਿਆਕਰਣ ਭਾਗ (व्यावहारिक व्याकरण · 12 अंक)", "#6D28D9")
    if ch_id == "pun_rac_ch21":
        return ("ਅਣਡਿੱਠਾ ਪੈਰ੍ਹਾ (अपठित अवबोधन · 10 अंक)", "#B45309")
    if ch_id == "pun_rac_ch22":
        return ("ਰਚਨਾਤਮਕ ਕਾਰਜ — ਨਿਬੰਧ ਅਤੇ ਪੱਤਰ (रचनात्मक लेखन · 13 अंक)", "#BE123C")
    return ("ਹੱਲ ਕੀਤੇ ਬੋਰਡ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ (2014–2026 PYQ Bank)", "#1E3A8A")


def build_html() -> Path:
    data = json.loads(BOOK_JSON.read_text(encoding="utf-8"))
    chapters = data["chapters"]

    toc_rows = []
    chapter_sections = []

    for idx, ch in enumerate(chapters, 1):
        ch_id = ch["id"]
        badge_text, badge_color = section_badge(ch_id)
        toc_rows.append(
            f'<tr>'
            f'<td style="text-align:center;font-weight:700;">{idx}</td>'
            f'<td><span class="toc-pill" style="background:{badge_color}18;color:{badge_color};border:1px solid {badge_color}55;">{html.escape(badge_text.split("(")[0].strip())}</span></td>'
            f'<td><a href="#ch_{idx:02}" class="toc-link"><strong>{html.escape(ch["title"])}</strong></a><br><span class="sub-en">{html.escape(ch["subtitle"])}</span></td>'
            f'<td style="text-align:center;">{len(ch["mcqs"])}</td>'
            f'</tr>'
        )

        blocks_html = []
        for b in ch["content"]:
            btype = b["type"]
            val = b["value"]
            if btype == "heading":
                is_part = val.startswith("भाग ") or val.startswith("ਸਾਲ-ਵਾਰ") or val.endswith("ਪ੍ਰੀਖਿਆ")
                cls = "part-heading" if is_part else "sub-heading"
                blocks_html.append(f'<h3 class="{cls}">{inline_md(val)}</h3>')
            elif btype == "callout":
                blocks_html.append(f'<div class="callout-box">{inline_md(val)}</div>')
            elif btype == "image":
                img_path = (IMAGES_DIR / val).resolve()
                img_uri = img_path.as_uri()
                caption = html.escape(b.get("caption", ""))
                blocks_html.append(
                    f'<figure class="diagram-fig">'
                    f'<img src="{img_uri}" alt="{caption}">'
                    f'<figcaption>{caption}</figcaption>'
                    f'</figure>'
                )
            else:
                blocks_html.append(render_text_block(val))

        chapter_sections.append(
            f'<section class="chapter-section" id="ch_{idx:02}">'
            f'<div class="chapter-header" style="border-left: 6px solid {badge_color};">'
            f'<div class="chapter-badge" style="color:{badge_color};">{html.escape(badge_text)}</div>'
            f'<h2 class="chapter-title">{html.escape(ch["title"])}</h2>'
            f'<div class="chapter-subtitle">{html.escape(ch["subtitle"])}</div>'
            f'</div>'
            f'{"".join(blocks_html)}'
            f'</section>'
        )

    html_doc = f"""<!DOCTYPE html>
<html lang="pa">
<head>
<meta charset="utf-8">
<title>RBSE Class 10 Punjabi (Code 75) — Complete Study Guide & Solved Papers (2014–2026)</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 16mm 15mm 18mm 15mm;
    @bottom-center {{
      content: "RBSE ਜਮਾਤ 10 ਪੰਜਾਬੀ (ਕੋਡ 75) · Setu Learning Guide — Page " counter(page) " of " counter(pages);
      font-family: "Nirmala UI", sans-serif;
      font-size: 8.5pt;
      color: #64748B;
    }}
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: "Nirmala UI", "Raavi", "Mangal", sans-serif;
    font-size: 10.5pt;
    line-height: 1.62;
    color: #0F172A;
    margin: 0;
    padding: 0;
    background: #FFFFFF;
  }}
  .cover-page {{
    border: 2px solid #0369A1;
    border-radius: 12px;
    padding: 24px 26px;
    background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 45%, #FFFBEB 100%);
    page-break-after: always;
  }}
  .cover-top-tag {{
    display: inline-block;
    background: #0369A1;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 9.5pt;
    padding: 5px 12px;
    border-radius: 6px;
    letter-spacing: 0.3px;
  }}
  .cover-title-pa {{
    font-size: 22pt;
    font-weight: 800;
    color: #0C4A6E;
    margin: 14px 0 6px 0;
    line-height: 1.3;
  }}
  .cover-title-hi {{
    font-size: 14.5pt;
    font-weight: 700;
    color: #7C2D12;
    margin: 0 0 6px 0;
  }}
  .cover-title-en {{
    font-size: 11pt;
    font-weight: 600;
    color: #475569;
    margin-bottom: 16px;
  }}
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 16px 0;
  }}
  .stat-card {{
    background: #FFFFFF;
    border: 1px solid #BAE6FD;
    border-top: 4px solid #0284C7;
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
  }}
  .stat-num {{
    font-size: 16pt;
    font-weight: 800;
    color: #0369A1;
  }}
  .stat-label {{
    font-size: 8.8pt;
    color: #334155;
    margin-top: 2px;
  }}
  .teacher-note {{
    background: #FFFBEB;
    border: 1px solid #F59E0B;
    border-left: 5px solid #D97706;
    border-radius: 8px;
    padding: 12px 15px;
    margin: 14px 0;
    font-size: 9.8pt;
  }}
  .teacher-note h4 {{
    margin: 0 0 6px 0;
    color: #92400E;
    font-size: 11pt;
  }}
  .toc-section {{
    page-break-after: always;
  }}
  .toc-heading {{
    font-size: 16pt;
    color: #0C4A6E;
    border-bottom: 2px solid #0284C7;
    padding-bottom: 6px;
    margin-top: 0;
  }}
  .toc-pill {{
    display: inline-block;
    font-size: 8pt;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
    white-space: nowrap;
  }}
  .toc-link {{
    color: #0F172A;
    text-decoration: none;
  }}
  .sub-en {{
    font-size: 8.5pt;
    color: #64748B;
  }}
  .chapter-section {{
    page-break-before: always;
  }}
  .chapter-header {{
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 14px;
  }}
  .chapter-badge {{
    font-size: 9pt;
    font-weight: 700;
    margin-bottom: 4px;
  }}
  .chapter-title {{
    font-size: 16pt;
    font-weight: 800;
    color: #0F172A;
    margin: 0 0 4px 0;
    line-height: 1.35;
  }}
  .chapter-subtitle {{
    font-size: 9.8pt;
    color: #475569;
    font-weight: 600;
  }}
  h3.part-heading {{
    background: #EFF6FF;
    color: #1E3A8A;
    border-left: 4px solid #2563EB;
    padding: 6px 12px;
    font-size: 11.8pt;
    margin: 16px 0 8px 0;
    border-radius: 0 6px 6px 0;
    page-break-after: avoid;
  }}
  h3.sub-heading {{
    color: #7C2D12;
    border-bottom: 1px solid #FED7AA;
    padding-bottom: 3px;
    font-size: 10.8pt;
    margin: 13px 0 6px 0;
    page-break-after: avoid;
  }}
  .callout-box {{
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-left: 4px solid #16A34A;
    padding: 9px 13px;
    border-radius: 6px;
    margin: 10px 0;
    font-size: 9.8pt;
    page-break-inside: avoid;
  }}
  .guide-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 9.5pt;
  }}
  .guide-table th {{
    background: #0F172A;
    color: #FFFFFF;
    text-align: left;
    padding: 6px 9px;
    font-weight: 700;
    border: 1px solid #0F172A;
  }}
  .guide-table td {{
    padding: 6px 9px;
    border: 1px solid #CBD5E1;
    vertical-align: top;
  }}
  .guide-table tr:nth-child(even) td {{
    background: #F8FAFC;
  }}
  .guide-table tr {{
    page-break-inside: avoid;
  }}
  figure.diagram-fig {{
    margin: 12px auto;
    text-align: center;
    background: #F8FAFC;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 8px;
    page-break-inside: avoid;
  }}
  figure.diagram-fig img {{
    max-width: 92%;
    max-height: 360px;
    height: auto;
    border-radius: 4px;
  }}
  figure.diagram-fig figcaption {{
    font-size: 8.8pt;
    color: #475569;
    margin-top: 5px;
    font-weight: 600;
  }}
  p {{
    margin: 6px 0 9px 0;
    text-align: left;
  }}
  a.ext-link {{
    color: #0369A1;
    text-decoration: none;
  }}
</style>
</head>
<body>

<div class="cover-page">
  <span class="cover-top-tag">ਮਾਧਿਅਮਿਕ ਸਿੱਖਿਆ ਬੋਰਡ ਰਾਜਸਥਾਨ, ਅਜਮੇਰ (RBSE) · ਵਿਸ਼ਾ ਕੋਡ: 75 · ਲੜੀ ਪੁਸਤਕ 7</span>
  <div class="cover-title-pa">ਜਮਾਤ 10 ਪੰਜਾਬੀ: ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ ਅਤੇ ਵਿਆਕਰਣ ਗਾਈਡ</div>
  <div class="cover-title-hi">आरबीएसई कक्षा 10 पंजाबी (तृतीया भाषा): संपूर्ण अध्यायवार अध्ययन मार्गदर्शिका</div>
  <div class="cover-title-en">Complete Bilingual (Gurmukhi + Hindi) Smart Study Guide & Solved RBSE Board Papers (2014–2026) — Subject Expert Review Copy</div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-num">23 ਪਾਠ</div>
      <div class="stat-label">22 ਮੁੱਖ ਪਾਠ + ਪਾਠ 23 ਬੋਰਡ ਪੇਪਰ ਬੈਂਕ</div>
    </div>
    <div class="stat-card">
      <div class="stat-num">80 ਅੰਕ</div>
      <div class="stat-label">RBSE 2025–26 ਅਧਿਕਾਰਤ ਅੰਕ-ਭਾਰ</div>
    </div>
    <div class="stat-card">
      <div class="stat-num">348 MCQs</div>
      <div class="stat-label">ਕਾਰਨ-ਸਹਿਤ ਉੱਤਰ-ਕੁੰਜੀ ਸਮੇਤ</div>
    </div>
    <div class="stat-card">
      <div class="stat-num">221 PYQs</div>
      <div class="stat-label">17 ਅਧਿਕਾਰਤ ਪੇਪਰ (2014–2026) ਹੱਲ</div>
    </div>
  </div>

  <div class="teacher-note">
    <h4>ਪੰਜਾਬੀ ਵਿਸ਼ਾ-ਮਾਹਿਰ / ਅਧਿਆਪਕ ਸਾਹਿਬਾਨ ਲਈ ਸਮੀਖਿਆ ਨੋਟ (Note for the Punjabi Subject Teacher)</h4>
    <p style="margin:0;">ਇਹ ਪੁਸਤਕ <strong>Setu Learning Android App</strong> ਲਈ ਰਾਜਸਥਾਨ ਬੋਰਡ (RBSE) ਜਮਾਤ 10 ਦੀ ਤੀਜੀ ਭਾਸ਼ਾ <strong>ਪੰਜਾਬੀ (ਵਿਸ਼ਾ ਕੋਡ: 75)</strong> ਦੀ ਅਧਿਕਾਰਤ ਪਾਠ-ਪੁਸਤਕ <strong>'ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ'</strong> (ਕਾਵਿ ਭਾਗ, ਨਿਬੰਧ ਭਾਗ, ਕਹਾਣੀ ਭਾਗ) ਅਤੇ ਨਿਰਧਾਰਿਤ 2025–2026 ਪਾਠਕ੍ਰਮ ਦੇ ਆਧਾਰ ਉੱਤੇ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਹੇਠਾਂ ਦਿੱਤੇ ਬਿੰਦੂਆਂ ਦੀ ਵਿਸ਼ੇਸ਼ ਜਾਂਚ ਕਰਨ ਦੀ ਕ੍ਰਿਪਾਲਤਾ ਕਰੋ: (1) ਕਾਵਿ-ਬੰਦਾਂ ਦੀ ਪ੍ਰਸੰਗ-ਸਹਿਤ ਵਿਆਖਿਆ ਅਤੇ ਕੇਂਦਰੀ ਭਾਵ, (2) ਨਿਬੰਧਾਂ ਤੇ ਕਹਾਣੀਆਂ ਦੇ ਸਾਰ ਅਤੇ ਪਾਤਰ-ਚਿਤਰਣ, (3) ਗੁਰਮੁਖੀ ਲਿਪੀ, ਲਗਾਂ-ਮਾਤਰਾਵਾਂ, ਲਗਾਖਰ (ਬਿੰਦੀ, ਟਿੱਪੀ, ਅੱਧਕ) ਅਤੇ ਦੁੱਤ ਅੱਖਰਾਂ ਦੇ ਨਿਯਮ, ਅਤੇ (4) ਪਾਠ 23 ਵਿੱਚ ਦਿੱਤੇ 2014–2026 ਦੇ ਬੋਰਡ ਪ੍ਰਸ਼ਨ-ਪੱਤਰਾਂ ਦੇ ਹੱਲ।</p>
  </div>

  <h3 class="part-heading" style="margin-top:14px;">RBSE ਜਮਾਤ 10 ਪੰਜਾਬੀ (ਕੋਡ 75) — ਅਧਿਕਾਰਤ 80-ਅੰਕ ਬਲੂਪ੍ਰਿੰਟ (2025–2026)</h3>
  <table class="guide-table">
    <thead>
      <tr>
        <th>ਇਕਾਈ / ਭਾਗ (Section)</th>
        <th>ਨਿਰਧਾਰਿਤ ਵਿਸ਼ਾ-ਵਸਤੂ (Prescribed Syllabus Content)</th>
        <th>ਪਾਠ ਕ੍ਰਮਾਂਕ</th>
        <th>ਅੰਕ-ਭਾਰ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਕਾਵਿ ਭਾਗ</strong></td>
        <td>ਗੁਰਮਤਿ ਕਾਵਿ (ਸ਼ੇਖ਼ ਫ਼ਰੀਦ, ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਜੀ, ਗੁਰੂ ਅਮਰਦਾਸ ਜੀ, ਗੁਰੂ ਰਾਮਦਾਸ ਜੀ, ਭਾਈ ਗੁਰਦਾਸ ਜੀ), ਸੂਫ਼ੀ ਕਾਵਿ (ਮੀਆਂ ਵਜ਼ੀਦ, ਬੁੱਲ੍ਹੇ ਸ਼ਾਹ) ਅਤੇ ਆਧੁਨਿਕ ਕਾਵਿ (ਭਾਈ ਵੀਰ ਸਿੰਘ, ਧਨੀ ਰਾਮ ਚਾਤ੍ਰਿਕ, ਪ੍ਰੋ. ਮੋਹਨ ਸਿੰਘ, ਅੰਮ੍ਰਿਤਾ ਪ੍ਰੀਤਮ, ਸ਼ਿਵ ਕੁਮਾਰ ਬਟਾਲਵੀ, ਸੁਰਜੀਤ ਪਾਤਰ)</td>
        <td>ਪਾਠ 1 ਤੋਂ 7</td>
        <td><strong>15 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>2. ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਨਿਬੰਧ ਭਾਗ</strong></td>
        <td>ਕਿਰਤ (ਪੂਰਨ ਸਿੰਘ), ਗੰਗਾ ਦੀਨ (ਤੇਜਾ ਸਿੰਘ), ਫਲਾਇੰਗ ਸਿੱਖ ਮਿਲਖਾ ਸਿੰਘ (ਸਰਵਣ ਸਿੰਘ), ਮਹਾਰਾਜਾ ਗੰਗਾ ਸਿੰਘ (ਲਖਵਿੰਦਰ ਸਿੰਘ ਲੱਖੀਆਂ), ਰਾਜਸਥਾਨ ਦੇ ਪ੍ਰਸਿੱਧ ਕਿਲ੍ਹੇ (ਗੁਰਬਚਨ ਸਿੰਘ ਭੁੱਲਰ), ਭਾਈ ਮਰਦਾਨਾ ਜੀ (ਹਰਪਾਲ ਸਿੰਘ ਪੰਨੂ)</td>
        <td>ਪਾਠ 8 ਤੋਂ 13</td>
        <td><strong>15 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>3. ਸਾਹਿਤ ਸੁਗੰਧੀਆਂ — ਕਹਾਣੀ ਭਾਗ</strong></td>
        <td>ਬਾਗ਼ੀ ਦੀ ਧੀ (ਗੁਰਬਖ਼ਸ਼ ਸਿੰਘ ਪ੍ਰੀਤਲੜੀ), ਪੇਮੀ ਦੇ ਨਿਆਣੇ (ਸੰਤ ਸਿੰਘ ਸੇਖੋਂ), ਸਾਂਝੀ ਕੰਧ (ਸੰਤੋਖ ਸਿੰਘ ਧੀਰ), ਦੁੱਧ ਦਾ ਛੱਪੜ (ਕੁਲਵੰਤ ਸਿੰਘ ਵਿਰਕ), ਖੂਨ (ਗੁਰਬਚਨ ਸਿੰਘ ਭੁੱਲਰ)</td>
        <td>ਪਾਠ 14 ਤੋਂ 18</td>
        <td><strong>15 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>4. ਵਿਆਕਰਣ ਭਾਗ</strong></td>
        <td>ਭਾਸ਼ਾ ਅਤੇ ਪੰਜਾਬੀ ਦੀਆਂ ਉਪ-ਭਾਸ਼ਾਵਾਂ, ਧੁਨੀ ਅਤੇ ਗੁਰਮੁਖੀ ਲਿਪੀ (ਲਗਾਂ, ਲਗਾਖਰ, ਦੁੱਤ ਅੱਖਰ); ਅਰਥ-ਬੋਧ (ਵਿਰੋਧੀ, ਸਮਾਨਾਰਥਕ ਅਤੇ ਬਹੁ-ਅਰਥਕ ਸ਼ਬਦ)</td>
        <td>ਪਾਠ 19 ਤੋਂ 20</td>
        <td><strong>12 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>5. ਅਣਡਿੱਠਾ ਪੈਰ੍ਹਾ</strong></td>
        <td>ਦੋ ਅਣਡਿੱਠੇ ਪੈਰ੍ਹੇ (150 ਸ਼ਬਦਾਂ ਦੇ ਦੋ ਗਦਿਆਂਸ਼ — ਪ੍ਰਸ਼ਨੋੱਤਰ ਅਤੇ ਢੁਕਵਾਂ ਸਿਰਲੇਖ: 5 + 5 ਅੰਕ)</td>
        <td>ਪਾਠ 21</td>
        <td><strong>10 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>6. ਨਿਬੰਧ ਅਤੇ ਪੱਤਰ-ਰਚਨਾ</strong></td>
        <td>ਨਿਬੰਧ / ਲੇਖ ਰਚਨਾ (200 ਸ਼ਬਦ: 7 ਅੰਕ) ਅਤੇ ਪੱਤਰ-ਰਚਨਾ — ਨਿੱਜੀ, ਦਫ਼ਤਰੀ ਅਤੇ ਵਪਾਰੀ ਪੱਤਰ (6 ਅੰਕ)</td>
        <td>ਪਾਠ 22</td>
        <td><strong>13 ਅੰਕ</strong></td>
      </tr>
      <tr>
        <td><strong>7. ਬੋਰਡ ਪ੍ਰਸ਼ਨ-ਪੱਤਰ ਬੈਂਕ (2014–2026)</strong></td>
        <td>17 ਅਧਿਕਾਰਤ RBSE ਮੁੱਖ ਅਤੇ ਪੂਰਕ ਪ੍ਰਸ਼ਨ-ਪੱਤਰਾਂ (S-75) ਦੇ 221 ਸਰੋਤ-ਪ੍ਰਮਾਣਿਤ ਹੱਲ ਅਤੇ 18 ਦੁਹਰਾਈ MCQs</td>
        <td>ਪਾਠ 23</td>
        <td><strong>ਅਭਿਆਸ ਬੈਂਕ</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="toc-section">
  <h2 class="toc-heading">ਵਿਸ਼ਾ-ਸੂਚੀ (अनुक्रमणिका / Table of Contents)</h2>
  <table class="guide-table">
    <thead>
      <tr>
        <th style="width:45px;text-align:center;">ਕ੍ਰ.</th>
        <th style="width:170px;">ਭਾਗ / ਖੰਡ</th>
        <th>ਪਾਠ ਦਾ ਨਾਂ (Chapter Title & Subtitle)</th>
        <th style="width:55px;text-align:center;">MCQs</th>
      </tr>
    </thead>
    <tbody>
      {"".join(toc_rows)}
    </tbody>
  </table>
</div>

{"".join(chapter_sections)}

</body>
</html>
"""
    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    HTML_PATH.write_text(html_doc, encoding="utf-8")
    return HTML_PATH


def render_pdf(html_file: Path, pdf_file: Path):
    chrome_candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    browser = next((p for p in chrome_candidates if p.exists()), None)
    if browser is None:
        raise RuntimeError("No Chrome or Edge browser found for headless PDF generation.")

    cmd = [
        str(browser),
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_file}",
        html_file.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    html_file = build_html()
    print(f"Generated HTML: {html_file} ({html_file.stat().st_size / 1024:.1f} KB)")
    render_pdf(html_file, PDF_PATH)
    ARTIFACT_PDF_PATH.write_bytes(PDF_PATH.read_bytes())
    print(f"Generated PDF:  {PDF_PATH} ({PDF_PATH.stat().st_size / (1024 * 1024):.2f} MB)")
    print(f"Copied PDF to:  {ARTIFACT_PDF_PATH}")
