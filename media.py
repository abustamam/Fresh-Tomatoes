import webbrowser
import imdb

def get_info(title):
    i = imdb.IMDb()
    lst = i.search_movie(title)
    match = lst[0]
    i.update(match)
    return match

class Video():
    def __init__(self, title, trailer_youtube):
        self.title = title
        self.dat = get_info(title)
        self.storyline = self.dat['plot outline']
        self.poster = self.dat['full-size cover url']
        self.genre = self.dat['genres'][0]
        self.trailer = trailer_youtube
    
class Movie(Video):
    def __init__(self, title, trailer_youtube):
        Video.__init__(self, title, trailer_youtube)
        self.runtime = self.dat['runtimes'][0]

    def show_info(self):
        return "<p><strong>Runtime:</strong> " + str(self.runtime) + "</p>"
        

class Game(Video):
    def __init__(self, title, trailer_youtube, number_players):
        Video.__init__(self,title,trailer_youtube)
        self.developer = self.dat['production companies'][0]['name']
        self.publisher = self.dat['distributors'][0]['name']
        self.number_players = number_players

    def show_info(self):
        return ("<p><strong>Developer: </strong>" + str(self.developer) + "</p>"
               "<p><strong>Publisher: </strong>" + str(self.publisher) + "</p>"
               "<p><strong>Number of Players: </strong>" + str(self.number_players) + "</p>"
                )

class TVShow(Video):
    def __init__(self, title, trailer_youtube):
        Video.__init__(self, title, trailer_youtube)
        self.seasons = self.dat['seasons']
        self.station = self.dat['distributors'][0]['name']
        self.runtime = self.dat['runtimes'][0]

    def show_info(self):
        return ("<p><strong>Seasons: </strong>" + str(self.seasons) + "</p>" 
               "<p><strong>Station: </strong>" + str(self.station) + "</p>" 
               "<p><strong>Runtime: </strong>" + str(self.runtime) + "</p>"
                )
