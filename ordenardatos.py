import pandas as pd
import numpy as np


def limpiardatos(filename):
    datos = pd.read_csv(filename,delimiter=";",header=None,index_col=None)

    fecha = [dato.split(" ")[0] for dato in datos[0]]
    hora = [dato.split(" ")[1] for dato in datos[1]]

    datos.pop(0)
    datos.pop(1)
    
    
    datos[2]=[float(dato.replace(",",".")) for dato in datos[2]]
    datos[3]=[float(dato.replace(",",".")) for dato in datos[3]]
    
    
    #datos[0]=fecha
    #datos[1]=hora
    datetime=[fecha[i]+" "+hora[i] for  i in range(len(hora))]
    #datos["datetime"]=datetime
    datos["datetime"]=pd.to_datetime(datetime,format='%d/%m/%Y %H:%M:%S')
    
    
    
    #datos.set_index(["datetime"],inplace=True)
    
    datos.rename(columns={2:"monto",3:"precio"},inplace=True)
    datos.to_csv("clean_"+filename,sep=";",index=False)


limpiardatos("transacciones2008.txt")
limpiardatos("transacciones2009.txt")
limpiardatos("transacciones2010.txt")