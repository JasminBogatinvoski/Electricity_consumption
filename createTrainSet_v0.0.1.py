import pandas as pd

new6 = pd.read_csv('train.csv', usecols=['dates', 'sec', 'pall'])
new7 = pd.read_csv('train7.csv', usecols=['dates', 'sec', 'pall'])
new8 = pd.read_csv('train8.csv', usecols=['dates', 'sec', 'pall'])
new9 = pd.read_csv('train9.csv', usecols=['dates', 'sec', 'pall'])
new10 = pd.read_csv('train10.csv', usecols=['dates', 'sec', 'pall'])
new11 = pd.read_csv('train11.csv', usecols=['dates', 'sec', 'pall'])
new12 = pd.read_csv('train12.csv', usecols=['dates', 'sec', 'pall'])
new13 = pd.read_csv('train13.csv', usecols=['dates', 'sec', 'pall'])

frames = [new6, new7, new8, new9, new10, new11, new12, new13]
new = pd.concat(frames)

new.to_csv('trainPall.csv', sep=',')

print(new)

