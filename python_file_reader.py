def read_text():
    quotes = open("/Users/ankeshkhemani/Dropbox/Projects/movie_quotes.txt")
    contents=quotes.read()
    print(contents)
    quotes.close()

read_text()
    
