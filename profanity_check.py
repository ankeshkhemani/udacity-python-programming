import urllib


def read_text():
    quotes = open("/Users/ankeshkhemani/Dropbox/Projects/movie_quotes.txt")
    contents=quotes.read()
    quotes.close()
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+contents)
    output=connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert")
    else:
        print("No curse words found")
   
read_text()
    


