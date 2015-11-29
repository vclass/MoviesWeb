import webbrowser

class Movie():
	"""A movie class that stores its desription and details

	Attributes:
		title: A string contains movie title name
		storyline: A string decribes main story line of the movie
		release_date: A string indicate movie's release date
		rated: A string indicates movies rated e.g. G, PG, PG-13 etc.
		poster_image_url: A link to movie's poster image
		youtube_url: A link to movie's trailer 
	"""

	def __init__(self,movie_title,movie_storyline,movie_release_date,movie_rated,poster_image,trailer_youtube):
		"""Inits Movie class with their movie's attributes"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.release_date = movie_release_date
		self.rated = movie_rated
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

