import math 
import random
import os

class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self,name):
        self.name= name
    def get_data(self):
        series=[]
        try:
            file=open(self.name, 'r')
        except:
            raise ExamException('File non apribile')
        
        lines=file.read().split('\n')[1:]
        for line in lines:
            elemento=line.split(',')
            series.append(elemento)
        for lista in series:
            if len(lista)==2 and lista[1]!='':
                lista[1]=int(lista[1])
        file.close()
        return series[:-1]

def compute_var(time_series, first_year, last_year):
    data=time_series
    dic={}
    medie=[]
    for current in range(first_year, last_year+1):
        incr=0
        somma=0
        current=str(current)
        for item in data:
            if current in item[0]:
                print(item)
                somma+=item[1]
                incr+=1
        if incr !=0:
            media=somma/incr
            medie.append(media)
    #return medie
        for i in range(0,len(medie)-1):
            diff=medie[i+1]-medie[i]
            dic[current]=diff
    return dic


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
#print(time_series)
dictionary=compute_var(time_series, 1949,1960)
print(dictionary)




