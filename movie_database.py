# movie_database.py
from omdb_api import OMDBApi

class MovieDatabase:
    def __init__(self, api_key):
        self.omdb_api = OMDBApi(api_key)
        self.search_history = []

    def search_movies(self, search_query):
        try:
            # Söker efter filmer och visar resultaten för användaren
            data = self.omdb_api.search_movies(search_query)

            if data.get("Response") == "True":
                movies = data.get("Search", [])

                if not movies:
                    print("Inga resultat hittades.")
                    return

                print("Hittade följande filmer:")
                for idx, movie in enumerate(movies, start=1):
                    print(f"{idx}. {movie['Title']} ({movie['Year']})")

                choice = input("Välj vilken film du vill ha detaljer om (1-{}): ".format(len(movies)))
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(movies):
                        chosen_movie = movies[choice - 1]
                        self.get_movie_details(chosen_movie['Title'])
                        # Lägg till sökningen i historiken
                        self.add_to_history(search_query)
                    else:
                        print("Ogiltigt val. Försök igen.")
                except ValueError:
                    print("Ogiltigt val. Försök igen.")
            else:
                print("Inga resultat hittades.")
        except requests.exceptions.RequestException as err:
            print(f"Ett oväntat problem uppstog: {err}")

    def get_movie_details(self, movie_title):
        try:
            # Hämtar detaljer om en specifik film och visar informationen
            data = self.omdb_api.get_movie_details(movie_title)

            if data.get("Response") == "True":
                print(f"Detaljer för filmen '{data['Title']}':")
                print(f"- År: {data['Year']}")
                print(f"- Skådespelare: {data['Actors']}")
                print(f"- Betyg: {data['imdbRating']}")
                # Lägg till fler detaljer om du vill få annan information
            else:
                print("Kunde inte hämta detaljer för den valda filmen.")
        except requests.exceptions.RequestException as err:
            print(f"An unexpected error occurred: {err}")

    def add_to_history(self, search_query):
        # Lägger till sökningen i historiken och behåller endast de senaste fem sökningarna
        self.search_history.append(search_query)
        if len(self.search_history) > 5:
            self.search_history.pop(0)

    def show_history(self):
        # Visar historiken för användaren
        print("\nSökhistorik:")
        for idx, search_query in enumerate(self.search_history, start=1):
            print(f"{idx}. {search_query}")
