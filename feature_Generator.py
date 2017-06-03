import pandas as pd
import numpy as np
from reading import read_sm_csv_by_day_sequence
from time import time

def onOff(pall):
    ThA = 30
    ThT = 30
    diff = np.abs(np.subtract(pall[1:], pall[0:-1]))
    onOffFeature = np.zeros((diff.shape[0],))
    k=1
    for x in diff:
            if x > ThA:
                for y in diff[k+1:(k+ThT)]:
                    if y > ThA:
                        onOffFeature[k] = 1
                    else:
                        onOffFeature[k] = 0
                        break
            k=k+1
    return onOffFeature

def SAD_Total(x1,x2,x3):
    SA = np.abs(np.subtract(x1, x2))+np.abs(np.subtract(x1, x3))+np.abs(np.subtract(x2, x3))
    return SA

def SAD_partial(x1,x2,x3):
    SA = np.abs(np.subtract(x1, x2))+np.abs(np.subtract(x1, x3))
    return SA

startTime = time()
d = {}
frameSize = 420
data, days = read_sm_csv_by_day_sequence(1, 6, '01-06-2012', '01-07-2012')

frames = []

for x in range(0, np.size(days)):
    v = np.full((data[days[x]].shape[0], 1), fill_value=days[x])
    t = np.arange(start=0, stop=v.shape[0], step=1)
    X = pd.DataFrame(v[:], t, columns=['dates']).reset_index()
    data[days[x]]['index'] = t

    dates = X.dates
    index = X['index']

    ####################### features dates and index

    pom = data[days[x]]['pall']
    pallMean = pd.rolling_mean(pom, window=frameSize)
    pallMean.name = 'pallMean'
    pallMean.iloc[0:frameSize] = pom.iloc[0:frameSize].sum()/frameSize

    pallMin = pd.rolling_min(pom, window=frameSize)
    pallMin.name = 'pallMin'
    pallMin.iloc[0:frameSize] = pom.iloc[0:frameSize].min()

    pallMax = pd.rolling_max(pom, window=frameSize)
    pallMax.name = 'pallMax'
    pallMax.iloc[0:frameSize] = pom.iloc[0:frameSize].max()

    pallCorr = pd.rolling_corr(pom, window=frameSize)
    pallCorr.name = 'pallCorr'
    pallCorr.iloc[0:frameSize] = np.ones((frameSize, ), dtype='int32')

    pallStd = pd.rolling_std(pom, window=frameSize)
    pallStd.name = 'pallStd'
    pallStd.iloc[0:frameSize] = np.std((pom[0:frameSize], pallMean[0:frameSize]))

    pallCov = pd.rolling_cov(pom, window=frameSize)
    pallCov.name = 'pallCov'
    #pallCov.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')
    pallCov.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.cov(pom[0:frameSize]))

    pallVar = pd.rolling_var(pom, window=frameSize)
    pallVar.name = 'pallVar'
    pallVar.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.var(pom[0:frameSize]))

    onOffPall = onOff(pom)
    onOffPallDataFrame = pd.DataFrame(data=onOffPall, columns=['onOffPall'])
    #################### features pall

    pom1 = data[days[x]]['pl1']
    pl1Mean = pd.rolling_mean(pom1, window=frameSize)
    pl1Mean.name = 'pl1Mean'
    pl1Mean.iloc[0:frameSize] = pom1.iloc[0:frameSize].sum() / frameSize

    pl1Min = pd.rolling_min(pom1, window=frameSize)
    pl1Min.name = 'pl1Min'
    pl1Min.iloc[0:frameSize] = pom1.iloc[0:frameSize].min()

    pl1Max = pd.rolling_max(pom1, window=frameSize)
    pl1Max.name = 'pl1Max'
    pl1Max.iloc[0:frameSize] = pom1.iloc[0:frameSize].max()

    pl1Corr = pd.rolling_corr(pom1, window=frameSize)
    pl1Corr.name = 'pl1Corr'
    pl1Corr.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')

    pl1Std = pd.rolling_std(pom1, window=frameSize)
    pl1Std.name = 'pl1Std'
    pl1Std.iloc[0:frameSize] = np.std((pom1[0:frameSize], pallMean[0:frameSize]))

    pl1Cov = pd.rolling_cov(pom1, window=frameSize)
    pl1Cov.name = 'pl1Cov'
    pl1Cov.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')
    pl1Cov.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.cov(pom1[0:frameSize]))

    pl1Var = pd.rolling_var(pom1, window=frameSize)
    pl1Var.name = 'pl1Var'
    pl1Var.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.var(pom1[0:frameSize]))

    onOffPl1 = onOff(pom1)
    onOffPl1DataFrame = pd.DataFrame(data=onOffPl1, columns=['onOffPl1'])
    ########################## features p1


    pom2 = data[days[x]]['pl2']

    pl2Mean = pd.rolling_mean(pom2, window=frameSize)
    pl2Mean.name = 'pl2Mean'
    pl2Mean.iloc[0:frameSize] = pom2.iloc[0:frameSize].sum() / frameSize

    pl2Min = pd.rolling_min(pom2, window=frameSize)
    pl2Min.name = 'pl2Min'
    pl2Min.iloc[0:frameSize] = pom2.iloc[0:frameSize].min()

    pl2Max = pd.rolling_max(pom2, window=frameSize)
    pl2Max.name = 'pl2Max'
    pl2Max.iloc[0:frameSize] = pom2.iloc[0:frameSize].max()

    pl2Corr = pd.rolling_corr(pom2, window=frameSize)
    pl2Corr.name = 'pl2Corr'
    pl2Corr.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')

    pl2Std = pd.rolling_std(pom2, window=frameSize)
    pl2Std.name = 'pl2Std'
    pl2Std.iloc[0:frameSize] = np.std((pom2[0:frameSize], pallMean[0:frameSize]))

    pl2Cov = pd.rolling_cov(pom2, window=frameSize)
    pl2Cov.name = 'pl2Cov'
    pl2Cov.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')
    pl2Cov.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.cov(pom2[0:frameSize]))

    pl2Var = pd.rolling_var(pom2, window=frameSize)
    pl2Var.name = 'pl2Var'
    pl2Var.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.var(pom2[0:frameSize]))

    onOffPl2 = onOff(pom2)
    onOffPl2DataFrame = pd.DataFrame(data=onOffPl2, columns=['onOffPl2'])
    ########################## features p2

    pom3 = data[days[x]]['pl3']

    pl3Mean = pd.rolling_mean(pom3, window=frameSize)
    pl3Mean.name = 'pl3Mean'
    pl3Mean.iloc[0:frameSize] = pom3.iloc[0:frameSize].sum() / frameSize

    pl3Min = pd.rolling_min(pom3, window=frameSize)
    pl3Min.name = 'pl3Min'
    pl3Min.iloc[0:frameSize] = pom3.iloc[0:frameSize].min()

    pl3Max = pd.rolling_max(pom3, window=frameSize)
    pl3Max.name = 'pl3Max'
    pl3Max.iloc[0:frameSize] = pom3.iloc[0:frameSize].max()

    pl3Corr = pd.rolling_corr(pom3, window=frameSize)
    pl3Corr.name = 'pl3Corr'
    pl3Corr.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')

    pl3Std = pd.rolling_std(pom3, window=frameSize)
    pl3Std.name = 'pl3Std'
    pl3Std.iloc[0:frameSize] = np.std((pom3[0:frameSize], pallMean[0:frameSize]))

    pl3Cov = pd.rolling_cov(pom3, window=frameSize)
    pl3Cov.name = 'pl3Cov'
    pl3Cov.iloc[0:frameSize] = np.ones((frameSize,), dtype='int32')
    pl3Cov.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.cov(pom3[0:frameSize]))

    pl3Var = pd.rolling_var(pom3, window=frameSize)
    pl3Var.name = 'pl3Var'
    pl3Var.iloc[0:frameSize] = np.full((frameSize,), fill_value=np.var(pom3[0:frameSize]))

    onOffPl3 = onOff(pom3)
    onOffPl3DataFrame = pd.DataFrame(data=onOffPl3, columns=['onOffPl2'])
    ########################## features p3

    Sad_all_phase = SAD_Total(pom1, pom2, pom3)
    Sad_all_phasePall = pd.DataFrame(data=Sad_all_phase, columns=['Sad_all_phase'])

    SAD_partial1 = SAD_Total(pom, pom2, pom3)
    SAD_partial1DataFrame = pd.DataFrame(data=SAD_partial1, columns=['Sad_al1'])

    SAD_partial2 = SAD_Total(pom, pom1, pom3)
    SAD_partial2DataFrame = pd.DataFrame(data=SAD_partial2, columns=['Sad_al2'])

    SAD_partial3 = SAD_Total(pom, pom1, pom2)
    SAD_partial3DataFrame = pd.DataFrame(data=SAD_partial3, columns=['Sad_al3'])

    newDataFrame = pd.concat([dates, index, pallMean, pallMin, pallMax, pallCorr, pallStd, pallCov, pallVar, onOffPallDataFrame, Sad_all_phasePall,
                              pl1Mean, pl1Min, pl1Max, pl1Corr, pl1Std, pl1Cov, pl1Var,  onOffPl1DataFrame, SAD_partial1DataFrame,
                              pl2Mean, pl2Min, pl2Max, pl2Corr, pl2Std, pl2Cov, pl2Var,  onOffPl2DataFrame, SAD_partial2DataFrame,
                              pl3Mean, pl3Min, pl3Max, pl3Corr, pl3Std, pl3Cov, pl3Var,  onOffPl3DataFrame, SAD_partial3DataFrame
                              ], axis=1)
    frames.append(newDataFrame)


featuresTable = pd.concat(frames)
featuresTable.to_csv('featuresTable6.csv')
endTime = time()
print(endTime-startTime)