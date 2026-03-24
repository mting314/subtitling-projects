#!/usr/bin/env python3
"""Generate side-by-side JP vs EN comparison reports for translated subtitle files.

Reads a source (Japanese) and translated (English) ASS file, produces an interactive
HTML report with the same dark theme as quality_report.py.
"""

import argparse
import os
import sys
from pathlib import Path

from utils.ass_parser import parse_ass, extract_dialogue_lines, seconds_to_timestamp


def generate_comparison_html(
    source_lines: list[dict],
    translated_lines: list[dict],
    html_path: str,
    video_path: str | None = None,
    title: str | None = None,
):
    """Generate an interactive HTML comparison report."""
    path = Path(html_path)
    num_lines = min(len(source_lines), len(translated_lines))

    total_jp_chars = sum(len(l["text"]) for l in source_lines[:num_lines])
    total_en_chars = sum(len(l["text"]) for l in translated_lines[:num_lines])
    ratio = total_en_chars / total_jp_chars if total_jp_chars > 0 else 0

    # Resolve video path
    video_src = None
    if video_path:
        vp = Path(video_path)
        if vp.is_file():
            try:
                video_src = os.path.relpath(vp, path.parent)
            except ValueError:
                video_src = str(vp.resolve())

    # Stats HTML
    stats_html = f"""<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">{num_lines}</div><div class="stat-label">Lines</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_jp_chars}</div><div class="stat-label">JP Characters</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_en_chars}</div><div class="stat-label">EN Characters</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{ratio:.2f}</div><div class="stat-label">EN/JP Ratio</div>
  </div>
</div>"""

    # Video player
    if video_src:
        escaped_video_src = video_src.replace("&", "&amp;").replace('"', "&quot;")
        video_html = f"""<div id="player-section">
  <div id="video-wrap">
    <video id="video" controls preload="metadata">
      <source src="{escaped_video_src}">
    </video>
  </div>
  <div id="now-playing">
    <div id="now-header">
      <span id="now-line-num"></span>
      <span id="now-time"></span>
    </div>
    <div id="now-jp" class="now-text">Click a line to preview</div>
    <div id="now-en" class="now-text"></div>
  </div>
</div>"""
        video_css = """
  #player-section { display: flex; gap: 16px; align-items: stretch; padding: 8px 0; }
  #video-wrap { width: 420px; min-width: 200px; flex-shrink: 0; resize: horizontal; overflow: hidden; }
  #video { width: 100%; background: #000; border-radius: 8px; display: block; }
  #now-playing { flex: 1; background: #16213e; border-radius: 8px; padding: 10px 14px;
                  border: 1px solid #2a3a5c; display: flex; flex-direction: column; gap: 6px; }
  #now-header { display: flex; justify-content: space-between; margin-bottom: 4px; }
  #now-line-num { font-size: 0.75em; color: #4d94ff; font-weight: 600; }
  #now-time { font-size: 0.75em; color: #888; font-family: monospace; }
  .now-text { font-size: 1em; line-height: 1.5; background: #0d1a30;
              border: 1px solid #2a3a5c; border-radius: 6px; padding: 10px 12px;
              white-space: pre-wrap; word-break: break-word; flex: 1; overflow-y: auto; }
  #now-jp { color: #ffcc66; }
  #now-en { color: #66ccff; }
  th { top: 0; }"""
    else:
        video_html = ""
        video_css = ""

    # Build table rows
    table_rows = []
    for i in range(num_lines):
        src = source_lines[i]
        tgt = translated_lines[i]
        jp_chars = len(src["text"])
        en_chars = len(tgt["text"])
        dur = src["end"] - src["start"]

        # Color coding for char ratio
        if jp_chars > 0:
            line_ratio = en_chars / jp_chars
        else:
            line_ratio = 1.0

        row_class = ""
        data_filter = ""
        if line_ratio < 0.3 and jp_chars > 5:
            row_class = "severity-orange"
            data_filter = 'data-issue-short="1"'
        elif line_ratio > 3.0 and jp_chars > 3:
            row_class = "severity-yellow"
            data_filter = 'data-issue-long="1"'

        escaped_jp = src["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        escaped_en = tgt["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        table_rows.append(
            f'<tr class="{row_class}" {data_filter} '
            f'data-start="{src["start"]:.3f}" data-end="{src["end"]:.3f}" '
            f'data-jp="{escaped_jp}" data-en="{escaped_en}" '
            f'onclick="onRowClick(this)">'
            f"<td>{i + 1}</td>"
            f"<td>{seconds_to_timestamp(src['start'])}</td>"
            f"<td>{seconds_to_timestamp(src['end'])}</td>"
            f"<td>{dur:.2f}s</td>"
            f"<td>{src['style']}</td>"
            f"<td class=\"jp-text\">{escaped_jp}</td>"
            f"<td class=\"en-text\">{escaped_en}</td>"
            f"<td>{jp_chars}/{en_chars}</td>"
            f"</tr>"
        )

    rows_html = "\n".join(table_rows)

    # Count issues for filter buttons
    short_count = sum(1 for i in range(num_lines)
                      if len(source_lines[i]["text"]) > 5
                      and len(translated_lines[i]["text"]) / max(len(source_lines[i]["text"]), 1) < 0.3)
    long_count = sum(1 for i in range(num_lines)
                     if len(source_lines[i]["text"]) > 3
                     and len(translated_lines[i]["text"]) / max(len(source_lines[i]["text"]), 1) > 3.0)

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title or "Translation Comparison"}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         background: #1a1a2e; color: #e0e0e0; padding: 20px; }}
  h1 {{ color: #fff; margin-bottom: 16px; }}
  .stats-grid {{ display: flex; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }}
  .stat-card {{ background: #16213e; border-radius: 8px; padding: 16px; flex: 1; min-width: 150px; }}
  .stat-value {{ font-size: 1.5em; font-weight: bold; color: #fff; }}
  .stat-label {{ font-size: 0.85em; color: #888; margin-top: 4px; }}
  #sticky-top {{ position: sticky; top: 0; z-index: 10; background: #1a1a2e; padding-bottom: 4px; }}
  .filters {{ margin: 8px 0; display: flex; gap: 8px; flex-wrap: wrap; }}
  .filter-btn {{ border: none; border-radius: 6px; padding: 8px 16px; cursor: pointer;
                 font-size: 0.85em; font-weight: 600; transition: opacity 0.2s; }}
  .filter-btn.inactive {{ opacity: 0.35; }}
  .btn-all {{ background: #555; color: #fff; }}
  .btn-orange {{ background: #ff9933; color: #fff; }}
  .btn-yellow {{ background: #e6c300; color: #1a1a2e; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 0.85em; }}
  th {{ background: #0f3460; color: #fff; padding: 10px 8px; text-align: left;
       position: sticky; top: 0; z-index: 2; }}
  td {{ padding: 8px; border-bottom: 1px solid #222; vertical-align: top; }}
  tr {{ cursor: pointer; transition: background 0.15s; }}
  tr:hover {{ background: #1e2d4a !important; }}
  tr.selected {{ outline: 2px solid #4d94ff; }}
  .severity-orange {{ background: rgba(255,153,51,0.12); }}
  .severity-yellow {{ background: rgba(230,195,0,0.10); }}
  .jp-text {{ color: #ffcc66; }}
  .en-text {{ color: #66ccff; }}
  .hidden-row {{ display: none !important; }}{video_css}
</style>
</head>
<body>
<h1>Translation Comparison{f" &mdash; {title}" if title else ""}</h1>
{stats_html}
<div id="sticky-top">
{video_html}
<div class="filters">
  <button class="filter-btn btn-all" onclick="filterAll()">All</button>
  <button class="filter-btn btn-orange" data-filter="short" onclick="toggleFilter(this)">
    Short translations ({short_count})</button>
  <button class="filter-btn btn-yellow" data-filter="long" onclick="toggleFilter(this)">
    Long translations ({long_count})</button>
</div>
</div>
<table>
<thead><tr>
  <th>#</th><th>Start</th><th>End</th><th>Duration</th>
  <th>Style</th><th>Japanese</th><th>English</th><th>Chars (JP/EN)</th>
</tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<script>
const video = document.getElementById('video');
const nowLineNum = document.getElementById('now-line-num');
const nowTime = document.getElementById('now-time');
const nowJp = document.getElementById('now-jp');
const nowEn = document.getElementById('now-en');
let selectedRow = null;

function onRowClick(row) {{
  if (selectedRow) selectedRow.classList.remove('selected');
  row.classList.add('selected');
  selectedRow = row;
  const lineNum = row.cells[0].textContent;
  const startTime = row.cells[1].textContent;
  const endTime = row.cells[2].textContent;
  if (nowLineNum) nowLineNum.textContent = 'Line #' + lineNum;
  if (nowTime) nowTime.textContent = startTime + ' \\u2192 ' + endTime;
  if (nowJp) nowJp.textContent = row.getAttribute('data-jp');
  if (nowEn) nowEn.textContent = row.getAttribute('data-en');
  if (video) {{
    const t = parseFloat(row.getAttribute('data-start'));
    video.currentTime = t;
    video.play();
  }}
}}

const activeFilters = new Set();
function applyFilters() {{
  const rows = document.querySelectorAll('tbody tr');
  rows.forEach(row => {{
    if (activeFilters.size === 0) {{
      row.classList.remove('hidden-row');
      return;
    }}
    let show = false;
    for (const f of activeFilters) {{
      if (row.getAttribute('data-issue-' + f) === '1') show = true;
    }}
    row.classList.toggle('hidden-row', !show);
  }});
  document.querySelectorAll('.filter-btn[data-filter]').forEach(btn => {{
    btn.classList.toggle('inactive', activeFilters.size > 0 && !activeFilters.has(btn.dataset.filter));
  }});
}}
function toggleFilter(btn) {{
  const f = btn.dataset.filter;
  if (activeFilters.has(f)) activeFilters.delete(f); else activeFilters.add(f);
  applyFilters();
}}
function filterAll() {{
  activeFilters.clear();
  applyFilters();
}}
// Pin table headers below sticky top bar
(function() {{
  const stickyTop = document.getElementById('sticky-top');
  if (!stickyTop) return;
  function updateThTop() {{
    const h = stickyTop.offsetHeight;
    document.querySelectorAll('th').forEach(th => th.style.top = h + 'px');
  }}
  updateThTop();
  window.addEventListener('resize', updateThTop);
  new ResizeObserver(updateThTop).observe(stickyTop);
}})();
</script>
</body>
</html>"""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Generate side-by-side JP vs EN comparison report for translated subtitles."
    )
    parser.add_argument(
        "--source", required=True,
        help="Source ASS file (Japanese)",
    )
    parser.add_argument(
        "--translated", required=True,
        help="Translated ASS file (English)",
    )
    parser.add_argument(
        "--video", default=None,
        help="Path to source video file for embedded player",
    )
    parser.add_argument(
        "--title", default=None,
        help="Report title (default: translated filename)",
    )

    args = parser.parse_args()

    source_path = Path(args.source)
    translated_path = Path(args.translated)

    if not source_path.is_file():
        parser.error(f"Source file not found: {args.source}")
    if not translated_path.is_file():
        parser.error(f"Translated file not found: {args.translated}")

    title = args.title or translated_path.stem

    print(f"Generating comparison report...")
    print(f"  Source:     {source_path}")
    print(f"  Translated: {translated_path}")

    # Parse both files
    source_data = parse_ass(source_path)
    translated_data = parse_ass(translated_path)

    source_lines = extract_dialogue_lines(source_data["events"])
    translated_lines = extract_dialogue_lines(translated_data["events"])

    if len(source_lines) != len(translated_lines):
        print(
            f"  Warning: line count mismatch (source: {len(source_lines)}, "
            f"translated: {len(translated_lines)})",
            file=sys.stderr,
        )

    html_path = translated_path.with_stem(translated_path.stem + "_comparison").with_suffix(".html")
    generate_comparison_html(
        source_lines,
        translated_lines,
        str(html_path),
        video_path=args.video,
        title=title,
    )

    num_lines = min(len(source_lines), len(translated_lines))
    total_jp = sum(len(l["text"]) for l in source_lines[:num_lines])
    total_en = sum(len(l["text"]) for l in translated_lines[:num_lines])

    print(f"\n  Lines:      {num_lines}")
    print(f"  JP chars:   {total_jp}")
    print(f"  EN chars:   {total_en}")
    print(f"  Report:     {html_path}")


if __name__ == "__main__":
    main()
