#import numpy as  np
#import matplotlib as mpl
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
        
"""
class TrendModel():
    def predict(data):
        summ=0
        j=0
        for i in range(len(data)-1):
            prev=data[i]
            summ+=data[i+1]-prev
            j+=1
        Predict=data[-1]+summ/j
        return Predict
datax=[50,52,60]
print(TrendModel.predict(datax))
