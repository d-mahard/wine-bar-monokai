# VS Code Theme File Structure Guide

This document explains how VS Code allows separating color theme files based on the VS Code source code analysis.

## What You Can Separate:

### 1. **tokenColors** - Full External File Support ✓

You can reference an external file for token colors:

```json
{
  "tokenColors": "./token-colors.json"
}
```

or

```json
{
  "tokenColors": "./my-theme.tmTheme"
}
```

**Key Points:**
- The path is resolved **relative to your theme file's directory**
- Supports both `.json` and `.tmTheme` (TextMate) formats
- See: `src/vs/workbench/services/themes/common/colorThemeData.ts:773-781`

### 2. **include** Property - Multi-File Theme Support ✓

You can use `include` to split your theme across multiple files:

```json
{
  "include": "./base-colors.json",
  "colors": {
    "activityBar.activeBorder": "#0078D4"
  }
}
```

**This allows you to:**
- Create a base theme file with common definitions
- Extend it with specific overrides
- Chain multiple includes (included files can include others)
- Properties in the current file override those from included files

**Real-world example:** VS Code's `dark_modern.json` includes `dark_plus.json`

See: `src/vs/workbench/services/themes/common/colorThemeData.ts:750-751`

## What You Cannot Separate:

### **colors** Property - Must Be Inline ✗

The `colors` property **cannot reference external files**. It must be an inline object:

```json
{
  "colors": {
    "editor.background": "#1e1e1e"
  }
}
```

See: `src/vs/workbench/services/themes/common/colorThemeData.ts:758-771`

## Recommended Structure:

```
my-theme/
├── theme.json          (main file with colors + include)
├── base-colors.json    (included base colors)
└── token-colors.json   (referenced by tokenColors)
```

### Example: theme.json

```json
{
  "$schema": "vscode://schemas/color-theme",
  "name": "My Theme",
  "include": "./base-colors.json",
  "colors": {
    "editor.background": "#1e1e1e",
    "editor.foreground": "#d4d4d4"
  },
  "tokenColors": "./token-colors.json"
}
```

### Example: base-colors.json

```json
{
  "colors": {
    "activityBar.background": "#2c2c2c",
    "statusBar.background": "#007acc"
  }
}
```

### Example: token-colors.json

```json
[
  {
    "scope": "comment",
    "settings": {
      "foreground": "#6A9955"
    }
  },
  {
    "scope": "keyword",
    "settings": {
      "foreground": "#569CD6"
    }
  }
]
```

## How Theme Loading Works:

1. VS Code reads your main theme JSON file
2. If `include` is present, it recursively loads the included file first
3. If `tokenColors` is a string, it loads that external file
4. Properties in the current file override those from included files
5. All `tokenColors` arrays are merged (not overridden)

## Source Code References:

- Main loading logic: `src/vs/workbench/services/themes/common/colorThemeData.ts`
- Schema definition: `src/vs/workbench/services/themes/common/colorThemeSchema.ts`
- Example themes: `extensions/theme-defaults/themes/`
