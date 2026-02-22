# Installation Guide

Follow these steps to set up the **CineJournal** project locally.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1.  **Python 3.13+**
2.  **PostgreSQL** (running and accessible)
3.  **uv** (recommended Python package manager)

## 1. Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/str8zer0/cine-journal.git
cd cine-journal
```

## 2. Environment Configuration

The project uses `python-environ` to manage configuration through a `.env` file. 

1.  Create a file named `.env` in the project root.
2.  Add the following variables and adjust them for your local PostgreSQL setup:

```env
DEBUG=True
SECRET_KEY=your-super-secret-key-change-me
ALLOWED_HOSTS=127.0.0.1 localhost

DATABASE_NAME=cine_journal_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

> **Note:** Authentication and Django User management are explicitly excluded from this project's current scope as per requirements.

## 3. Install Dependencies

Using `uv` is the recommended way to install dependencies:

```bash
uv sync
```

Alternatively, if you prefer using `pip`:

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```
*(Note: If `requirements.txt` is not present, use `uv export --format requirements-txt > requirements.txt` if you have `uv` installed, or just use `uv sync`)*

## 4. Generate a Secret Key
1. Make sure all dependencies are installed as described in the previous step.
2. Open a Django shell:

```bash
uv run manage.py shell
```
3. Inside the shell, run the following to generate a secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

4. Copy the generated key and paste it into your `.env` file as the value for `SECRET_KEY`.

## 4. Database Setup

1.  Create the database in PostgreSQL as specified in your `.env` (e.g., `cine_journal_db`).
2.  Apply migrations:

```bash
uv run manage.py migrate
```

## 5. (Optional) Load Seed Data

The project includes an optional seed script that populates the database with:

- sample movies  
- genres and tags  
- reviews  
- movie lists  
- watch plans  

To load the seed data, run:

```bash
uv run manage.py seed
```

## 6. Running the Application

Start the Django development server:

```bash
uv run manage.py runserver
```

> **Note:** The server will run on port 8000 by default.
The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 7. Verification

- Ensure you see the home page.
- Navigate through Movies, Reviews, Movie Lists, and Watch Plans to confirm everything is working.
- A custom 404 page is also implemented for testing invalid URLs.
