# Author Eric Wallace
# Assignment A0
# Course CIS 225

# There is definately a more elegant way to code this but, 
# it took me a whole lot of review to get to this point. It works though!

# Setting up the empty dictionary
moviedb = {}

# The struggle was real until I remembered the while True part, 
# kept entering movie data over and over only to lose it at the program end
while True:
    # Ask for the user for their name
    fullname = input("Enter your first and last name: ")
    # Loop through the moviedb to check if the user exists and displays top movies if so
    if fullname in moviedb:
        print("Top five movies: ")
        for movie in moviedb[fullname]:
            print("Title: " + movie["title"])
            print("Director: " + movie["director"])
            print("Release year: " + movie["year"])
            print("IMDB rating: " + movie["imdb"])
            print("Rotten Tomatoes rating: " + movie["tomatoes"])
            print("MPAA rating: " + movie["mpaa"])
    else:
        # Create a list of movies for the user in the moviedb dictionary
        moviedb[fullname] = []
        print("User was not found, please enter your top five movies.")
        for i in range(5):
            title = input("Enter movie title: ")
            director = input("Enter director's name: ")
            year = input("Enter the year it was released: ")
            imdb = input("Enter the star rating the movie has on IMDB: ")
            tomatoes = input("Enter the movie's Rotten Tomatoes rating %: ")
            mpaa = input("Enter the MPAA rating 'PG, PG-13, R, etc.': ")
            moviedb[fullname].append({
                "title": title,
                "director": director,
                "year": year,
                "imdb": imdb,
                "tomatoes": tomatoes,
                "mpaa": mpaa
                })







