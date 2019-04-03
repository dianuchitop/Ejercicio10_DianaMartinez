import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as signal

#D2008=pd.read_csv("clean_transacciones2008.txt",delimiter=";")
#D2009=pd.read_csv("clean_transacciones2009.txt",delimiter=";")
#D2010=pd.read_csv("clean_transacciones2010.txt",delimiter=";")
#
#D2008["datetime"]=pd.to_datetime(D2008["datetime"])
##D2008.set_index(["datetime"],inplace=True)



def importplotdatos(filename):
    datos=pd.read_csv(filename,delimiter=";")
    datos["datetime"]=pd.to_datetime(datos["datetime"])
    name=filename.split(".")[0]
    plt.figure(figsize=(12,6))
    plt.plot(datos["datetime"],datos["monto"])
    plt.xticks(rotation="vertical")
    plt.title(name.split("_")[1])
    plt.savefig(name+"_plot.png")
    
    
    return datos


D2008=importplotdatos("clean_transacciones2008.txt")
D2009=importplotdatos("clean_transacciones2009.txt")
D2010=importplotdatos("clean_transacciones2010.txt")
    
def plot_filtro(N,Wn,datos,tit,nam):
#N  = 2    # Orden del filtro
#Wn = 0.01 # Corte de frecuancia
    B, A = signal.butter(N, Wn)
    monto_filt = signal.filtfilt(B,A, datos["monto"].values)
    plt.figure(figsize=(12,6))
    plt.plot(datos["datetime"],datos["monto"])
    plt.plot(datos["datetime"],monto_filt,c="r")
    plt.xticks(rotation="vertical")
    
    plt.title(tit)
    plt.savefig(nam)
    
    
    
    
N=3    
Wn=0.00005
plot_filtro(N,Wn,D2008,"transacciones 2008 filtradas","T2008_filt.png")
plot_filtro(N,Wn,D2009,"transacciones 2009 filtradas","T2009_filt.png")
plot_filtro(N,Wn,D2010,"transacciones 2010 filtradas","T2010_filt.png")