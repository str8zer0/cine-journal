# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

_No unreleased changes yet._

---

## [1.1.0] – 2026-02-22

### Added
- Database seed command for generating sample movies, genres, tags, reviews, and lists.
- `cover_or_placeholder` property to provide fallback images for movies without a cover.

### Changed
- Updated README and INSTALL documentation with seed instructions and navigation links.

### Fixed
- Corrected rating display logic to show accurate average ratings.

---

## [1.0.0] – 2026-02-21

### Added
- Movie filters and pagination for improved browsing.
- Additional core features across movies, reviews, lists, and watch plans.

### Changed
- General UI refinements and template improvements.

---

## [0.4.0] – 2026-02-20

### Added
- “Highest Rated Movies” section on the homepage.

### Changed
- Footer extracted into a standalone partial template.
- Multiple templates redesigned for improved layout and UX.
- Fine‑tuned styling and structure across the application.

---

## [0.3.0] – 2026-02-19

### Added
- Additional templates for movies, lists, reviews, and watch plans.

### Changed
- Reorganized views, forms, and models for better maintainability.

---

## [0.2.0] – 2026-02-18

### Added
- Main views and forms for core application functionality.
- Foundational project files.

---

## [0.1.0] – 2026-02-17

### Added
- Initial Django project setup.
- Base apps: `movies`, `journal`, `library`, `common`.
- Initial models for movies, genres, tags, reviews, lists, and watch plans.

---