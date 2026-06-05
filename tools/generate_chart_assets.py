#!/usr/bin/env python3
"""Generate text-based SVG chart assets referenced by the pandas manual.

The manual links to these SVG files directly. SVG keeps pull-request diffs
reviewable while still providing rendered chart images in Markdown viewers.
The script uses only the Python standard library.
"""

from __future__ import annotations

import html
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "pandas_manual_assets"
WIDTH = 900
HEIGHT = 560

COLORS = {
    "blue": "#2563eb",
    "orange": "#ea580c",
    "green": "#16a34a",
    "purple": "#7c3aed",
    "red": "#dc2626",
    "teal": "#0d9488",
    "grid": "#e2e8f0",
    "axis": "#4b5563",
    "text": "#232323",
    "muted": "#9ca3af",
    "light_blue": "#93c5fd",
    "light_orange": "#fdba74",
}



class SVG:
    def __init__(self, title: str):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
            f"<title>{html.escape(title)}</title>",
            f"<desc>{html.escape(title)} chart for the pandas manual.</desc>",
            '<rect width="100%" height="100%" fill="white"/>',
            '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#232323}.title{font-size:30px;font-weight:700}.label{font-size:17px}.small{font-size:14px}.legend{font-size:16px}</style>',
            f'<text class="title" x="{WIDTH / 2}" y="48" text-anchor="middle">{html.escape(title)}</text>',
        ]

    def add(self, markup: str) -> None:
        self.parts.append(markup)

    def text(self, x: float, y: float, value: str, cls: str = "label", anchor: str = "start", color: str | None = None) -> None:
        fill = f' fill="{color}"' if color else ""
        self.add(f'<text class="{cls}" x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}"{fill}>{html.escape(value)}</text>')

    def save(self, filename: str) -> None:
        self.parts.append("</svg>")
        (ASSET_DIR / filename).write_text("\n".join(self.parts) + "\n", encoding="utf-8")


def chart_frame(svg: SVG) -> tuple[int, int, int, int]:
    left, top, right, bottom = 90, 90, 840, 470
    for i in range(6):
        y = bottom - i * (bottom - top) / 5
        svg.add(f'<line x1="{left}" y1="{y:.1f}" x2="{right}" y2="{y:.1f}" stroke="{COLORS["grid"]}"/>')
    svg.add(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
    svg.add(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
    return left, top, right, bottom


def y_scale(value: float, top: float, bottom: float, min_value: float, max_value: float) -> float:
    return bottom - (value - min_value) / (max_value - min_value) * (bottom - top)


def points(values: list[float], area: tuple[int, int, int, int], min_value: float, max_value: float) -> list[tuple[float, float]]:
    left, top, right, bottom = area
    return [
        (left + i * (right - left) / max(1, len(values) - 1), y_scale(value, top, bottom, min_value, max_value))
        for i, value in enumerate(values)
    ]


def line_path(pts: list[tuple[float, float]]) -> str:
    first, *rest = pts
    return "M " + f"{first[0]:.1f} {first[1]:.1f} " + " ".join(f"L {x:.1f} {y:.1f}" for x, y in rest)


def legend(svg: SVG, items: list[tuple[str, str]], x: int = 610, y: int = 100) -> None:
    for i, (label, color) in enumerate(items):
        yy = y + i * 30
        svg.add(f'<rect x="{x}" y="{yy}" width="24" height="14" fill="{color}"/>')
        svg.text(x + 34, yy + 14, label, "legend")


def save_mean_median_mode() -> None:
    svg = SVG("Mean, Median, and Mode")
    left, top, right, bottom = chart_frame(svg)
    values = [2, 3, 3, 4, 4, 4, 5, 6, 7, 20]
    bins = list(range(2, 22, 2))
    counts = [sum(1 for value in values if start <= value < start + 2) for start in bins]
    for i, count in enumerate(counts):
        x = left + i * (right - left) / len(counts) + 5
        width = (right - left) / len(counts) - 10
        y = y_scale(count, top, bottom, 0, max(counts))
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["blue"]}"/>')
    for value, label, color, offset in [
        (sum(values) / len(values), "Mean", COLORS["red"], 0),
        (4, "Median", COLORS["green"], 28),
        (4, "Mode", COLORS["purple"], 56),
    ]:
        x = left + (value - 2) / 20 * (right - left)
        svg.add(f'<line x1="{x:.1f}" y1="{top}" x2="{x:.1f}" y2="{bottom}" stroke="{color}" stroke-width="4"/>')
        svg.text(x + 8, top + 20 + offset, label, "small", color=color)
    svg.text(112, 508, "Outlier pulls the mean to the right", "small")
    svg.save("stats_mean_median_mode.svg")


def save_histogram() -> None:
    svg = SVG("Histogram Distribution")
    left, top, right, bottom = chart_frame(svg)
    counts = [1, 3, 7, 12, 16, 14, 10, 6, 3, 1]
    for i, count in enumerate(counts):
        x = left + i * (right - left) / len(counts) + 5
        width = (right - left) / len(counts) - 10
        y = y_scale(count, top, bottom, 0, max(counts))
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["teal"]}"/>')
    svg.text(450, 508, "Score ranges", "small", "middle")
    svg.save("plot_histogram_distribution.svg")


def save_boxplot() -> None:
    svg = SVG("Box Plot Quartiles and Outliers")
    chart_frame(svg)
    for x, low, q1, median, q3, whisker_low, outliers, color, label in [
        (240, 130, 205, 310, 380, 430, [96, 452], COLORS["blue"], "Group A"),
        (470, 180, 250, 335, 420, 450, [142], COLORS["orange"], "Group B"),
        (700, 155, 230, 300, 390, 438, [116], COLORS["green"], "Group C"),
    ]:
        svg.add(f'<line x1="{x}" y1="{low}" x2="{x}" y2="{q1}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
        svg.add(f'<line x1="{x}" y1="{q3}" x2="{x}" y2="{whisker_low}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
        svg.add(f'<line x1="{x - 34}" y1="{low}" x2="{x + 34}" y2="{low}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
        svg.add(f'<line x1="{x - 34}" y1="{whisker_low}" x2="{x + 34}" y2="{whisker_low}" stroke="{COLORS["axis"]}" stroke-width="3"/>')
        svg.add(f'<rect x="{x - 70}" y="{q1}" width="140" height="{q3 - q1}" fill="{color}" stroke="#232323"/>')
        svg.add(f'<line x1="{x - 70}" y1="{median}" x2="{x + 70}" y2="{median}" stroke="white" stroke-width="4"/>')
        for y in outliers:
            svg.add(f'<circle cx="{x}" cy="{y}" r="8" fill="{COLORS["red"]}"/>')
        svg.text(x, 508, label, "small", "middle")
    svg.save("plot_boxplot_quartiles_outliers.svg")


def save_heatmap() -> None:
    svg = SVG("Correlation Heatmap")
    labels = ["Revenue", "Cost", "Claims", "Profit"]
    vals = [[1.00, 0.94, 0.82, 0.88], [0.94, 1.00, 0.79, 0.62], [0.82, 0.79, 1.00, 0.55], [0.88, 0.62, 0.55, 1.00]]
    x0, y0, size = 250, 115, 92
    for i, row in enumerate(vals):
        svg.text(90, y0 + i * size + 52, labels[i], "small")
        svg.text(x0 + i * size + size / 2, 96, labels[i], "small", "middle")
        for j, value in enumerate(row):
            shade = round(255 - value * 140)
            color = f"rgb({shade},{shade + 10},255)"
            svg.add(f'<rect x="{x0 + j * size}" y="{y0 + i * size}" width="88" height="88" fill="{color}"/>')
            svg.text(x0 + j * size + 44, y0 + i * size + 52, f"{value:.2f}", "small", "middle")
    svg.save("plot_correlation_heatmap.svg")


def save_line_plot() -> None:
    svg = SVG("Revenue and Cost Over Time")
    area = chart_frame(svg)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    series = [("Revenue", [12500, 13200, 15100, 14800, 17400, 18900], COLORS["blue"]), ("Cost", [8000, 8200, 9000, 9100, 10300, 11100], COLORS["orange"])]
    for _, values, color in series:
        pts = points(values, area, 0, 20000)
        svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{color}" stroke-width="4"/>')
        for x, y in pts:
            svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{color}"/>')
    left, _, right, bottom = area
    for i, month in enumerate(months):
        svg.text(left + i * (right - left) / 5, bottom + 28, month, "small", "middle")
    legend(svg, [(name, color) for name, _, color in series])
    svg.save("plot_line_over_time.svg")


def save_bar_plot() -> None:
    svg = SVG("Profit by Month")
    left, top, right, bottom = chart_frame(svg)
    profits = [4500, 5000, 6100, 5700, 7100, 7900]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for i, profit in enumerate(profits):
        x = left + i * (right - left) / len(profits) + 12
        width = (right - left) / len(profits) - 24
        y = y_scale(profit, top, bottom, 0, 8500)
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["green"]}"/>')
        svg.text(x + width / 2, bottom + 28, months[i], "small", "middle")
    svg.save("plot_bar_profit.svg")


def save_scatter() -> None:
    svg = SVG("Claims vs Profit")
    left, top, right, bottom = chart_frame(svg)
    claims = [80, 85, 92, 89, 101, 108, 113, 118, 120]
    profits = [4500, 5000, 6100, 5700, 7100, 7900, 8200, 9100, 9500]
    svg.add(f'<line x1="{left + 20}" y1="{bottom - 30}" x2="{right - 35}" y2="{top + 35}" stroke="{COLORS["muted"]}" stroke-width="2"/>')
    for claim, profit in zip(claims, profits):
        x = left + (claim - 75) / 50 * (right - left)
        y = y_scale(profit, top, bottom, 4000, 10000)
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{COLORS["purple"]}"/>')
    svg.text(450, 508, "Claims", "small", "middle")
    svg.save("plot_scatter_relationship.svg")


def save_area_plot() -> None:
    svg = SVG("Revenue and Cost Volume")
    area = chart_frame(svg)
    left, _, _, bottom = area
    for name, values, stroke, fill in [
        ("Revenue", [12500, 13200, 15100, 14800, 17400, 18900], COLORS["blue"], COLORS["light_blue"]),
        ("Cost", [8000, 8200, 9000, 9100, 10300, 11100], COLORS["orange"], COLORS["light_orange"]),
    ]:
        pts = points(values, area, 0, 20000)
        area_path = line_path(pts) + f" L {pts[-1][0]:.1f} {bottom} L {left} {bottom} Z"
        svg.add(f'<path d="{area_path}" fill="{fill}" fill-opacity="0.55" stroke="none"/>')
        svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{stroke}" stroke-width="4"/>')
    legend(svg, [("Revenue", COLORS["blue"]), ("Cost", COLORS["orange"])])
    svg.save("plot_area_volume.svg")


def save_pie() -> None:
    svg = SVG("Share of Work by Method")
    cx, cy, radius = 450, 290, 170
    parts = [("Fax", 42, COLORS["blue"]), ("Website", 28, COLORS["orange"]), ("Mail", 18, COLORS["green"]), ("Projects", 12, COLORS["purple"])]
    start = -90.0
    for label, value, color in parts:
        end = start + value / 100 * 360
        large_arc = 1 if end - start > 180 else 0
        x1, y1 = cx + radius * math.cos(math.radians(start)), cy + radius * math.sin(math.radians(start))
        x2, y2 = cx + radius * math.cos(math.radians(end)), cy + radius * math.sin(math.radians(end))
        svg.add(f'<path d="M {cx} {cy} L {x1:.1f} {y1:.1f} A {radius} {radius} 0 {large_arc} 1 {x2:.1f} {y2:.1f} Z" fill="{color}" stroke="white" stroke-width="2"/>')
        mid = math.radians((start + end) / 2)
        svg.text(cx + math.cos(mid) * 225, cy + math.sin(mid) * 225, f"{label} {value}%", "small", "middle")
        start = end
    svg.add(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#232323"/>')
    svg.save("plot_pie_share.svg")


def main() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    save_mean_median_mode()
    save_histogram()
    save_boxplot()
    save_heatmap()
    save_line_plot()
    save_bar_plot()
    save_scatter()
    save_area_plot()
    save_pie()


if __name__ == "__main__":
    main()
