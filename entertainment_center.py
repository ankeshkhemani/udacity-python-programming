#!/usr/bin/env python
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("Avatar",
						"A story of a marine on an alien planet",
						"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")
dark_knight = media.Movie("Dark Knight",
						"Batman fights his worst enemy",
						"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=yQ5U8suTUw0")
#print dark_knight.storyline
#dark_knight.show_trailer()
movies = [toy_story, avatar, dark_knight]
fresh_tomatoes.open_movies_page(movies)