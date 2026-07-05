from services.movie_service import MovieService
from utils.formatter import Formatter

class ShowCommand:
    
    def execute(self, args):
        Formatter.display(MovieService().list_movies())