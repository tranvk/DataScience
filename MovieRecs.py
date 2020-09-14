import pandas as pd
import numpy as np
from scipy import spatial
import operator

"""
*@ComputeDistance: #compute distance between two movies based on how similar their genres and popularity are
*@getNeighbors: #compute distance between a test movie and all the movies on the data set, print out K nearest neighbors
*@findMovieByName: check if movie exists, param: movie name, the year
"""

r_cols = ["user_id", "movie_id", "rating"] #column titles

file_path = "" #Enter CSV Path

ratings = pd.read_csv(file_path, sep = '\t', names = r_cols, usecols=range(3), encoding = "ISO-8859-1") #Link to movieLens dataset

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])

movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x))/(np.max(x) - np.min(x)))

movieDict = {}

with open (file_path, encoding = "ISO-8859-1") as file_:

    temp = ''

    for line in file_:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'),
        movieProperties.loc[movieID].rating.get('mean'))
        
def ComputeDistance(a, b):

    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)

    return genreDistance + popularityDistance



def getNeighbors(movieID, K):

    distances = []

    for movie in movieDict:
        if (movie!= movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie,dist))

    distances.sort(key = operator.itemgetter(1))
    neighbors = []

    for x in range(K):
        neighbors.append(distances[x][0])

    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= K

#check if movie exists
#param: movie name + the year
def findMovieByName(name):

    if name in movieDict:
        return True
    else:
        return False

print (findMovieByName("Aladdin (1992)"))
