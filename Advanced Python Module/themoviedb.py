#themoviedb.org  ==> movie and series archive
#use themoviedb's methods api in your app
#search by keyword
#most popular movies list
#list of movies released

import requests

class theMovieDb:
    def __init__(self):
        self.api_url= "https://api.themoviedb.org/3/"
        self.api_key ="c665a6929b693d7f7fc82a3a7e2ec1dd"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}+movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    

movieApi = theMovieDb()



while True:
    select = input("1-Popular Movies\n2-Exit\nSelection: ")

    if select == "2":
        break
    elif select == "1":
        movies = movieApi.getPopulars()
        print(movies)

# not done