import pandas as pd
import glob
import os
import numpy as np
import datetime

def read_occupancy_csv(season,number):
    filePath = 'occupancy/'+str(0)+str(number)+'_occupancy_csv/'+str(0)+str(number)
    if season == 'winter':
        filePath += '_winter.csv'
        seas = pd.read_csv(filePath)
    else:
        if season == 'summer':
            filePath += '_summer.csv'
            seas = pd.read_csv(filePath)
        else:
            return 0
    return seas

def read_plugs_csv(houseNumber,plugNumber):
    filePath = 'plugs/' + str(0) + str(houseNumber) + '_plugs_csv/' + str(0) + str(houseNumber)+'/'+str(0) + str(plugNumber)
    allfiles = glob.glob(os.path.join(filePath, "*.csv"))
    d={}
    for file_ in allfiles:
        df = pd.read_csv(file_, index_col=None, header=None)
        date = file_
        date = date[date.rfind('201'):(date.rfind('201')+len('2012-06-02'))]
        d[date] = df.as_matrix()
        d[date] = d[date].squeeze()
    big_frame = pd.DataFrame(data=d)
    return big_frame

def read_sm_csv(houseNumber, month):
    filePath = 'sm/' + str(0) + str(houseNumber) + '_sm_csv/' + str(0) + str(houseNumber) + '/' + str(0) + str(month)
    allfiles = glob.glob(os.path.join(filePath, "*.csv"))
    np_array_list = []
    np_array_name = []
    for file_ in allfiles:
        df = pd.read_csv(file_, index_col=None, header=None)
        date = file_
        date = date[date.rfind('201'):(date.rfind('201')+len('2012-06-02'))]
        np_array_list.append(df.as_matrix())
        np_array_name.append(date)
    big_frame = pd.DataFrame(data=np_array_list[0],  columns=['pall', 'pl1', 'pl2', 'pl3', 'cn', 'cl1', 'cl2', 'cl3',
                                                              'vl1', 'vl2', 'vl3', 'pl2l1', 'pl3l1', 'pcvl1',
                                                              'pcvl2', 'pcvl3'])
    for x in np_array_list:
        big_frame1 = pd.DataFrame(x, columns=['pall', 'pl1', 'pl2', 'pl3', 'cn', 'cl1', 'cl2', 'cl3', 'vl1', 'vl2',
                                              'vl3', 'pl2l1', 'pl3l1', 'pcvl1',
                                              'pcvl2', 'pcvl3'])
        big_frame = big_frame.append(big_frame1, ignore_index=True)
    return big_frame

def read_sm_csv_by_day(houseNumber, month, startDate, endDate, date):
    start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
    end = datetime.datetime.strptime(endDate, "%d-%m-%Y")
    date = datetime.datetime.strptime(date, "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
    dates = []
    for date in date_generated:
        dates.append(date.strftime("%d-%m-%Y"))
    d = {}
    data = read_sm_csv(houseNumber, month)
    n = np.size(data)
    X = np.linspace(0, n, 60 * 60 * 24) # sec * min *hours
    nx = np.size(X)
    for x in range(0, np.size(dates)):
        p = data.iloc[x * nx:(x + 1) * nx - 1]
        key = dates[x]
        d[key] = p.reset_index()
    key = date.strftime("%d-%m-%Y")
    return d[key] #vrakja dataframe za tekoven den prosleden vo date
def read_sm_csv_by_day_sequence(houseNumber, month, startDate, endDate):
    start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
    end = datetime.datetime.strptime(endDate, "%d-%m-%Y")

    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]
    dates = []
    for date in date_generated:
        dates.append(date.strftime("%d-%m-%Y"))
    d = {}
    data = read_sm_csv(houseNumber, month)
    n = np.size(data)
    X = np.linspace(0, n, 60 * 60 * 24)
    nx = np.size(X)
    for x in range(0, np.size(dates)):
        p = data.iloc[x * nx:(x + 1) * nx - 1]
        key = dates[x]
        d[key] = p.reset_index()
    return d, dates #vrakja recnik od dataframeovi i negovite klucevi so indeks koj odgovoara na opsegot na datumi
def read_wheater_data_daily():
    return pd.read_csv('wheater_data\weather_data_daily_appended_v00.csv', sep=',')

def read_wheater_data_hourly():
    return pd.read_csv('wheater_data\weather_data_hourly_appended_v00.csv', sep=',')

def read_working_data():
    return pd.read_csv('workingDaysData.csv', sep=',')
