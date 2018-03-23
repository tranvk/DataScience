import pandas as pd
import numpy as np

r_cols = ["user_id", "movie_id", "rating"] #column titles

ratings = pd.read_csv("/home/kevin/Documents/Data Science/DataScience-Python3/ml-100k/u.data", sep = '\t', names = r_cols, usecols=range(3), encoding = "ISO-8859-1")#link to movieLens dataset

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
