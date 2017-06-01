import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time
from reading import read_sm_csv_by_day_sequence

startTime = time()

frame_size = 480  #rolling horizon of 8 minutes e dovolno golem
dictionaryData, keys = read_sm_csv_by_day_sequence(1, 7, "01-08-2012", "01-09-2012")

new = dictionaryData
k = 62
for key in keys:
    figName = ''
    plt.figure(k)
    X = new[key].pall.values
    t = np.arange(0, X.shape[0])
    D = pd.Series(X, t)
    data_ma=pd.rolling_mean(D, frame_size)
    data_ma.iloc[0:frame_size] = D.iloc[0:frame_size].sum()/frame_size
    data_ma_std = pd.rolling_std(D, window=frame_size)
    data_ma_std.iloc[0:frame_size] = np.std((D[0:frame_size], data_ma[0:frame_size]))
endTime = time()
print('Vreme na izvrasuvanje na skriptata: ', endTime-startTime)

#plt.plot(t, X, c='red')
#plt.plot(t, data_ma)
#plt.plot(t,data_ma_std,'green')
#plt.savefig('Reports\ma_reports\Eight_min_rolling_horizon_standard_deviation.png')
#plt.show()
#plt.plot(t, X, c='red')
#plt.plot(t, data_ma)
#plt.plot(t, data_ma_std, 'green')
#figName = 'Reports\ma_reports' + '\Eight_min_rolling_horizon_standard_deviation'+str(k)+'.png'
#plt.savefig(figName)
#k=k+1