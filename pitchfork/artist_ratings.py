
import pandas as pd
import sqlite3


#SQLite to Pandas
#Connect to database

connection = sqlite3.connect("/home/kevin/Documents/Data Science/Projects/pitchfork/database.sqlite")

#DataFrame
review_data = pd.read_sql_query("SELECT `_rowid_`,* FROM `reviews`  ORDER BY `artist` ASC LIMIT 0, 50000", connection)

'''
Plan: sort artists by alphabet
      add up the review scores
      average the review scores
      return the most successful artists
'''

#get review by artist name
dictionary_artists = dict(tuple(review_data.groupby('artist')))

artists = [dictionary_artists[x] for x in dictionary_artists] #list of DataFrame split by artist name

various_artists = []

single_artists = []

#special case for various artists label

for name in artists:
    if (name.iloc[0]["artist"] == "various artists"):
        various_artists.append(name)
    else:
        single_artists.append(name)

#already have dataframes split by artists name. ie: kanye has his own dataframe
#access score column of dataframe and get average score
#loc takes labels, iloc takes positions (index number)
#loc params = [row, column]

# next: remove outliers, include sample size with the mean

#output name, score, size
list_scores = []
list_names = []
list_amount = []
artist_stats = {}

for y in range(0, len(single_artists)): #len(artists) reflects number of unique artists
    for scores in single_artists[y].loc[:, "score"]:
        
        names = single_artists[y].iloc[0]['artist']
        average_score = single_artists[y].loc[:,"score"].mean()
        amount_reviews = len(single_artists[y].loc[:,"score"])

    list_names.append(names)
    list_scores.append(average_score)
    list_amount.append(amount_reviews)

#most successful artists
#sort average scores, high to low
sorted_scores = sorted(list_scores, key = float)

print(sorted_scores)
