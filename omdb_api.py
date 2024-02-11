# omdb_api.py
import requests

class OMDBApi:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_movies(self, search_query):
        # Funktion för att söka efter filmer baserat på en sökterm
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&s={search_query}"
        response = requests.get(url)
        response.raise_for_status()  # Kastar ett HTTPError om förfrågan misslyckas
        return response.json()

    def get_movie_details(self, movie_title):
        # Funktion för att hämta detaljer om en specifik film baserat på titel
        url = f"https://www.omdbapi.com/?apikey={self.api_key}&t={movie_title}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
