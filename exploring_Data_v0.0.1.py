import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from reading import read_sm_csv_by_day_sequence
dictionaryData, keys = read_sm_csv_by_day_sequence(1, 6, "01-06-2012", "05-06-2012")
from sklearn.cluster import KMeans
for x in range(0, len(keys)):
    data = dictionaryData[keys[x]].iloc[:, [1, 2, 3, 4]].values
    wcss = []
    for i in range(1, 12):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=20, random_state=0)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    #kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=400, random_state=0)
    #y_pred = kmeans.fit_predict(data)
    plt.figure(x)
    plt.plot(range(1, 12), wcss)
    plt.title('The Elbow method: '+str(x+1))
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.savefig('slikiKmeans/'+str(x+1)+'-06-2012.png')
    #plt.show()
