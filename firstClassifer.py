import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time

startTime=time()

data = pd.read_csv('featuresTable6.csv', nrows=8*86398, skiprows=[1*86398, 3*86398])
X_train = data.iloc[:, [3, 4, 5, 6, 7]].values

from sklearn.cluster import KMeans
wcs = []
t = np.arange(start=1, stop=11, step=1)
for x in range(1, 11):
    classifier = KMeans(n_clusters=x, init='k-means++', random_state=42)
    classifier.fit(X_train)
    wcs.append(classifier.inertia_)
endTime = time()
print("vremeto na izvrasuvanje na programata e: ", endTime-startTime)
