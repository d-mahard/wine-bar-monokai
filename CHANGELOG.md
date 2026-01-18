# Change Log

All notable changes to the "wine-bar-monokai" extension will be documented in this file.

This follows the [Keep a Changelog](http://keepachangelog.com/) structure recommendation.

## [v0.1.11] - 2026-01-18

### Fixed

- broken file structure

## [v0.1.10] - 2024-12-30

### Changed

- extract token colors to a separate file
- colors of notification center, to match with sidebar section style

### Added

- Color palette analyzer tool (`tools/analyze_colors.py`) for analyzing theme colors grouped by similarity
- colors related to debugging
- colors related to diff editor
- color of action-bar tool background

### Fixed

- color of git commit placeholder 

## [v0.1.9] - 2024-06-12

### Changed

- fix color for diff editor, to help more focus on the changes. The maroon was a bit distracting as it is close to red. 

## [v0.1.8] - 2024-05-09

### Changed

- color for diff editor and code lens

## [v0.1.7] - 2024-04-05

### Changed

- color for terminal sticky scroll, sidebar title, and some color related to editor/group borders

## [v0.1.6] - 2024-02-27

### Changed

- add transparency for colors that have to be opaque (except editor fold, to match with sticky scroll)
- comment widget range

## [v0.1.5] - 2024-01-12

### Added

- color for error lens, to make it more muted

## [v0.1.4] - 2024-01-12

### Fixed

- incorrect license file name in package.json

## [v0.1.3] - 2024-01-12

### Changed

- license file name into `COPYING` following GNU suggestion

### Fixed

- remove unnecessary files, update .vscodeignore, reducing the size from 8mb to 1mb


## [v0.1.2] - 2024-01-12

### Changed

- change gitlens color to purple (inspirid by GitHub main page color). This is to differentiate with the ghost text


## [v0.1.1] - 2023-12-15

### Added

- sample text for github commit editor and javascript

### Changed

- change ghost color to differentiate with comment. Ghost color includes suggestion from intelliSense and AI suggestion.
- change progress bar color to be more vivid (match background of badge)

## [v0.1.0] - 2023-11-06

### Added

- Tool to demonstrate ANSI color 

### Changed

- Terminal ANSI color following [Monokai Vivid theme](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/screenshots/monokai_vivid.png)
- Button color, to make primary and secondary button more contrast
- Tab header color, was too contrast and distracting
- Folded line background, to match sticky scroll
- Status bar compact hover, it was too washed-out

## [Unreleased]

- Initial release
