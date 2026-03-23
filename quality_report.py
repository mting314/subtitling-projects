"""Quality analysis and reporting for ASS subtitle files.

Provides structured quality analysis, console output, plain text log files,
and interactive HTML reports with color-coded issue highlighting.
"""

import os
from pathlib import Path

from utils.time import seconds_to_timestamp


def analyze_quality(lines: list[dict]) -> dict:
    """Analyze dialogue lines for quality issues. Returns structured report data."""
    if not lines:
        return {
            "stats": {
                "num_lines": 0,
                "total_chars": 0,
                "time_range": None,
                "length_stats": None,
                "duration_stats": None,
            },
            "issues": {
                "zero_duration": [],
                "long_lines": [],
                "short_lines": [],
                "long_duration": [],
                "inverted": [],
                "overlaps": [],
                "large_gaps": [],
            },
        }

    text_lengths = [len(line["text"]) for line in lines]
    durations = [line["end"] - line["start"] for line in lines]
    total_chars = sum(text_lengths)
    sorted_lengths = sorted(text_lengths)
    sorted_durations = sorted(durations)

    stats = {
        "num_lines": len(lines),
        "total_chars": total_chars,
        "time_range": (lines[0]["start"], lines[-1]["end"]),
        "length_stats": {
            "min": min(text_lengths),
            "max": max(text_lengths),
            "mean": total_chars / len(lines),
            "median": sorted_lengths[len(sorted_lengths) // 2],
        },
        "duration_stats": {
            "min": min(durations),
            "max": max(durations),
            "mean": sum(durations) / len(durations),
            "median": sorted_durations[len(sorted_durations) // 2],
        },
    }

    issues = {
        "zero_duration": [i for i, d in enumerate(durations) if d <= 0],
        "long_lines": [
            (i, length) for i, length in enumerate(text_lengths) if length > 200
        ],
        "short_lines": [
            (i, lines[i]["text"]) for i, length in enumerate(text_lengths) if length < 3
        ],
        "long_duration": [(i, d) for i, d in enumerate(durations) if d > 60],
        "inverted": [i for i, d in enumerate(durations) if d < 0],
        "overlaps": [
            i
            for i in range(len(lines) - 1)
            if lines[i + 1]["start"] < lines[i]["end"] - 0.1
        ],
        "large_gaps": [
            (i, lines[i + 1]["start"] - lines[i]["end"])
            for i in range(len(lines) - 1)
            if lines[i + 1]["start"] - lines[i]["end"] > 30
        ],
    }

    return {"stats": stats, "issues": issues}


def print_quality_report(lines: list[dict]):
    """Print ASS file stats and quality warnings."""
    report = analyze_quality(lines)
    stats = report["stats"]
    issues = report["issues"]

    if stats["num_lines"] == 0:
        print("  Dialogue lines: 0")
        print("\n  WARNING: No dialogue lines generated!")
        return

    time_start, time_end = stats["time_range"]
    ls = stats["length_stats"]
    ds = stats["duration_stats"]

    print("\n  --- ASS File Stats ---")
    print(f"  Dialogue lines:  {stats['num_lines']}")
    print(f"  Total characters: {stats['total_chars']}")
    print(
        f"  Time range:      {seconds_to_timestamp(time_start)} - {seconds_to_timestamp(time_end)}"
    )

    print("\n  --- Line Length (characters) ---")
    print(f"  Min:     {ls['min']}")
    print(f"  Max:     {ls['max']}")
    print(f"  Mean:    {ls['mean']:.1f}")
    print(f"  Median:  {ls['median']}")

    print("\n  --- Line Duration (seconds) ---")
    print(f"  Min:     {ds['min']:.2f}s")
    print(f"  Max:     {ds['max']:.2f}s")
    print(f"  Mean:    {ds['mean']:.2f}s")
    print(f"  Median:  {ds['median']:.2f}s")

    issue_lines = []

    if issues["zero_duration"]:
        issue_lines.append(
            f"  - {len(issues['zero_duration'])} line(s) with zero or negative duration "
            f"(likely bogus timestamps)"
        )
        for idx in issues["zero_duration"][:5]:
            line = lines[idx]
            issue_lines.append(
                f"      line {idx + 1}: {seconds_to_timestamp(line['start'])} -> "
                f'{seconds_to_timestamp(line["end"])}  "{line["text"][:50]}"'
            )
        if len(issues["zero_duration"]) > 5:
            issue_lines.append(f"      ... and {len(issues['zero_duration']) - 5} more")

    if issues["long_lines"]:
        issue_lines.append(
            f"  - {len(issues['long_lines'])} line(s) over 200 characters "
            f"(may need manual splitting in Aegisub)"
        )
        for idx, length in issues["long_lines"][:3]:
            issue_lines.append(f"      line {idx + 1}: {length} chars")
        if len(issues["long_lines"]) > 3:
            issue_lines.append(f"      ... and {len(issues['long_lines']) - 3} more")

    if issues["short_lines"]:
        issue_lines.append(
            f"  - {len(issues['short_lines'])} line(s) under 3 characters "
            f"(likely noise or artifacts)"
        )
        for idx, text in issues["short_lines"][:5]:
            issue_lines.append(f'      line {idx + 1}: "{text}"')
        if len(issues["short_lines"]) > 5:
            issue_lines.append(f"      ... and {len(issues['short_lines']) - 5} more")

    if issues["long_duration"]:
        issue_lines.append(
            f"  - {len(issues['long_duration'])} line(s) spanning over 60 seconds "
            f"(likely timestamp gaps from API)"
        )
        for idx, dur in issues["long_duration"][:3]:
            line = lines[idx]
            issue_lines.append(
                f"      line {idx + 1}: {dur:.1f}s  "
                f"{seconds_to_timestamp(line['start'])} -> {seconds_to_timestamp(line['end'])}"
            )
        if len(issues["long_duration"]) > 3:
            issue_lines.append(f"      ... and {len(issues['long_duration']) - 3} more")

    if issues["inverted"]:
        issue_lines.append(
            f"  - {len(issues['inverted'])} line(s) with end time before start time "
            f"(bogus timestamps)"
        )
        for idx in issues["inverted"][:3]:
            line = lines[idx]
            issue_lines.append(
                f"      line {idx + 1}: {seconds_to_timestamp(line['start'])} -> "
                f"{seconds_to_timestamp(line['end'])}"
            )
        if len(issues["inverted"]) > 3:
            issue_lines.append(f"      ... and {len(issues['inverted']) - 3} more")

    if issues["overlaps"]:
        issue_lines.append(
            f"  - {len(issues['overlaps'])} pair(s) of overlapping lines "
            f"(next line starts before current ends)"
        )
        for idx in issues["overlaps"][:3]:
            issue_lines.append(
                f"      lines {idx + 1}-{idx + 2}: "
                f"end={seconds_to_timestamp(lines[idx]['end'])} > "
                f"start={seconds_to_timestamp(lines[idx + 1]['start'])}"
            )
        if len(issues["overlaps"]) > 3:
            issue_lines.append(f"      ... and {len(issues['overlaps']) - 3} more")

    if issues["large_gaps"]:
        issue_lines.append(
            f"  - {len(issues['large_gaps'])} gap(s) over 30 seconds between lines "
            f"(silence, music, or missed speech)"
        )
        for idx, gap in issues["large_gaps"][:3]:
            issue_lines.append(
                f"      between lines {idx + 1}-{idx + 2}: "
                f"{gap:.1f}s gap at {seconds_to_timestamp(lines[idx]['end'])}"
            )
        if len(issues["large_gaps"]) > 3:
            issue_lines.append(f"      ... and {len(issues['large_gaps']) - 3} more")

    if issue_lines:
        print(f"\n  --- Quality Warnings ({len(issue_lines)} issues) ---")
        for issue in issue_lines:
            print(issue)
    else:
        print("\n  --- Quality: No issues detected ---")


def write_quality_log(lines: list[dict], report: dict, log_path: str):
    """Write full quality report to a plain text log file (untruncated)."""
    path = Path(log_path)
    stats = report["stats"]
    issues = report["issues"]

    out = []
    out.append("=== Quality Report ===\n")

    if stats["num_lines"] == 0:
        out.append("Dialogue lines: 0\nWARNING: No dialogue lines generated!\n")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(out), encoding="utf-8")
        return

    time_start, time_end = stats["time_range"]
    ls = stats["length_stats"]
    ds = stats["duration_stats"]

    out.append("--- Stats ---")
    out.append(f"Dialogue lines:  {stats['num_lines']}")
    out.append(f"Total characters: {stats['total_chars']}")
    out.append(
        f"Time range:      {seconds_to_timestamp(time_start)} - {seconds_to_timestamp(time_end)}"
    )
    out.append("")
    out.append("--- Line Length (characters) ---")
    out.append(f"Min:     {ls['min']}")
    out.append(f"Max:     {ls['max']}")
    out.append(f"Mean:    {ls['mean']:.1f}")
    out.append(f"Median:  {ls['median']}")
    out.append("")
    out.append("--- Line Duration (seconds) ---")
    out.append(f"Min:     {ds['min']:.2f}s")
    out.append(f"Max:     {ds['max']:.2f}s")
    out.append(f"Mean:    {ds['mean']:.2f}s")
    out.append(f"Median:  {ds['median']:.2f}s")

    def _log_lines_by_index(label, indices):
        out.append(f"\n--- {label} ({len(indices)} lines) ---")
        for idx in indices:
            line = lines[idx]
            dur = line["end"] - line["start"]
            out.append(
                f"  line {idx + 1}: {seconds_to_timestamp(line['start'])} -> "
                f"{seconds_to_timestamp(line['end'])}  ({dur:.2f}s)  "
                f'"{line["text"][:80]}"'
            )

    def _log_lines_with_value(label, items, fmt_value):
        out.append(f"\n--- {label} ({len(items)} lines) ---")
        for item in items:
            idx = item[0]
            val = item[1]
            line = lines[idx]
            out.append(
                f"  line {idx + 1}: {seconds_to_timestamp(line['start'])} -> "
                f"{seconds_to_timestamp(line['end'])}  {fmt_value(val)}  "
                f'"{line["text"][:80]}"'
            )

    if issues["zero_duration"]:
        _log_lines_by_index(
            "Zero/negative duration (bogus timestamps)", issues["zero_duration"]
        )

    if issues["inverted"]:
        _log_lines_by_index(
            "Inverted timestamps (end before start)", issues["inverted"]
        )

    if issues["long_lines"]:
        _log_lines_with_value(
            "Long lines (>200 chars)",
            issues["long_lines"],
            lambda v: f"{v} chars",
        )

    if issues["short_lines"]:
        _log_lines_with_value(
            "Short lines (<3 chars)",
            issues["short_lines"],
            lambda v: f'text="{v}"',
        )

    if issues["long_duration"]:
        _log_lines_with_value(
            "Long duration (>60s)",
            issues["long_duration"],
            lambda v: f"{v:.1f}s",
        )

    if issues["overlaps"]:
        out.append(f"\n--- Overlapping lines ({len(issues['overlaps'])} pairs) ---")
        for idx in issues["overlaps"]:
            out.append(
                f"  lines {idx + 1}-{idx + 2}: "
                f"end={seconds_to_timestamp(lines[idx]['end'])} > "
                f"start={seconds_to_timestamp(lines[idx + 1]['start'])}"
            )

    if issues["large_gaps"]:
        out.append(f"\n--- Large gaps >30s ({len(issues['large_gaps'])} gaps) ---")
        for idx, gap in issues["large_gaps"]:
            out.append(
                f"  between lines {idx + 1}-{idx + 2}: "
                f"{gap:.1f}s gap at {seconds_to_timestamp(lines[idx]['end'])}"
            )

    has_issues = any(v for v in issues.values())
    if not has_issues:
        out.append("\n--- No issues detected ---")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


_SEVERITY_ORDER = {"red": 0, "orange": 1, "yellow": 2, "blue": 3}


def write_quality_html(
    lines: list[dict],
    report: dict,
    html_path: str,
    video_path: str | None = None,
    title: str | None = None,
):
    """Write an interactive HTML quality report with color-coded lines.

    If video_path is provided and the file exists, embeds an HTML5 video player
    with click-to-seek and a sticky selected-line display.
    """
    path = Path(html_path)
    stats = report["stats"]
    issues = report["issues"]

    # Pre-compute issue sets for O(1) lookup
    issue_sets = {
        "zero_duration": set(issues["zero_duration"]),
        "inverted": set(issues["inverted"]),
        "overlaps": set(issues["overlaps"]),
        "long_lines": {i for i, _ in issues["long_lines"]},
        "short_lines": {i for i, _ in issues["short_lines"]},
        "long_duration": {i for i, _ in issues["long_duration"]},
        "large_gaps": {i for i, _ in issues["large_gaps"]},
        "after_large_gaps": {i + 1 for i, _ in issues["large_gaps"]},
    }

    def get_row_issues(idx):
        result = []
        if idx in issue_sets["zero_duration"]:
            result.append(("red", "Zero/negative duration"))
        if idx in issue_sets["inverted"]:
            result.append(("red", "Inverted timestamps"))
        if idx in issue_sets["long_duration"]:
            result.append(("orange", "Duration >60s"))
        if idx in issue_sets["overlaps"]:
            result.append(("orange", "Overlaps next line"))
        if idx in issue_sets["long_lines"]:
            result.append(("yellow", "Text >200 chars"))
        if idx in issue_sets["short_lines"]:
            result.append(("yellow", "Text <3 chars"))
        if idx in issue_sets["large_gaps"]:
            result.append(("blue", "Large gap before next line"))
        if idx in issue_sets["after_large_gaps"]:
            result.append(("blue", "After large gap"))
        return result

    # Build stats HTML
    if stats["num_lines"] == 0:
        stats_html = "<p>No dialogue lines generated.</p>"
    else:
        time_start, time_end = stats["time_range"]
        ls = stats["length_stats"]
        ds = stats["duration_stats"]
        total_issues = sum(len(v) for v in issues.values())
        stats_html = f"""<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-value">{stats["num_lines"]}</div><div class="stat-label">Lines</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{stats["total_chars"]}</div><div class="stat-label">Characters</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{total_issues}</div><div class="stat-label">Issues</div>
  </div>
  <div class="stat-card">
    <div class="stat-value">{seconds_to_timestamp(time_start)} - {seconds_to_timestamp(time_end)}</div>
    <div class="stat-label">Time Range</div>
  </div>
</div>
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-label">Line Length (chars)</div>
    <div class="stat-detail">Min: {ls["min"]} | Max: {ls["max"]} | Mean: {ls["mean"]:.1f} | Median: {ls["median"]}</div>
  </div>
  <div class="stat-card">
    <div class="stat-label">Line Duration (seconds)</div>
    <div class="stat-detail">Min: {ds["min"]:.2f}s | Max: {ds["max"]:.2f}s | Mean: {ds["mean"]:.2f}s | Median: {ds["median"]:.2f}s</div>
  </div>
</div>"""

    # Resolve video path relative to the HTML output file
    video_src = None
    if video_path:
        vp = Path(video_path)
        if vp.is_file():
            try:
                video_src = os.path.relpath(vp, path.parent)
            except ValueError:
                # On Windows, relpath fails across drives
                video_src = str(vp.resolve())

    # Build table rows
    table_rows = []
    for idx, line in enumerate(lines):
        dur = line["end"] - line["start"]
        char_count = len(line["text"])
        row_issues = get_row_issues(idx)

        if row_issues:
            severity = min(row_issues, key=lambda x: _SEVERITY_ORDER.get(x[0], 99))[0]
            row_class = f"severity-{severity}"
            issue_tags = "".join(
                f'<span class="issue-tag tag-{sev}">{label}</span>'
                for sev, label in row_issues
            )
            # Data attributes for filtering
            data_attrs = " ".join(f'data-issue-{sev}="1"' for sev, _ in row_issues)
        else:
            row_class = ""
            issue_tags = ""
            data_attrs = ""

        escaped_text = (
            line["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )

        table_rows.append(
            f'<tr class="{row_class}" {data_attrs} '
            f'data-start="{line["start"]:.3f}" data-end="{line["end"]:.3f}" '
            f'data-text="{escaped_text}" '
            f'onclick="onRowClick(this)">'
            f"<td>{idx + 1}</td>"
            f"<td>{seconds_to_timestamp(line['start'])}</td>"
            f"<td>{seconds_to_timestamp(line['end'])}</td>"
            f"<td>{dur:.2f}s</td>"
            f"<td>{char_count}</td>"
            f"<td>{line['style']}</td>"
            f"<td>{escaped_text}</td>"
            f"</tr>"
        )
        if row_issues:
            table_rows.append(
                f'<tr class="detail-row" style="display:none">'
                f'<td colspan="7">{issue_tags}</td></tr>'
            )

    rows_html = "\n".join(table_rows)

    # Issue counts for filter buttons
    issue_counts = {
        "red": len(issues["zero_duration"]) + len(issues["inverted"]),
        "orange": len(issues["long_duration"]) + len(issues["overlaps"]),
        "yellow": len(issues["long_lines"]) + len(issues["short_lines"]),
        "blue": len(issues["large_gaps"]),
    }

    # Video player section (only if video file exists)
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
    <div id="now-text">Click a line to preview</div>
  </div>
</div>"""
        video_css = """
  #player-section { display: flex; gap: 16px; align-items: stretch;
                     padding: 8px 0; }
  #video-wrap { width: 420px; min-width: 200px; flex-shrink: 0;
                 resize: horizontal; overflow: hidden; }
  #video { width: 100%; background: #000; border-radius: 8px;
            display: block; }
  #now-playing { flex: 1; background: #16213e; border-radius: 8px;
                  padding: 10px 14px; border: 1px solid #2a3a5c;
                  align-self: stretch; display: flex; flex-direction: column; }
  #now-header { display: flex; justify-content: space-between;
                 margin-bottom: 6px; }
  #now-line-num { font-size: 0.75em; color: #4d94ff; font-weight: 600; }
  #now-time { font-size: 0.75em; color: #888; font-family: monospace; }
  #now-text { font-size: 1em; color: #fff; line-height: 1.5;
               background: #0d1a30; border: 1px solid #2a3a5c; border-radius: 6px;
               padding: 10px 12px; white-space: pre-wrap; word-break: break-word;
               flex: 1; overflow-y: auto; }
  th { top: 0; }"""
    else:
        video_html = ""
        video_css = ""

    html = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title or "Quality Report"}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
         background: #1a1a2e; color: #e0e0e0; padding: 20px; }}
  h1 {{ color: #fff; margin-bottom: 16px; }}
  .stats-grid {{ display: flex; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }}
  .stat-card {{ background: #16213e; border-radius: 8px; padding: 16px; flex: 1; min-width: 150px; }}
  .stat-value {{ font-size: 1.5em; font-weight: bold; color: #fff; }}
  .stat-label {{ font-size: 0.85em; color: #888; margin-top: 4px; }}
  .stat-detail {{ font-size: 0.9em; color: #ccc; margin-top: 8px; }}
  #sticky-top {{ position: sticky; top: 0; z-index: 10; background: #1a1a2e;
                 padding-bottom: 4px; }}
  .filters {{ margin: 8px 0; display: flex; gap: 8px; flex-wrap: wrap; }}
  .filter-btn {{ border: none; border-radius: 6px; padding: 8px 16px; cursor: pointer;
                 font-size: 0.85em; font-weight: 600; transition: opacity 0.2s; }}
  .filter-btn.inactive {{ opacity: 0.35; }}
  .btn-red {{ background: #ff4d4d; color: #fff; }}
  .btn-orange {{ background: #ff9933; color: #fff; }}
  .btn-yellow {{ background: #e6c300; color: #1a1a2e; }}
  .btn-blue {{ background: #4d94ff; color: #fff; }}
  .btn-all {{ background: #555; color: #fff; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 0.85em; }}
  th {{ background: #0f3460; color: #fff; padding: 10px 8px; text-align: left;
       position: sticky; top: 0; z-index: 2; }}
  td {{ padding: 8px; border-bottom: 1px solid #222; vertical-align: top; }}
  tr {{ cursor: pointer; transition: background 0.15s; }}
  tr:hover {{ background: #1e2d4a !important; }}
  tr.selected {{ outline: 2px solid #4d94ff; }}
  .severity-red {{ background: rgba(255,77,77,0.15); }}
  .severity-orange {{ background: rgba(255,153,51,0.12); }}
  .severity-yellow {{ background: rgba(230,195,0,0.10); }}
  .severity-blue {{ background: rgba(77,148,255,0.10); }}
  .detail-row {{ cursor: default; }}
  .detail-row:hover {{ background: inherit !important; }}
  .detail-row td {{ padding: 4px 8px 8px 32px; border-bottom: 2px solid #333; }}
  .issue-tag {{ display: inline-block; border-radius: 4px; padding: 2px 8px;
               margin-right: 6px; font-size: 0.8em; font-weight: 600; }}
  .tag-red {{ background: #ff4d4d; color: #fff; }}
  .tag-orange {{ background: #ff9933; color: #fff; }}
  .tag-yellow {{ background: #e6c300; color: #1a1a2e; }}
  .tag-blue {{ background: #4d94ff; color: #fff; }}
  .hidden-row {{ display: none !important; }}{video_css}
</style>
</head>
<body>
<h1>Quality Report{f" — {title}" if title else ""}</h1>
{stats_html}
<div id="sticky-top">
{video_html}
<div class="filters">
  <button class="filter-btn btn-all" onclick="filterAll()">All</button>
  <button class="filter-btn btn-red" data-filter="red" onclick="toggleFilter(this)">
    Critical ({issue_counts["red"]})</button>
  <button class="filter-btn btn-orange" data-filter="orange" onclick="toggleFilter(this)">
    Warning ({issue_counts["orange"]})</button>
  <button class="filter-btn btn-yellow" data-filter="yellow" onclick="toggleFilter(this)">
    Info ({issue_counts["yellow"]})</button>
  <button class="filter-btn btn-blue" data-filter="blue" onclick="toggleFilter(this)">
    Gaps ({issue_counts["blue"]})</button>
  <button class="filter-btn btn-all" onclick="filterIssuesOnly()">Issues Only</button>
</div>
</div>
<table>
<thead><tr>
  <th>#</th><th>Start</th><th>End</th><th>Duration</th>
  <th>Chars</th><th>Style</th><th>Text</th>
</tr></thead>
<tbody>
{rows_html}
</tbody>
</table>
<script>
const video = document.getElementById('video');
const nowLineNum = document.getElementById('now-line-num');
const nowTime = document.getElementById('now-time');
const nowText = document.getElementById('now-text');
let selectedRow = null;

function onRowClick(row) {{
  // Toggle detail row
  const next = row.nextElementSibling;
  if (next && next.classList.contains('detail-row')) {{
    next.style.display = next.style.display === 'none' ? '' : 'none';
  }}
  // Select line and seek video
  if (selectedRow) selectedRow.classList.remove('selected');
  row.classList.add('selected');
  selectedRow = row;
  const lineNum = row.cells[0].textContent;
  const text = row.getAttribute('data-text');
  const startTime = row.cells[1].textContent;
  const endTime = row.cells[2].textContent;
  if (nowLineNum) nowLineNum.textContent = 'Line #' + lineNum;
  if (nowTime) nowTime.textContent = startTime + ' \u2192 ' + endTime;
  if (nowText) nowText.textContent = text;
  if (video) {{
    const t = parseFloat(row.getAttribute('data-start'));
    video.currentTime = t;
    video.play();
  }}
}}
const activeFilters = new Set();
function applyFilters() {{
  const rows = document.querySelectorAll('tbody tr:not(.detail-row)');
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
    const next = row.nextElementSibling;
    if (next && next.classList.contains('detail-row')) {{
      if (!show) next.style.display = 'none';
    }}
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
function filterIssuesOnly() {{
  activeFilters.clear();
  ['red','orange','yellow','blue'].forEach(f => activeFilters.add(f));
  applyFilters();
}}
// Pin table headers just below the sticky top bar
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


def write_reports(
    lines: list[dict],
    ass_path: str,
    video_path: str | None = None,
    title: str | None = None,
):
    """Print quality report and write .log and .html files next to the ASS output."""
    print_quality_report(lines)
    report = analyze_quality(lines)
    output = Path(ass_path)
    log_path = output.with_suffix(".log")
    html_path = output.with_suffix(".html")
    write_quality_log(lines, report, str(log_path))
    write_quality_html(
        lines, report, str(html_path), video_path=video_path, title=title
    )
    print(f"  Log:  {log_path}")
    print(f"  HTML: {html_path}")
