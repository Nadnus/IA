import lab as lb
import pandas as pd
def encontrar_condicional(df, x,y,a):
    cardX = lb.cardinalidad(df,x)
    cardY = len(y)
    listaFinal = []
    valoresY = y
    for valorY in valoresY:
        val = lb.probabilidad_x_si_y(df,x,y,valorY,a)
        listaFinal+(val)
    return listaFinal
def decode(listaFinal,x,y):
    listaNombres = []
    valoresY = y
    valoresX = lb.find_variables(x)
    for valorY in valoresY:
        for valorX in valoresX:
            listaNombres.append(valorX,valorY)
    df = pd.DataFrame   (list(zip(valoresY,valoresX)), columns = [y,x])

