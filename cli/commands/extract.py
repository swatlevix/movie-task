from services.movie_service import MovieService
from utils.formatter import Formatter

class ExtractCommand:

    def execute(self, args):
        if len(args) < 1:
            print("Usage: extract <description>")
            print('Example: extract "Inception was an amazing sci-fi movie in 2010"')
            return

        text = " ".join(args)
        Formatter.display(MovieService().extract_movie_from_text(text))