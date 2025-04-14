# Telegram Mini App

A Python-based Telegram Mini App that demonstrates user data handling and profile picture access.

## Features

- User authentication and data storage
- Profile picture access and display
- Last seen tracking
- Modern, responsive UI

## Prerequisites

- Python 3.9 or higher
- MongoDB instance
- Poetry for dependency management

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-mini-app.git
cd telegram-mini-app
```

2. Install dependencies:
```bash
poetry install
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
MONGODB_URI=your_mongodb_uri_here
FLASK_ENV=development
FLASK_DEBUG=1
```

4. Activate the virtual environment:
```bash
poetry shell
```

## Running the Application

Start the development server:
```bash
python run.py
```

The application will be available at `http://localhost:3000`.

## Project Structure

```
telegram-mini-app/
├── src/
│   └── telegram_mini_app/
│       ├── __init__.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py
│       └── web/
│           ├── __init__.py
│           ├── routes.py
│           └── templates/
│               └── index.html
├── .env
├── .gitignore
├── pyproject.toml
└── run.py
```

## License

MIT 