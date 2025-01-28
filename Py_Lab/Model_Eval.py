import numpy as np
import matplotlib.pyplot as plt
import random
import os


"""
Valutare un modello:
    -C'è una differenza tra fare aderire ai dati alla nostra curva e prevedere bene i dati futuri
    - Per un modello preditivo si dividono i dati in due parti
        Una parte per il "fittaggio" anche detto training dataset, circa il 70%- 80% dei dati
        l'altra parte dei dati per testare il modello,  anche detto evaluation dataset, il 20%-30% di dati rimanenti
        A volte si usa anche una terza parte detto validation dataset che si usa nel "training" del modello per testarlo man mano e migliorarlo
    Possibili risultati di un fit:
        Underfit: Non approssima bene i dati, errore grosso
        Ok: La nostra curva ha un errore piccolo, non passa per ogni punto ma lo approssima
        Overfit: Il modello passa esattamente per i dati originali, errore nullo sul datasett originali. Causa problemi
    Il confronto tra le predizioni e dati veri si fa calcolando la differenza tra la predizione e il dato di test, calcolando cosi l'errore del prediction
    La media degli errori sul evaluation dataset ci dà una idea generale sull'andamento del modello
"""
class Model:
    def fit(self, data):
        raise NotImplementedError
    
    def predict(self, data):
        raise NotImplementedError
    
    def average_var(self, data):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Data must be a list of numbers.")
        val=[]
        prev=None
        for item in data:
            if prev is not None:            
                val.append(item - prev)
            prev = item
        return sum(val)/len(val)
    def evaluate(self, data):
        error=0
        length=int(len(data)*0.7)
        storici=data[:length]
        evaldata=data[length:]
        try:
            self.fit(storici)
        except:
            print("No fit")
        finally:
            j=len(evaldata)-self.window
            for i in range(j):
                pred=self.predict(evaldata[i:i+self.window])
                error+=abs(pred-evaldata[i+self.window])
                print("Pred: ", pred)
            return (error/j)

class ModelTrend(Model):
    def __init__(self,window):
        self.window = window
    
    def predict(self, data):
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        avg_var = self.average_var(data)
        return data[-1] + avg_var

class FitTrendModel(ModelTrend):
    def fit(self, data):
        self.history_var = self.average_var(data)
    
    def predict(self, data):
        return data[-1] + self.history_var

data=[1,2,3,4,5,6,7,8, 9,10.5,11.5,11.2]
#data=[8,19,31,41,50,52,60,67,72,72,67,72]
fitmodel=FitTrendModel(2)
#trendmodel=ModelTrend(3)
#print("Prediction is: ", predict)
eval=fitmodel.evaluate(data)
#eval1=trendmodel.evaluate(data)
print(f"Error is: {eval}")
#print(f"No fit error is: {eval1}")
#plt.plot(data+eval,color="tab:red")
#plt.show()

"""
Per esame:
    creare class ExamException(Exception): pass
    che si chiamerà al posto dei normali exception

"""