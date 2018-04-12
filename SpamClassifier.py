import os
import io
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

"""
*Spam classifier using naive bayes (Simplified)
*TODO: train/test
"""

#read files and parse
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for name in filenames:
            path = os.path.join(root, name)

            inBody = False
            lines = []
            file_ = io.open(path, 'r', encoding = 'latin1')
            for line in file_:
                if inBody:
                    lines.append(line)

                elif line == '\n':
                    inBody = True

            file_.close()
            message = '\n'.join(lines)
            yield path, message


#populate dataframe from from directory
def dataFrameFromDirectory(path, classification):

    rows = []
    index = []

    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index = index)

data = DataFrame({'message': [],  'class': []})

data = data.append(dataFrameFromDirectory('/home/kevin/Documents/Data Science/DataScience-Python3/emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('/home/kevin/Documents/Data Science/DataScience-Python3/emails/ham', 'ham'))

#implement train/test

train,test = train_test_split(data, test_size = 0.2)

#split up each message into its list of words
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(train['message'].values) #email contents

classifier = MultinomialNB()
targets = train['class'].values
classifier.fit(counts,targets)

#try your code

examples = [' Viagra free now!!!', " this is spam free", 'sdfasdf', "Hi free viagra Bob, how  free about a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print(train)
