"""
Color Palette Analyzer for Wine Bar Monokai Theme

Analyzes the workbench colors in the theme file and outputs a JSON file
showing the color palette grouped by similarity.

Usage:
    python tools/analyze_colors.py
    python tools/analyze_colors.py --output custom_output.json
"""

import json
import re
import colorsys
import argparse
from pathlib import Path
from collections import defaultdict


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    # Take only first 6 chars (ignore alpha)
    hex_color = hex_color[:6]
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    """Convert RGB to HSL. Returns (hue 0-360, saturation 0-1, lightness 0-1)."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return (h * 360, s, l)


def get_color_group(hex_color: str) -> str:
    """Determine which color group a hex color belongs to based on HSL."""
    rgb = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(*rgb)

    # Handle neutrals (low saturation or very dark/light)
    if s < 0.1 or l < 0.05 or l > 0.95:
        if l < 0.15:
            return "blacks"
        elif l > 0.85:
            return "whites"
        else:
            return "grays"

    # Handle very dark colors with low saturation
    if l < 0.2 and s < 0.3:
        return "blacks"

    # Browns: dark to medium oranges/reds with low to moderate saturation
    # Hue range: 0-45 (red to orange), lightness < 0.45, saturation < 0.7
    if (h < 45 or h >= 345) and l < 0.45 and s < 0.7:
        return "browns"

    # Group by hue ranges
    if h < 15 or h >= 345:
        return "reds"
    elif h < 45:
        return "oranges"
    elif h < 70:
        return "yellows"
    elif h < 150:
        return "greens"
    elif h < 195:
        return "cyans"
    elif h < 260:
        return "blues"
    elif h < 290:
        return "purples"
    elif h < 345:
        return "magentas"

    return "other"


def parse_theme_colors(theme_path: Path) -> dict[str, str]:
    """
    Parse theme file and extract all color definitions from the colors object.
    Includes both active and commented-out color definitions.
    """
    with open(theme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    colors = {}

    # Find the colors object (between "colors": { and the closing })
    colors_match = re.search(r'"colors"\s*:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content, re.DOTALL)
    if not colors_match:
        raise ValueError("Could not find 'colors' object in theme file")

    colors_content = colors_match.group(1)

    # Pattern to match color definitions (both active and commented)
    # Handles: "key": "#value" and //"key": "#value"
    pattern = r'(?://\s*)?["\']([^"\']+)["\']\s*:\s*["\']([^"\']+)["\']'

    for match in re.finditer(pattern, colors_content):
        key = match.group(1)
        value = match.group(2)
        # Only include hex color values
        if value.startswith('#') and len(value) in (7, 9):  # #RRGGBB or #RRGGBBAA
            colors[key] = value

    return colors


def extract_base_and_alpha(hex_color: str) -> tuple[str, str]:
    """Extract base color (6 digits) and alpha from hex color."""
    hex_color = hex_color.lstrip('#').upper()
    if len(hex_color) == 8:
        return f"#{hex_color[:6]}", hex_color[6:]
    else:
        return f"#{hex_color}", "FF"


def analyze_colors(colors: dict[str, str]) -> dict:
    """Analyze colors and group by similarity."""

    # Group by base color
    base_color_usage = defaultdict(lambda: defaultdict(list))

    for element, hex_color in colors.items():
        base, alpha = extract_base_and_alpha(hex_color)
        base_color_usage[base][alpha].append(element)

    # Organize by color groups
    color_groups = defaultdict(list)

    for base_color, alpha_usage in base_color_usage.items():
        group = get_color_group(base_color)

        variations = []
        for alpha, elements in sorted(alpha_usage.items(), key=lambda x: x[0], reverse=True):
            if alpha == "FF":
                hex_with_alpha = base_color
            else:
                hex_with_alpha = f"{base_color}{alpha}"
            variations.append({
                "hex": hex_with_alpha.lower(),
                "alpha": alpha.lower(),
                "usage": sorted(elements)
            })

        # Get HSL for sorting
        rgb = hex_to_rgb(base_color)
        h, s, l = rgb_to_hsl(*rgb)

        color_groups[group].append({
            "base_color": base_color.lower(),
            "hsl": {"h": round(h, 1), "s": round(s, 3), "l": round(l, 3)},
            "variations": variations,
            "_sort_key": (h, s, l)  # For sorting within group
        })

    # Sort colors within each group by hue, then saturation, then lightness
    for group in color_groups:
        color_groups[group].sort(key=lambda x: x["_sort_key"])
        # Remove sort key from output
        for color in color_groups[group]:
            del color["_sort_key"]

    # Calculate summary
    total_entries = len(colors)
    total_unique_base = len(base_color_usage)
    group_counts = {group: len(colors_list) for group, colors_list in color_groups.items()}

    # Order groups logically (browns first as core theme color)
    group_order = ["browns", "reds", "oranges", "yellows", "greens", "cyans", "blues", "purples", "magentas", "whites", "grays", "blacks", "other"]
    ordered_groups = {}
    for group in group_order:
        if group in color_groups:
            ordered_groups[group] = color_groups[group]

    return {
        "summary": {
            "total_color_entries": total_entries,
            "total_unique_base_colors": total_unique_base,
            "color_groups": {g: group_counts[g] for g in group_order if g in group_counts}
        },
        "color_groups": ordered_groups
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze color palette in Wine Bar Monokai theme")
    parser.add_argument(
        "--output", "-o",
        default="tools/color_analysis.json",
        help="Output JSON file path (default: tools/color_analysis.json)"
    )
    parser.add_argument(
        "--theme", "-t",
        default="themes/Wine Bar Monokai-color-theme.json",
        help="Theme file path (default: themes/Wine Bar Monokai-color-theme.json)"
    )
    args = parser.parse_args()

    # Resolve paths relative to script location
    script_dir = Path(__file__).parent.parent
    theme_path = script_dir / args.theme
    output_path = script_dir / args.output

    print(f"Analyzing theme: {theme_path}")

    # Parse and analyze
    colors = parse_theme_colors(theme_path)
    print(f"Found {len(colors)} color definitions")

    analysis = analyze_colors(colors)

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2)

    print(f"Analysis written to: {output_path}")
    print(f"\nSummary:")
    print(f"  Total color entries: {analysis['summary']['total_color_entries']}")
    print(f"  Unique base colors: {analysis['summary']['total_unique_base_colors']}")
    print(f"  Color groups: {analysis['summary']['color_groups']}")


if __name__ == "__main__":
    main()
