from reading import *
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd

dictionaryData, keys = read_sm_csv_by_day_sequence(1, 6, "01-06-2012", "05-06-2012")
n = np.size(dictionaryData[keys[0]])/17
X = np.linspace(0, n, n, endpoint=True)
data = dictionaryData[keys[0]]
#data1 = dictionaryData[keys[0]]
#data2 = dictionaryData[keys[0]]
#data3 = dictionaryData[keys[0]]
power = data['pall']
currentl1 = data['cl1']
voltagel1 = data['vl1']
powerl1 = data['pl1']
phaseCurrentVoltagel1 = data['pcvl1']

plt.figure(figsize=(120, 50), dpi=50)
#plt.subplot(221)
#plt.plot(X,power, color="red", linewidth=0.7, label = 'pall day 01-06-2017')
#plt.xticks(np.linspace(0, np.size(power), 9, endpoint=True), [ '00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00','00:00'])
#plt.xlim(np.min(X)*0.98, np.max(X))
#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data', 0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data', 0))
#plt.legend(loc='upper left', frameon=False)
plt.subplot(221)
plt.plot(X, currentl1, color="green", linewidth=0.7, label = 'current line 1')
plt.xticks(np.linspace(0, np.size(currentl1), 9, endpoint=True),
           ['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
plt.xlim(np.min(X) * 0.98, np.max(X))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.legend(loc='upper left', frameon=False)

plt.subplot(222)
plt.plot(X, voltagel1,color="blue", linewidth=0.7, label = 'voltage line 1')
plt.xticks(np.linspace(0, np.size(voltagel1), 9, endpoint=True),
           ['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
plt.xlim(np.min(X) * 0.98, np.max(X))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.legend(loc='upper left', frameon=False)

plt.subplot(223)
plt.plot(X, powerl1, color="cyan", linewidth=0.7, label = 'power line 1')
plt.xticks(np.linspace(0, np.size(powerl1), 9, endpoint=True),
           ['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
plt.xlim(np.min(X) * 0.98, np.max(X))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.legend(loc='upper left', frameon=False)

plt.subplot(224)
plt.plot(X, phaseCurrentVoltagel1,color="magenta", linewidth=0.7, label = 'currentvoltagePhase line 1')
plt.xticks(np.linspace(0, np.size(phaseCurrentVoltagel1), 9, endpoint=True),
           ['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
plt.xlim(np.min(X) * 0.98, np.max(X))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
plt.legend(loc='upper left', frameon=False)


#plt.plot(X,data1, color="green", linewidth=1.0)
#plt.plot(X,data2, color="red", linewidth=0.6)
#plt.plot(X,data3)
plt.show()
plt.figure(figsize=(120, 50), dpi=50)
plt.plot(X, data['pall'], color='red',label='pall day 1')
plt.xticks(np.linspace(0, np.size(data['pall']), 9, endpoint=True),
['00:00 ', '03:00 ', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00', '00:00'])
plt.show()

