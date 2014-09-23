import media
import fresh_tomatoes

bioshock = media.Game("Bioshock Infinite",
                    "https://www.youtube.com/watch?v=XZmxvig1dXE", 1)

brawl = media.Game("Super Smash Bros. Brawl",
                       "https://www.youtube.com/watch?v=Lmw78t8NgIE", 4)

portal = media.Game("Portal 2",
                     "https://www.youtube.com/watch?v=TluRVBhmf8w", 2)

bad = media.TVShow("Breaking Bad",
                  "https://www.youtube.com/watch?v=oDqGAUvWKkU")

dead = media.TVShow("The Walking Dead",
                   "https://www.youtube.com/watch?v=rNxvo8AcpQQ")

thrones = media.TVShow("Game of Thrones",
                      "https://www.youtube.com/watch?v=SVaD8rouJn0")

frozen = media.Movie("Frozen",
                     "https://www.youtube.com/watch?v=Zb5IH57SorQ")

lucy = media.Movie("Lucy",
                   "https://www.youtube.com/watch?v=MVt32qoyhi0")

avengers = media.Movie("The Avengers",
                       "https://www.youtube.com/watch?v=QDajL441mZc")

games = {"name": "Games",
         "content": [bioshock,brawl,portal]}

shows = {"name": "TV Shows",
         "content": [bad, dead, thrones]}

movies = {"name": "Movies",
          "content": [frozen,lucy,avengers]}

cont = [games, shows, movies]

fresh_tomatoes.open_movies_page(cont)
