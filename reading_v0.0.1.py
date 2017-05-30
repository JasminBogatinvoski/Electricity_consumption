import pandas as pd
import glob
import os
import numpy as np


def read_occupancy_csv(season,number):
    filePath = 'occupancy/'+str(0)+str(number)+'_occupancy_csv/'+str(0)+str(number)
    if season == 'winter':
        filePath += '_winter.csv'
        seas = pd.read_csv(filePath)
    else:
        filePath += '_summer.csv'
        if season == 'summer':
            seas = pd.read_csv('01_summer.csv')
        else:
            return 0
    return seas

def read_plugs_csv(houseNumber,plugNumber):
    filePath = 'plugs/' + str(0) + str(houseNumber) + '_plugs_csv/' + str(0) + str(houseNumber)+'/'+str(0) + str(plugNumber)
    allfiles = glob.glob(os.path.join(filePath, "*.csv"))
    np_array_list = []
    np_array_name = []
    for file_ in allfiles:
        df = pd.read_csv(file_, index_col=None, header=0)
        date = file_
        date=date[date.rfind('201'):(date.rfind('201')+len('2012-06-02'))]
        np_array_list.append(df.as_matrix())
        np_array_name.append(date)
    np_array_name.append('bezveze')
    np_array_list.append(np_array_name)
    big_frame = pd.DataFrame(np_array_list, index=np_array_name)
    big_frame = big_frame.iloc[0:(len(big_frame)-1)]
    big_frame.columns=['Podatoci']
    d={}
    for x in range(0,len(np_array_name)-1):
        d[np_array_name[x]] = list(big_frame.Podatoci.iloc[x][0:])
    print(d)
    return big_frame

def read_wheater_data_daily():
    return pd.read_csv('wheater_data\wheater_daily.csv', sep=',')

def read_wheater_data_hourly():
    return pd.read_csv('wheater_data\wheater_hourly.csv', sep=',')

d = pd.DataFrame()
d = read_plugs_csv(1,1)
#print(d)
