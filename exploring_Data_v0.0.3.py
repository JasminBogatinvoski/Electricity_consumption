import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from reading import read_sm_csv_by_day_sequence
def daySeparator(day, dates, rang):
    chunkSize = day[dates[0]].iloc[:, 0].size//rang + 1
    d = {}
    for x in range(0, rang):
        d[x] = day[dates[0]].iloc[x*chunkSize:(x+1)*chunkSize, :]
    return d
day, dates = read_sm_csv_by_day_sequence(1, 6, '02-06-2012', '03-06-2012')
rang = 4
q = daySeparator(day, dates, rang)
for t in range(0, rang):
    ws = []
    for x in range(1, 11):
        classifier = KMeans(n_clusters=x, init='k-means++', random_state=42)
        classifier.fit(q[t].iloc[:, [0, 15]].values)
        ws.append(classifier.inertia_)
    plt.figure(t)
    plt.plot(np.arange(start=1, stop=11, step=1), ws)
    plt.show()
# interesni slucuvanja ima za rang=12, bilo koj den dava ist grafik za site klasi