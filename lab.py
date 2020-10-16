import pandas as pd


def conteo_interseccion(df, parametros, columnas):
    col1 = df[columnas[0]]
    col2 = df[columnas[1]]
    cont = 0
    for i in range(len(col1)):
        if(col1[i] == parametros[0] and col2[i] == parametros[1]):
            cont += 1
    return cont


def cardinalidad(df, columnaX):
    cardinality = len(pd.Index(df[columnaX]).value_counts())
    return cardinality


def conteo(df,x, columnaX):
    cont = 0
    for i in df[columnaX]:
        if i == x:
            cont +=1

    return cont


def find_variables(x, columnaX):
    l = []
    for elem in x[columnaX]:
        if elem not in l:
            l.append(elem)
    return l


def estimar_marginal(df, X, a):
    d = {}

    for i in df[X]:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    card = len(d)
    for i in d:
        d[i] = (d[i]+a)/(df.shape[0] + card*a)

    dfRes = pd.DataFrame(d, columns=["X", "P(X)"])
    return dfRes


def probabilidad_x_si_y(df, x, columnaY, valY, a):
    toReturn = []
    columnas = [x, columnaY]
    # faltan separar las variables en variables []
    variables = find_variables(df,x)
    for row in variables:
        parametros = [row, valY]
        card = conteo_interseccion(df, parametros, columnas) + a
        denom = df.size + conteo(df,row, x)*conteo(df,valY, columnaY)*a
        numerador = card / denom
        # confirmar los valores del segundo denominador, en la pizarra sale c * y * a,  sera cy *a?
        denom2 = (conteo(df,valY, columnaY) + a) / \
            (df.size + cardinalidad(df, columnaY) * a)
        totes = numerador / denom2
        toReturn.append(totes)
    return toReturn


#def predict(clase, variables, valores):
