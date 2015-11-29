from media import Movie
import fresh_tomatoes

#Create Toy Story Movie

title = "Toy Story"
storyline = "Toys Come to Life"
release_date = "1995-11-22"
rated = "G"
poster_image_url = "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
toy_story = Movie(title,storyline,release_date,rated,poster_image_url,trailer_youtube_url)

#Create Martian Movie

title = "Martian"
storyline = "Escape from Mars"
release_date = "2015-10-2"
rated = "PG-13"
poster_image_url = "http://sumnersunsettheatre.com/wp-content/uploads/The-Martian-movie-poster.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=Ue4PCI0NamI"
martian = Movie(title,storyline,release_date,rated,poster_image_url,trailer_youtube_url)

#Create Inception Movie

title = "Inception"
storyline = "Dive to the dream"
release_date = "2010-7-13"
rated = "PG-13"
poster_image_url = "http://www.aceshowbiz.com/images/still/inception_poster01.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=66TuSJo4dZM"
inception = Movie(title,storyline,release_date,rated,poster_image_url,trailer_youtube_url)

#Store all movies in movies list and send to fresh_tomatoes to create web page to show movies and their descriptions

movies = [toy_story,martian,inception]
fresh_tomatoes.open_movies_page(movies)