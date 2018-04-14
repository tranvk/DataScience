from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from pylab import *
import pylab as pl

"""
*Why use PCA: Reduce multi-dimensional data down to fewer dimensions
*Example: black & white image with X, Y, Brightness axes -> PCA -> image compression/facial recognition
*How: distills information that contributes most to the variance of data set
"""


#load iris data set, which as 4 dimensions for 3 different kinds of iris flowers
iris = load_iris()

numSamples, numFeatures = iris.data.shape

#4D -> 2D by projecting it to 2 orthogonal 4D vectors which are basis of new 2D projection
X = iris.data
pca = PCA(n_components = 2, whiten = True).fit(X)
X_pca = pca.transform(X)

colors = cycle('rgb')

target_ids = range(len(iris.target_names))
pl.figure()

for i,c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target -- i, 0], X_pca[iris.target == i, 1], c=c, label=label)

pl.legend()
pl.show()
