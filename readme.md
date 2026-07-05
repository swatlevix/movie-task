🎬 Movie Watchlist Management System

A lightweight, academic-grade client-server application built to demonstrate Distributed Systems Architecture and Separation of Concerns.

This system consists of a fast FastAPI Backend Server utilizing an In-Memory Dictionary for storage, coupled with an interactive Typer CLI Client that communicates with the backend over HTTP.

🏗️ System Architecture

The project is designed with a strict separation between the user interface and the backend processing logic:

       [ Typer CLI Frontend ]  (Command-line interface)
                 │
           HTTP Requests  (JSON over HTTP)
                 │
     [ FastAPI Backend Server ]  (Process logic & endpoints)
                 │
       [ In-Memory Dictionary ]  (Data storage in RAM)


Key Design Highlights:

Separation of Concerns: The CLI Frontend is completely independent of the FastAPI Backend.

Low Coupling: Changing the storage system in the future (e.g., migrating from in-memory to a database like Supabase) will not require any changes to the CLI code.

Simple & Modular: The system is easy to read, expand, and debug.

📂 Project Structure

This project follows a clean, modular structure exactly as requested:

MOVIE_PROJECT/
│
├── backend/               # Backend Server Files
│   └── app/
│       ├── __init__.py    # Python package initializer
│       ├── database.py    # In-memory dictionary database
│       ├── main.py        # FastAPI routes & server config
│       └── schemas.py     # Pydantic data validation models
│
├── cli/                   # CLI Client Files
│   ├── commands/          # CLI command logic
│   │   ├── add.py         # Logic for adding a movie
│   │   └── show.py        # Logic for showing all movies
│   ├── services/          # API communication layer
│   │   ├── api_service.py # Base HTTP client
│   │   └── movie_service.py # Movie-specific API calls
│   ├── utils/
│   │   └── formatter.py   # Console output formatting utility
│   └── main.py            # CLI application entry point
│
├── .gitignore             # Git ignore file for Python cache
└── README.md              # This project documentation


🚀 How to Run the Project

1️⃣ Step 1: Install Required Libraries

Open your Terminal/PowerShell in the main MOVIE_PROJECT directory and run:

pip install fastapi uvicorn pydantic requests


2️⃣ Step 2: Start the Backend Server

Navigate to the backend folder and run the FastAPI server:

cd backend
python -m uvicorn app.main:app --reload

💡 The backend server will run on: http://127.0.0.1:8000

You can test the endpoints interactively at: http://127.0.0.1:8000/docs

3️⃣ Step 3: Run the CLI Client

Open a new Terminal window (keep the backend server running in the background), navigate to the cli folder:

cd cli


📌 Command: Show Movies

Retrieve and display all movies stored in the memory:

python main.py show


📌 Command: Add Movie

Add a new movie to your watchlist:

python main.py add "Interstellar" "Christopher Nolan" 2014


Run the show command again to see your new movie added to the table!

🛠️ Tech Stack

FastAPI: Modern, fast web framework for building APIs.

Typer: Friendly library for building CLI applications.

Pydantic: Data validation and settings management.

Requests: Standard HTTP library for Python to talk to the backend.