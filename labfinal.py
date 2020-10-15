import lab as lb
import pandas as pd
def encontrar_condicional(df, x,y,a):
    cardX = lb.cardinalidad(df,x)
    cardY = lb.cardinalidad(df,y)
    listaFinal = []
    valoresY = lb.find_variables(y)
    for valorY in valoresY:
        val = lb.probabilidad_x_si_y(df,x,y,valorY,a)
        listaFinal+(val)
    return listaFinal
def decode(listaFinal,x,y):
    listaNombres = []
    valoresY = lb.find_variables(y)
    valoresX = lb.find_variables(x)
    for valorY in valoresY:
        for valorX in valoresX:
            listaNombres.append(valorX,valorY)
    df = pd.DataFrame   (list(zip(columns = [])))
