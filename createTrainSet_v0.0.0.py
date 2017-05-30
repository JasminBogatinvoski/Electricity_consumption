from reading import *
import pandas as pd
import numpy as np

keys = []

#dictionaryData6, keys6 =  read_sm_csv_by_day_sequence(1, 6, "01-06-2012", "01-07-2012")
#dictionaryData7, keys7 =  read_sm_csv_by_day_sequence(1, 7, "01-07-2012", "01-08-2012")
#dictionaryData8, keys8 =  read_sm_csv_by_day_sequence(1, 8, "01-08-2012", "01-09-2012")
#dictionaryData9, keys9 =  read_sm_csv_by_day_sequence(1, 9, "01-09-2012", "01-10-2012")
#dictionaryData10, keys10 =  read_sm_csv_by_day_sequence(1, 10, "01-10-2012", "01-11-2012")
#dictionaryData11, keys11 =  read_sm_csv_by_day_sequence(1, 11, "01-11-2012", "01-12-2012")
#dictionaryData12, keys12 =  read_sm_csv_by_day_sequence(1, 12, "01-12-2012", "01-01-2013")
dictionaryData13, keys13 =  read_sm_csv_by_day_sequence(1, 13, "01-01-2013", "01-02-2013")

train = pd.concat(dictionaryData13)
print(type(train))
train.to_csv('train13.csv', sep=',')
