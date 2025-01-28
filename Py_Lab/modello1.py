import numpy as  np
import matplotlib.pyplot as plt
import os
import random

"""
Modello: rappresentazione semplificata della realtà, costruito per analizzare o predire il comportamento di un sistema o fenomeno
    -Il modello ha sempre bisogno di dati iniziali
    - Modello fisico
        cerca do spiegare il comportamento di un fenomeno basandosi su principi fondamentali
        Enfasi sul cercare di CAPIRE il fenomeno
    -Modello statistico
        Basati sui dati e cerca di identificare schemi o relazioni nei dati 
        Enfasi sul predirre dati futuri
    I modelli approssimmano i dati dati ad una funzione per poi predirre dati futuri
A cosa servono i modelli:
    Per fare Predizioni: predictions

Modelli "a finestra" di lunghezza n
    Le vendite ad esempio, nel mese t+1 saranno date da:
        -le vendite al mese t + la media della variazione(differenza tra t e t-1) degli n mesi precedenti
        

class fTrendModel():
    def predict(data):
        if type(data)!=list:
            raise TypeError("Damn son! That's not a list...")
        summ=0
        j=0
        for i in range(len(data)-1):
            prev=data[i]
            summ+=data[i+1]-prev
            j+=1
        Predict=data[-1]+summ/j
        return Predict
    
#Fatto dalla prof:
class fTrendModelProf():
    def predict(data):
        if len(data)<=1:
            raise Exception("Lista troppo corta")
        predict=0
        if type(data)!=list:
            raise TypeError("Damn son! That's not a list...")
        prev=None
        for item in data:
            if prev is not None:
                predict+= item-prev
            prev=item
        predict/=(len(data)-1)
        predict+=data[-1]

#datax=[2,6]
#mymodel=TrendModel()
#print(mymodel.predict(datax))


Fittiamo un modello:
    "Specializzare" un modello per i dati forniti ossia adattare il modello per rappresentare meglio i dati che ho
    Come fittare un modello:
        Punto per punto si cerca di MINIMIZZARE la distanza tra i dati e la curva da noi proposta.
        I coefficenti della funzione che minimizzano l'errore sono quelli che userò per calcolare l'errore dai dati reali ossia l'efficienza del mio modello

Una classe Base che abbia funzioni utili per tutti  i modelli e poi i vari modelli come sottoclassi di esso
"""
"""
class fModel():
    def fit(self,data):
        raise NotImplementedError
    def predict(self,data):
        raise  NotImplementedError
    def average_var(self, data, window):
        summ=0
        j=0
        for i in range(len(data)-window):
            prev=data[-i]
            summ+=data[-(i+1)]-prev
            j+=1
        return summ/j
            
class fModelTrend(fModel):
    def __init__(self, window=3):
        self.window=window
    def predict(self, data):
        if type(data)!=list:
            raise TypeError("Damn son! That's not a list...")
        return data[-self.window]+self.average_var(data, self.window)

class fFitTrendModel(fModelTrend):
    def fit(self, data,dim):
        self.history_var=self.average_var(data,dim)
    def predict(self, data):
        return super().predict(data) + self.history_var
"""
#-------------------------------------------------------------------------------------------------------
class Model:
    def fit(self, data):
        raise NotImplementedError
    
    def predict(self, data):
        raise NotImplementedError
    
    def average_var(self, data, window):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Data must be a list of numbers.")
        if len(data) <= window:
            raise ValueError("Data length must be greater than window size.")
        summ = 0
        for i in range(len(data) - window, len(data)):
            summ += data[i] - data[i-1] 
        return summ / window

class ModelTrend(Model):
    def __init__(self, window=3):
        self.window = window
    
    def predict(self, data):
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        avg_var = self.average_var(data, self.window)
        return data[-1] + avg_var

class FitTrendModel(ModelTrend):
    def average_var(self, data, window):
        upto=len(data)-window 
        val=[]
        prev=None
        for i, item in enumerate(data):
            if i==upto:
                break
            if prev is not None:            
                val.append(item - prev)
            prev = item
        return int(sum(val)/(len(val)))

    def fit(self, data, window):
        self.history_var = self.average_var(data, window)
        #self.window_val=super().average_var(data, window)
    
    def predict(self, data):
        return data[-1] +self.history_var#+self.window_val)/2

data=[8,19,31,41,50,52,60,67,72,72]

# FitTrendModel 
fit_model = FitTrendModel()
data1=data.copy()
for i in range(10):
    model_trend = ModelTrend(window=3)
    prediction_trend = model_trend.predict(data)
    print("ModelTrend Prediction:", prediction_trend)
    data.append(prediction_trend)
    #-----
    fit_model.fit(data1, window=3)
    prediction = fit_model.predict(data1)
    print("FitTrendModel Prediction:", prediction)
    data1.append(prediction)
# Generando altri 10 valori predetti da questo modello per dati futuri
plt.plot(data+ [prediction_trend], color='tab:blue')
plt.plot(data1+ [prediction], color='tab:red')
plt.show()

