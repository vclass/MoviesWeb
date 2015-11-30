from media import Movie
import fresh_tomatoes


# Create Toy Story Movie

toy_story = Movie(
            "Toy Story",
            "Toys Come to Life",
            "1995-11-22",
            "G",
            "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Create Martian Movie

martian = Movie(
            "Martian",
            "Escape from Mars",
            "2015-10-2",
            "PG-13",
            "http://sumnersunsettheatre.com/wp-content/uploads/The-Martian-movie-poster.jpg",		# noqa
            "https://www.youtube.com/watch?v=Ue4PCI0NamI")

# Create Inception Movie

Inception = Movie(
            "Inception",
            "Dive to the dream",
            "2010-7-13",
            "PG-13",
            "hhttp://www.aceshowbiz.com/images/still/inception_poster01.jpg",
            "https://www.youtube.com/watch?v=66TuSJo4dZM")

# Store all movies in movies list and send to fresh_tomatoes to
# create web page to show movies and their descriptions

movies = [toy_story, martian, inception]
fresh_tomatoes.open_movies_page(movies)
