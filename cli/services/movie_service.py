from services.api_service import ApiService

class MovieService(ApiService):

    def list_movies(self):
        data = self.get("/movies")
        items = {}
        for m in data:
            items[str(m["id"])] = f"{m['title']} (by {m['director'] or 'Unknown'} - {m['release_year'] or 'N/A'})"
        
        return {
            "title": "All Movies",
            "items": items
        }

    def create_movie(self, title, director, release_year):
        payload = {
            "title": title,
            "director": director,
            "release_year": release_year
        }
        data = self.post("/movies", payload)
        return {
            "title": "Movie Created Successfully",
            "items": {
                "ID": data["id"],
                "Title": data["title"],
                "Director": data["director"] or "Unknown",
                "Release Year": data["release_year"] or "N/A"
            }
        }
    
    def extract_movie_from_text(self, text: str):
        payload = {"text": text}
        data = self.post("/movies/ai-extract", payload)
        return {
            "title": "Movie Extracted Successfully",
            "items": {
                "ID": data["id"],
                "Title": data["title"],
                "Director": data["director"] or "Unknown",
                "Release Year": data["release_year"] or "N/A",
                "Rating": data["rating"] or "N/A",
                "Review": data["review"] or "N/A"
            }
        }