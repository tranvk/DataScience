from numpy import random, array
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float

#generate fake income and age clusters for N people in k clusters
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float(N)/k

    X = []

    for i in range (k):
        incomeCentroid = random.uniform(20000, 200000)
        ageCentroid = random.uniform(20, 70)
        for j in range (int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000), random.normal(ageCentroid, 2)])
    X = array(X)

    return X


data = createClusteredData(100, 9)

model = KMeans(n_clusters = 5)

model = model.fit(scale(data))

print(model.labels_)

plt.figure(figsize = (8,6))
plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
plt.show()
