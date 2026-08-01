# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-08-01

### Added

- Initial release of PWA Manager.
- Command-based CLI architecture.
- PWA discovery and management for Linux desktop environments.
- Application listing:
  - managed PWAs
  - Chrome PWAs
  - desktop applications

### Commands

Implemented commands:

- `list`
- `doctor`
- `status`
- `repair`
- `backup`
- `restore <backup>`
- `export`
- `clean`
- `clean --fix`

### Backup and Recovery

- Added desktop file backup.
- Added icon backup.
- Added restore functionality.
- Added portable export configuration.

### Icon Management

- Added centralized icon discovery module.
- Unified icon handling for backup and export.
- Added support for:
  - local icon files
  - icon themes
  - Chrome PWA icons

### CLI Improvements

- Added `--help`.
- Added `--version`.
- Added version information.

### Architecture

- Introduced modular command structure.
- Added shared application context.
- Improved separation between:
  - CLI layer
  - command layer
  - core functionality
  - utilities

### Validation

Verified on Ubuntu desktop environment:

- 9 applications detected.
- 9/9 applications healthy.
- Backup and restore tested.
- Export tested.
- Duplicate detection tested.
