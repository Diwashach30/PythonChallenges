## Create a dictionary of your favourite movies and their release years. Add a new movie to the dictionary, update the release year of one of the movies, and then 
## remove a movie.

fav_movies = {
    'Pushpa' : 1999,
    'Sarangi' : 2009 ,
    'Thor' : 2024,
}



fav_movies['KGF'] = 2023 
fav_movies['Sarangi'] =2024

fav_movies.pop('Pushpa')

print(fav_movies)