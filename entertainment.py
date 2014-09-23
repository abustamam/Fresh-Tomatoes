import media
import fresh_tomatoes

bioshock = media.Game("Bioshock Infinite",
                    "https://www.youtube.com/watch?v=XZmxvig1dXE", 1)

brawl = media.Game("Super Smash Bros. Brawl",
                       "https://www.youtube.com/watch?v=Lmw78t8NgIE", 4)

portal = media.Game("Portal 2",
                     "https://www.youtube.com/watch?v=TluRVBhmf8w", 2)

bad = media.TVShow("Breaking Bad",
                  "https://www.youtube.com")

dead = media.TVShow("The Walking Dead",
                   "https://www.youtube.com")

thrones = media.TVShow("Game of Thrones",
                      "https://www.youtube.com")

frozen = media.Movie("Frozen",
                     "https://www.youtube.com/watch?v=Zb5IH57SorQ")

lucy = media.Movie("Lucy",
                   "https://www.youtube.com/watch?v=MVt32qoyhi0")

avengers = media.Movie("The Avengers",
                       "https://www.youtube.com/watch?v=QDajL441mZc")

games = [bioshock,brawl,portal]

shows = [bad, dead, thrones]

movies = [frozen,lucy,avengers]

fresh_tomatoes.open_movies_page(movies)
