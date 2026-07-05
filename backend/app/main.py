from fastapi import FastAPI, HTTPException, status
from typing import List
from app.database import MOVIES_DB
from app.schemas import MovieCreate, MovieResponse

app = FastAPI(title="Movie Management System", version="1.0.0")

@app.get("/movies", response_model=List[MovieResponse])
def get_movies():
    return list(MOVIES_DB.values())

@app.post("/movies", response_model=MovieResponse, status_code=201)
def create_movie(payload: MovieCreate):
    next_id = max(MOVIES_DB.keys(), default=0) + 1
    new_movie = {
        "id": next_id,
        "title": payload.title,
        "director": payload.director,
        "release_year": payload.release_year,
        "is_watched": False
    }
    MOVIES_DB[next_id] = new_movie
    return new_movie