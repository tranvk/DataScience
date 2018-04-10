import pandas as pd
import numpy as np
from scipy import spatial
import operator

r_cols = ["user_id", "movie_id", "rating"] #column titles

ratings = pd.read_csv("/home/kevin/Documents/Data Science/DataScience-Python3/ml-100k/u.data", sep = '\t', names = r_cols, usecols=range(3), encoding = "ISO-8859-1")#link to movieLens dataset


movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x))/(np.max(x) - np.min(x)))


movieDict = {}

with open (r'/home/kevin/Documents/Data Science/DataScience-Python3/ml-100k/u.data') as file_:

    temp = ''

    for line in file_:  #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'),
        movieProperties.loc[movieID].rating.get('mean'))





#compute distance between two movies based on how similar their genres and popularity are
def ComputeDistance(a, b):

    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)

    return genreDistance + popularDistance

m_cols = ["movie_id", "title"]

movies = pd.read_csv("/home/kevin/Documents/Data Science/DataScience-Python3/ml-100k/u.item", sep = '|', names = m_cols, usecols= range(2), encoding = "ISO-8859-1")

ratings = pd.merge(movies,ratings)

movieRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values ='rating')

starWarsRatings = movieRatings['Star Wars (1977)']

similarMovies = movieRatings.corrwith(starWarsRatings) #compute pairwise correlation
similarMovies = similarMovies.dropna() #drop NaN RESULTS
df = pd.DataFrame(similarMovies)

similarMovies.sort_values(ascending = False)

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending = False)[:15]

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns = ['similarity']))

df.sort_values(['similarity'], ascending = False)[:15]

print(df)
