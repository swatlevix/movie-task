from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    director: Optional[str] = None 
    release_year: Optional[int] = Field(None, ge=1888, le=2030) 

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int
    rating: Optional[int] = None
    is_watched: bool = False

    class Config:
        from_attributes = True
