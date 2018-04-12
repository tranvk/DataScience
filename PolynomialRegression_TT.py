import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from sklearn.metrics import r2_score

"""
*Split 80 percent of data for training and 20 for testing
*Randomly generated before the split
*Goal: Test different polynomial regressions against training data
*Correct: Why do overfitted polynomials return high r-squared?
*And why is the test data returning negative r2?
"""


# Simple Data Set for model

np.random.seed(2)

pageSpeeds = np.random.normal(3, 1, 100)
purchaseAmount = np.random.normal(50, 30, 100)/pageSpeeds

scatter(pageSpeeds, purchaseAmount)


#Split data into two parts
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

#training dataset
scatter(trainX, trainY)

#test dataset
scatter(testX, testY)

#fit n-degree polynomial to data
x = np.array(trainX)
y = np.array(trainY)

degree = int(input("Enter the polynomial degree: "))

p4 = np.poly1d(np.polyfit(x, y, degree))

#plot polynomial against training data

xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(x,y)
plt.plot(xp, p4(xp), c = 'r') #p4 is a function
plt.show()

testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c = 'r')
plt.show()

#r-squared score to verify correlation

r2_test = r2_score(testy, p4(testx))

print ("The R-squared of the test data is: ", r2_test)

r2_training = r2_score(np.array(trainY), p4(np.array(trainX)))

print("The R-squared for the training data is: ", r2_training)

if (r2_training > 0.75):
    print("The", degree, "degree polynomial is a strong fit!" )
