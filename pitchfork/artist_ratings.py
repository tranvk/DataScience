
import pandas as pd
import sqlite3


#SQLite to Pandas


#Connect to database

connection = sqlite3.connect("/home/kevin/Documents/Data Science/Projects/pitchfork/database.sqlite")

#DataFrame
review_data = pd.read_sql_query("SELECT `_rowid_`,* FROM `reviews`  ORDER BY `artist` ASC LIMIT 0, 50000", connection)

#sort artists by alphabet
#add up the review scores
#average the review scores
#return the most successful artists


#get review by artist name
#print(review_data.loc[review_data['artist'] == "!!!"])

dictionary_artists = dict(tuple(review_data.groupby('artist')))

artists = [dictionary_artists[x] for x in dictionary_artists] #list of DataFrame split by artist name

"""def average_score (database): #access scores in each artist entry
    total = 0
    for artist in database:
        for score in artist['score']:
            total += score

            """



#already have dataframes split by artists name. ie: kanye has his own dataframe
#access score column of dataframe and get average score
#loc takes labels, iloc takes positions (index number)
#loc params = [row, column]
print ((artists[1].loc[:, "score"]))


for y in range(0, len(artists)): #len(artists) reflects number of unique artists
    for scores in artists[y].loc[:, "score"]:

        print(artists[y].loc[:, "score"].mean())
print(len(artists))
