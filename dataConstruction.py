from reading import read_plugs_csv
import pandas as pd
from time import time

statTime=time()
plugs = read_plugs_csv(1, 7) # to be chanhed
k = 0
l = []
vrednosti = []
sekundi = []
dict = {}

for j in plugs.columns.values:
    for x in range(0, 86399):
        l.append(j)
        vrednosti.append(plugs.iloc[x, k])
        sekundi.append(x)
    k=k+1

midTime = time()
print(midTime-statTime)
dict['dates'] = l
dict['Freezer'] = vrednosti
dict['sec'] = sekundi

dataFrame = pd.DataFrame(data=dict)
dataFrame.to_csv('ured7_kukja1.csv', sep=',')

#plugsToDo = plugs.transpose()
#new = plugsToDo.reset_index()
#new = new.rename(columns={'index': 'dates'})
#new1 = pd.read_csv('train.csv', sep=',')
#new2 = pd.read_csv('train7.csv', sep=',')
#new3 = pd.read_csv('train8.csv', sep=',')
#new4 = pd.read_csv('train9.csv', sep=',')
#new5 = pd.read_csv('train10.csv', sep=',')
#new6 = pd.read_csv('train11.csv', sep=',')
#new7 = pd.read_csv('train12.csv', sep=',')
#new8 = pd.read_csv('train13.csv', sep=',')
#frames = [new1, new2, new3, new4, new5, new6, new7, new8]
#result = pd.concat(frames)
#result.to_csv('pomosno.csv', sep=',')

endTime=time()
print(endTime-statTime)