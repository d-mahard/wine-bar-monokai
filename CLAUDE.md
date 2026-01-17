# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Wine Bar Monokai is a Visual Studio Code color theme extension. It's a dark theme with a brown-maroon color palette inspired by an old wooden bar, combining the classic Monokai syntax highlighter with carefully crafted workbench colors. The theme is optimized for TypeScript and C#, with extended support for GitLens, ErrorLens, Copilot, and GitHub PR extensions.

## Key Architecture

### Theme Structure

The entire theme is defined in a single JSON file at `themes/Wine Bar Monokai-color-theme.json`. This file contains two main sections:

1. **Workbench colors** (`colors` object): Defines UI element colors for the entire VS Code interface (activity bar, editor, terminal, etc.)
2. **Syntax highlighting** (`tokenColors` array): Defines text colors and styles based on TextMate scopes

### Core Color Philosophy

- The design principle is to create clear visual separation between the working area (editor, terminal) and functional elements (sidebar, activity bar).
- The chosen color should help with ergonomics (good contrast, clear difference between clickable area, editable area, etc)

## Development Commands

### Testing the Theme

Press `F5` to launch the Extension Development Host window with the theme loaded. Changes to `themes/Wine Bar Monokai-color-theme.json` are automatically applied to this window.

To inspect token scopes in the test window:
1. Open a file with syntax highlighting
2. Run `Developer: Inspect Editor Tokens and Scopes` from the Command Palette (`Ctrl+Shift+P`)

### Testing ANSI Terminal Colors

Run `python tools/ansi_colors.py` in the terminal to display all ANSI color combinations. Note: Set `terminal.integrated.minimumContrastRatio` to `1` in VS Code settings to see actual colors without automatic contrast adjustments.

### Viewing Sample Files

Sample files for testing syntax highlighting are in `sample_text/`:
- `sample.ts` - TypeScript
- `sample.cs` - C#
- `sample.js` - JavaScript
- `sample.py` - Python
- `sample.md` - Markdown

## Editing Color Values

### Finding Color Names

There's no built-in way to identify workbench element names by clicking. Reference the official documentation:
- [Theme Color Reference](https://code.visualstudio.com/api/references/theme-color)
- [Workbench Colors Guide](https://code.visualstudio.com/api/extension-guides/color-theme#workbench-colors)
- [Syntax Highlight Guide](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide)
- [Semantic Highlight Guide](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide)

### Color Format

Colors use hex format with optional alpha channel:
- `#RRGGBB` - Solid color
- `#RRGGBBAA` - Color with transparency (00 = fully transparent, ff = fully opaque)

When modifying colors, maintain consistency with the brown-maroon theme palette and ensure sufficient contrast for readability.

## Publishing

The extension is published to the VS Code Marketplace under publisher `d-mahard`. Package version is managed in `package.json`.

