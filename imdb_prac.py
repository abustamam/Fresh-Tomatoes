import imdb

i = imdb.IMDb()
# movie_list is a list of Movie objects, with only attributes like 'title'
# and 'year' defined.
movie_list = i.search_movie('kingsman: secret service')
# the first movie in the list.
first_match = movie_list[0]
# only basic information like the title will be printed.
# print first_match.summary()
# update the information for this movie.
i.update(first_match)
# a lot of information will be printed!
# print first_match.summary()
# retrieve trivia information and print it.
i.update(first_match, 'trivia')
# print first_match['trivia'][0]
# retrieve both 'quotes' and 'goofs' information (with a list or tuple)
i.update(first_match, ['quotes', 'goofs'])
# print first_match['quotes'][0][0]
# print first_match['goofs'][0]
# retrieve every available information.
# i.update(first_match, 'all')

print first_match.keys()

#print first_match['full-size cover url']
