import lab as lb
import pandas as pd
def encontrar_condicional(df, x,columnaY,y,a):
    cardX = lb.cardinalidad(df,x)
    cardY = len(y)
    listaFinal = []
    valoresY = y
    for valorY in valoresY:
        val = lb.probabilidad_x_si_y(df,x,columnaY,valorY,a)
        listaFinal = listaFinal+(val)
    return listaFinal
def decode(df,listaFinal,x,y):
    listaNombres = []
    valoresY = y
    valoresX = lb.find_variables(df,x)
    for valorY in valoresY:
        for valorX in valoresX:
            listaNombres.append(valorX,valorY)
    df = pd.DataFrame   (list(zip(valoresY,valoresX)), columns = [y,x])
data = pd.read_csv("weather.csv")
result = encontrar_condicional(data,"outlook","humidity",["high"],1)
counter = 0
for element in result:
    counter = counter + element
print (result)
