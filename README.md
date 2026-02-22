# CineJournal 🎬

CineJournal is a personal movie diary that helps users track the films they watch, record their impressions, and organize their movie experiences. Instead of being just another movie database, CineJournal focuses on personal reflection — capturing moods, thoughts, and memories associated with each film. The app also helps users plan what to watch next by organizing movies into custom lists and categories.

## 🚀 Key Features

- **Movie Catalog**: Browse and manage movies with detailed information including release year, genres, and covers.
- **Journaling**: Write and manage movie reviews with ratings (1.0 - 10.0).
- **Movie Lists**: Create custom lists of movies (e.g., "Top 10 Sci-Fi", "Watch with Friends").
- **Watch Plans**: Plan movie watching sessions by selecting a list and setting a date and available duration.
- **Responsive Design**: Built with Bootstrap for a seamless experience on all devices.
- **Custom 404**: A user-friendly 404 error page.

## 🛠️ Technology Stack

- **Backend**: Django 6.0 (Python 3.13+)
- **Database**: PostgreSQL
- **Frontend**: Django Templates & Bootstrap
- **Package Management**: `uv`
- **Environment Management**: `python-environ`

## 📂 Project Structure

The project is divided into four main Django apps, each with a specific responsibility:

1.  **`movies`**: Handles movie-related data, genres, and tags.
2.  **`journal`**: Manages user-generated reviews and ratings.
3.  **`library`**: Handles movie lists and watch planning logic.
4.  **`common`**: Contains reusable mixins, custom template tags, and general views (e.g., home page).

## 📄 Documentation

- [**Installation Guide (INSTALL.md)**](INSTALL.md): Step-by-step instructions to set up the project locally.
- [**Changelog (CHANGELOG.md)**](CHANGELOG.md): History of changes and versions.
- [**License (LICENSE)**](LICENSE): Copyright and licensing information.
