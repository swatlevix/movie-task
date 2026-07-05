from services.movie_service import MovieService
from utils.formatter import Formatter

class AddCommand:    
    def execute(self, args):
        if len(args) < 1:
            print("Usage: add <title> [director] [release_year]")
            print("Example: add 'Interstellar' 'Christopher Nolan' 2014")
            return

        title = args[0]
        director = args[1] if len(args) > 1 else None
        
        release_year = None
        if len(args) > 2:
            try:
                release_year = int(args[2])
            except ValueError:
                print("Error: Release year must be a valid number.")
                return

        Formatter.display(MovieService().create_movie(title, director, release_year))