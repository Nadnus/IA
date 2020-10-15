import pandas as pd


def conteo_interseccion(df, parametros, columnas):
    return 0


def cardinalidad(df, columnaX):
    cardinality = len(pd.Index(df[columnaX]).value_counts())
    return cardinality


def conteo(x, columnaX):

    return 0


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
    variables = find_variables(x)
    for row in variables[x]:
        parametros = [row, valY]
        card = conteo_interseccion(df, parametros, columnas) + a
        denom = df.size + cardinalidad(row, x)*cardinalidad(valY, columnaY)*a
        numerador = card / denom
        # confirmar los valores del segundo denominador, en la pizarra sale c * y * a,  sera cy *a?
        denom2 = (conteo(valY, columnaY) + a) / \
            (df.size + cardinalidad(valY, columnaY) * a)
        totes = numerador / denom2
        toReturn.append(totes)
    return toReturn


def predict(clase, variables, valores):
