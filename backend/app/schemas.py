from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    director: Optional[str] = None 
    release_year: Optional[int] = Field(None, ge=1888, le=2030) 
    rating: Optional[int] = Field(None, ge=1, le=5)
    review: Optional[str] = None
    
class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int
    is_watched: bool = False

    class Config:
        from_attributes = True

class TextInput(BaseModel):
    text: str