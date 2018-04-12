import os
import io
import numpy
from pandas import DataFramefrom sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

"""
*Spam classifier using naive bayes (Simplified)
*
"""

#read files and parse
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for name in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            file_ = io.open(path, 'r', encoding = 'latin1')
            for line in file_:
                if inBody:
                    lines.append(line)

                elif line == '\n':
                    inBody = True

            f.close()
            message = '\n'.join(lines)
            yield path, message


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


#split up each message into its list of words
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values) #email contents

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts,targets)
