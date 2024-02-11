# main.py
from movie_database import MovieDatabase

def search_movies(movie_db):
    # Funktion för att söka efter filmer och visa resultatet
    search_query = input("Ange en film att söka efter: ")
    movie_db.search_movies(search_query)

def get_movie_details(movie_db):
    # Funktion för att hämta detaljer om en specifik film
    movie_title = input("Ange titeln på den film du vill ha detaljer om: ")
    movie_db.get_movie_details(movie_title)

def show_history(movie_db):
    # Funktion för att visa sökhistorik
    movie_db.show_history()

def exit_program(movie_db):
    # Funktion för att avsluta programmet
    print("Tack för att du använde Filmdatabasen. Hej då!")
    quit()

def read_api_key():
    try:
        with open("api_key.txt", "r") as file:
            api_key = file.readline().strip()
            return api_key
    except FileNotFoundError:
        print("Filen api_key.txt kunde inte hittas.")
        quit()

def main():
    api_key = read_api_key()
    movie_db = MovieDatabase(api_key)

    # Dictionary som matchar användarens val med motsvarande funktion
    menu_options = {
        '1': search_movies,
        '2': get_movie_details,
        '3': show_history,
        '4': exit_program
    }

    while True:
        print("\nVälkommen till Filmdatabasen!")
        print("1. Sök efter en film")
        print("2. Visa detaljer för en specifik film")
        print("3. Visa sökhistorik")
        print("4. Avsluta programmet")
        choice = input("Välj ett alternativ (1/2/3/4): ")

        # Hämtar och kör funktionen baserat på användarens val
        selected_function = menu_options.get(choice)
        if selected_function:
            selected_function(movie_db)
        else:
            print("Ogiltigt val. Försök igen. Giltiga val är 1-4")

if __name__ == "__main__":
    main()
