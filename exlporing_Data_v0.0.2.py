import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time

starttime= time()
from reading import read_sm_csv_by_day_sequence
dictionaryData, keys = read_sm_csv_by_day_sequence(1, 13, '01-01-2013', '01-02-2013')
for x in range(0, len(keys)):
    powerAll = dictionaryData[keys[x]].iloc[:, 1].values
    plt.figure(x)
    plt.plot(np.arange(start=0, stop=len(powerAll), step=1), powerAll)
    plt.xticks(np.linspace(0, np.size(powerAll), 9, endpoint=True),
           ['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
    plt.title('Power consumption, date:  ' + str(x + 1))
    plt.xlabel('Time of day')
    plt.ylabel('pALL')
    plt.savefig('PowerALL_Consumption_day_by_day/January/' + str(x + 1) + '-01-2013.png')
    plt.close(x)
endtime = time()

print('Total time execution: ', endtime-starttime)
print('>>>>>>>FINISH>>>>>>>>>')