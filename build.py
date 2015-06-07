#!/usr/bin/python
import fresh_tomatoes
import media

# Mad Max: Fury Road
mad_max = media.Movie("Mad Max: Fury Road", 
	"""In a stark desert landscape where humanity is broken, two rebels just might be able to restore order:
	Max, a man of action and of few words, and Furiosa, a woman of action who is looking to make it back
	to her childhood homeland.""",
	"120min",
	"http://media.aintitcool.com/media/uploads/2015/harry/11221365_672048706233987_4076824778214239268_n_huge.jpg",
	"https://www.youtube.com/watch?v=hEJnMQG9ev8",
	3)
	
# Furious 7
furious_7 = media.Movie("Furious 7",
	"""Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.""",
	"137min",
	"http://cdn2-www.comingsoon.net/assets/uploads/2015/02/Furious7onelastposterbig.jpg",
	"https://www.youtube.com/watch?v=Skpu5HaVkOc",
	2)
	
# Interstellar
interstellar = media.Movie("Interstellar",
	"""A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.""",
	"169min",
	"http://i.imgur.com/p5XDFbH.jpg",
	"https://www.youtube.com/watch?v=zSWdZVtXT7E",
	2)
	
# Ex Machina
ex_machina = media.Movie("Ex Machina",
	"""A young programmer is selected to participate in a breakthrough experiment in artificial intelligence 
	by evaluating the human qualities of a breathtaking female A.I.""",
	"108min",
	"http://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SX640_SY720_.jpg",
	"https://www.youtube.com/watch?v=gyKqHOgMi4g",
	3)

# Add Movies to an array
movies = [mad_max, furious_7, interstellar, ex_machina]

# Kick off the web page
fresh_tomatoes.open_movies_page(movies)