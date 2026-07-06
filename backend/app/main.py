from fastapi import FastAPI, HTTPException
from app.database import MOVIES_DB
from app.schemas import MovieCreate, MovieResponse, TextInput
from app.llm import extract_movie

app = FastAPI(title="Movie Management System", version="1.0.0")

@app.post("/movies/ai-extract", response_model=MovieResponse, status_code=201)
def extract_and_create(payload: TextInput):
    movie_data = extract_movie(payload.text) 
    
    next_id = max(MOVIES_DB.keys(), default=0) + 1
    new_movie = {
        "id": next_id,
        "title": movie_data.title,
        "director": movie_data.director,
        "release_year": movie_data.release_year,
        "rating": movie_data.rating,
        "review": movie_data.review,
        "is_watched": False
    }
    MOVIES_DB[next_id] = new_movie
    return new_movie