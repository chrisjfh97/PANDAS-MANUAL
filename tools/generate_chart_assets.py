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


def save_horizontal_bar_plot() -> None:
    svg = SVG("Horizontal Profit by Month")
    left, top, right, bottom = chart_frame(svg)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    profits = [4500, 5000, 6100, 5700, 7100, 7900]
    max_profit = 8500
    bar_h = (bottom - top) / len(profits) - 12
    for i, (month, profit) in enumerate(zip(months, profits)):
        y = top + i * (bottom - top) / len(profits) + 8
        width = (profit / max_profit) * (right - left)
        svg.add(f'<rect x="{left}" y="{y:.1f}" width="{width:.1f}" height="{bar_h:.1f}" fill="{COLORS["green"]}"/>')
        svg.text(left - 18, y + bar_h / 2 + 5, month, "small", "end")
        svg.text(left + width + 8, y + bar_h / 2 + 5, f"${profit:,}", "small")
    svg.text(450, 508, "Profit", "small", "middle")
    svg.save("plot_horizontal_bar_profit.svg")


def save_density_plot() -> None:
    svg = SVG("Profit Density")
    area = chart_frame(svg)
    left, top, right, bottom = area
    pts = []
    for i in range(80):
        x = left + i * (right - left) / 79
        t = -3 + i * 6 / 79
        yval = math.exp(-0.5 * t * t)
        pts.append((x, bottom - yval * (bottom - top) * 0.85))
    fill_path = line_path(pts) + f" L {right} {bottom} L {left} {bottom} Z"
    svg.add(f'<path d="{fill_path}" fill="{COLORS["light_blue"]}" fill-opacity="0.7"/>')
    svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{COLORS["blue"]}" stroke-width="4"/>')
    svg.text(450, 508, "Profit values", "small", "middle")
    svg.save("plot_density_profit.svg")


def save_reference_annotation_plot() -> None:
    svg = SVG("Profit Compared with Average")
    left, top, right, bottom = chart_frame(svg)
    profits = [4500, 5000, 6100, 5700, 7100, 7900]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    avg = sum(profits) / len(profits)
    avg_y = y_scale(avg, top, bottom, 0, 8500)
    svg.add(f'<line x1="{left}" y1="{avg_y:.1f}" x2="{right}" y2="{avg_y:.1f}" stroke="{COLORS["red"]}" stroke-width="4" stroke-dasharray="10 8"/>')
    svg.text(right - 10, avg_y - 10, "Average", "small", "end", COLORS["red"])
    for i, profit in enumerate(profits):
        x = left + i * (right - left) / len(profits) + 12
        width = (right - left) / len(profits) - 24
        y = y_scale(profit, top, bottom, 0, 8500)
        color = COLORS["orange"] if profit == max(profits) else COLORS["green"]
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{color}"/>')
        svg.text(x + width / 2, bottom + 28, months[i], "small", "middle")
    svg.add(f'<line x1="715" y1="135" x2="785" y2="112" stroke="{COLORS["axis"]}" stroke-width="3" marker-end="url(#arrow)"/>')
    svg.text(596, 140, "Highest profit", "small")
    svg.save("plot_reference_annotation.svg")


def save_formatted_revenue_plot() -> None:
    svg = SVG("Revenue by Month with Dollar Labels")
    area = chart_frame(svg)
    values = [12500, 13200, 15100, 14800, 17400, 18900]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    pts = points(values, area, 0, 20000)
    svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{COLORS["blue"]}" stroke-width="4"/>')
    for (x, y), value in zip(pts, values):
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{COLORS["blue"]}"/>')
        svg.text(x, y - 12, f"${value/1000:.1f}k", "small", "middle")
    left, _, right, bottom = area
    for i, month in enumerate(months):
        svg.text(left + i * (right - left) / 5, bottom + 28, month, "small", "middle")
    svg.save("plot_formatted_revenue.svg")


def save_grouped_summary_plot() -> None:
    svg = SVG("Total Profit by Month")
    # Create a grouped-summary asset with labels emphasizing summarized data.
    left, top, right, bottom = chart_frame(svg)
    profits = [4500, 5000, 6100, 5700, 7100, 7900]
    orders = [40, 45, 50, 48, 56, 61]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for i, (profit, order_count) in enumerate(zip(profits, orders)):
        x = left + i * (right - left) / len(profits) + 12
        width = (right - left) / len(profits) - 24
        y = y_scale(profit, top, bottom, 0, 8500)
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["teal"]}"/>')
        svg.text(x + width / 2, y - 8, f"{order_count} orders", "small", "middle")
        svg.text(x + width / 2, bottom + 28, months[i], "small", "middle")
    svg.save("plot_grouped_summary_profit.svg")


def save_small_multiples_plot() -> None:
    svg = SVG("Small Multiples by Region")
    panels = [(80, 110, 410, 450, "East", [40, 45, 50, 48]), (500, 110, 830, 450, "West", [30, 42, 44, 52])]
    months = ["Jan", "Feb", "Mar", "Apr"]
    for left, top, right, bottom, region, vals in panels:
        svg.add(f'<rect x="{left}" y="{top}" width="{right-left}" height="{bottom-top}" fill="none" stroke="{COLORS["grid"]}"/>')
        svg.add(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
        svg.add(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{COLORS["axis"]}" stroke-width="2"/>')
        area = (left, top, right, bottom)
        pts = points(vals, area, 0, 60)
        svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{COLORS["purple"]}" stroke-width="4"/>')
        for x, y in pts:
            svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{COLORS["purple"]}"/>')
        svg.text((left+right)/2, top-20, region, "label", "middle")
        for i, month in enumerate(months):
            svg.text(left + i * (right - left) / 3, bottom+28, month, "small", "middle")
    svg.save("plot_small_multiples_regions.svg")


def save_sorted_bars_plot() -> None:
    svg = SVG("Sorted Customer Actual Amount")
    left, top, right, bottom = chart_frame(svg)
    data = [("Online", 950), ("South LLC", 1800), ("North Co", 2200), ("West Shop", 3400)]
    max_value = 3600
    bar_h = (bottom - top) / len(data) - 18
    for i, (customer, value) in enumerate(data):
        y = top + i * (bottom - top) / len(data) + 10
        width = value / max_value * (right - left)
        color = COLORS["orange"] if value == max(v for _, v in data) else COLORS["blue"]
        svg.add(f'<rect x="{left}" y="{y:.1f}" width="{width:.1f}" height="{bar_h:.1f}" fill="{color}"/>')
        svg.text(left - 16, y + bar_h / 2 + 5, customer, "small", "end")
        svg.text(left + width + 8, y + bar_h / 2 + 5, f"${value:,}", "small")
    svg.save("plot_sorted_horizontal_bars.svg")


def save_stacked_percent_plot() -> None:
    svg = SVG("Order Status Mix by Region")
    left, top, right, bottom = chart_frame(svg)
    regions = ["East", "West", "South"]
    rows = [(90, 10, 5), (50, 25, 10), (40, 5, 5)]
    colors = [COLORS["green"], COLORS["orange"], COLORS["purple"]]
    labels = ["On Time", "Late", "Review"]
    bar_w = 120
    for i, (region, row) in enumerate(zip(regions, rows)):
        x = left + 120 + i * 210
        y_cursor = bottom
        total = sum(row)
        for val, color in zip(row, colors):
            h = val / total * (bottom - top)
            y_cursor -= h
            svg.add(f'<rect x="{x}" y="{y_cursor:.1f}" width="{bar_w}" height="{h:.1f}" fill="{color}" stroke="white"/>')
        svg.text(x + bar_w / 2, bottom + 28, region, "small", "middle")
    legend(svg, list(zip(labels, colors)), 650, 105)
    svg.text(50, 100, "100%", "small")
    svg.text(62, 470, "0%", "small")
    svg.save("plot_stacked_percent_status.svg")


def save_pareto_plot() -> None:
    svg = SVG("Pareto Chart of Issue Types")
    left, top, right, bottom = chart_frame(svg)
    labels = ["Missing", "Price", "Late", "Duplicate", "Other"]
    counts = [42, 30, 18, 7, 5]
    total = sum(counts)
    cumulative = []
    running = 0
    for c in counts:
        running += c
        cumulative.append(running / total)
    for i, count in enumerate(counts):
        x = left + i * (right - left) / len(counts) + 18
        width = (right - left) / len(counts) - 36
        y = y_scale(count, top, bottom, 0, 45)
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["blue"]}"/>')
        svg.text(x + width / 2, bottom + 28, labels[i], "small", "middle")
    pts = [(left + i * (right - left) / (len(counts) - 1), y_scale(p, top, bottom, 0, 1)) for i, p in enumerate(cumulative)]
    svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{COLORS["orange"]}" stroke-width="4"/>')
    for x, y in pts:
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{COLORS["orange"]}"/>')
    svg.text(800, 105, "Cumulative %", "small", "end", COLORS["orange"])
    svg.save("plot_pareto_issues.svg")


def save_before_after_plot() -> None:
    svg = SVG("Before-and-After Process Comparison")
    left, top, right, bottom = chart_frame(svg)
    data = [("Avg Days", 8.5, 5.2), ("Late Orders", 32, 18), ("Manual Reviews", 45, 29)]
    group_w = (right - left) / len(data)
    for i, (label, before, after) in enumerate(data):
        x0 = left + i * group_w + 30
        for j, (value, color) in enumerate([(before, COLORS["muted"]), (after, COLORS["green"])]):
            x = x0 + j * 50
            y = y_scale(value, top, bottom, 0, 50)
            svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="42" height="{bottom - y:.1f}" fill="{color}"/>')
        svg.text(x0 + 46, bottom + 28, label, "small", "middle")
    legend(svg, [("Before", COLORS["muted"]), ("After", COLORS["green"])])
    svg.save("plot_before_after_comparison.svg")


def save_dual_axis_plot() -> None:
    svg = SVG("Revenue and Orders by Month")
    left, top, right, bottom = chart_frame(svg)
    revenue = [12500, 13200, 15100, 14800, 17400, 18900]
    orders = [40, 45, 50, 48, 56, 61]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for i, val in enumerate(revenue):
        x = left + i * (right - left)/len(revenue) + 12
        width = (right - left)/len(revenue) - 24
        y = y_scale(val, top, bottom, 0, 20000)
        svg.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{bottom - y:.1f}" fill="{COLORS["light_blue"]}"/>')
        svg.text(x + width / 2, bottom+28, months[i], "small", "middle")
    pts = points(orders, (left, top, right, bottom), 0, 70)
    svg.add(f'<path d="{line_path(pts)}" fill="none" stroke="{COLORS["orange"]}" stroke-width="4"/>')
    for x, y in pts:
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{COLORS["orange"]}"/>')
    svg.text(100, 82, "Left axis: revenue", "small", color=COLORS["blue"])
    svg.text(730, 82, "Right axis: orders", "small", color=COLORS["orange"])
    svg.save("plot_dual_axis_revenue_orders.svg")


def save_missing_values_plot() -> None:
    svg = SVG("Monthly Value with Missing March Data")
    area = chart_frame(svg)
    months = ["Jan", "Feb", "Mar", "Apr", "May"]
    vals = [100, 120, None, 150, 160]
    left, top, right, bottom = area
    pts = []
    for i, val in enumerate(vals):
        x = left + i * (right - left)/(len(vals)-1)
        if val is None:
            svg.add(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{bottom}" stroke="{COLORS["red"]}" stroke-width="3" stroke-dasharray="8 8"/>')
            svg.text(x, top + 24, "Missing", "small", "middle", COLORS["red"])
            pts.append(None)
        else:
            pts.append((x, y_scale(val, top, bottom, 80, 170)))
            svg.add(f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="7" fill="{COLORS["blue"]}"/>')
        svg.text(x, bottom + 28, months[i], "small", "middle")
    for a,b in zip(pts, pts[1:]):
        if a is not None and b is not None:
            svg.add(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{COLORS["blue"]}" stroke-width="4"/>')
    svg.save("plot_missing_values_gap.svg")


def save_over_budget_plot() -> None:
    svg = SVG("Total Over-Budget Amount by Customer")
    left, top, right, bottom = chart_frame(svg)
    data = [("Online", 0), ("North Co", 150), ("West Shop", 650)]
    max_value = 700
    bar_h = (bottom - top) / len(data) - 20
    for i, (customer, value) in enumerate(data):
        y = top + i * (bottom - top) / len(data) + 12
        width = value / max_value * (right - left)
        color = COLORS["red"] if value == max(v for _, v in data) else COLORS["orange"]
        svg.add(f'<rect x="{left}" y="{y:.1f}" width="{width:.1f}" height="{bar_h:.1f}" fill="{color}"/>')
        svg.text(left - 16, y + bar_h / 2 + 5, customer, "small", "end")
        svg.text(left + max(width, 4) + 8, y + bar_h / 2 + 5, f"${value:,}", "small")
    svg.save("plot_over_budget_customer.svg")

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
    save_horizontal_bar_plot()
    save_density_plot()
    save_reference_annotation_plot()
    save_formatted_revenue_plot()
    save_grouped_summary_plot()
    save_small_multiples_plot()
    save_sorted_bars_plot()
    save_stacked_percent_plot()
    save_pareto_plot()
    save_before_after_plot()
    save_dual_axis_plot()
    save_missing_values_plot()
    save_over_budget_plot()


if __name__ == "__main__":
    main()
