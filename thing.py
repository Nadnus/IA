import lab as lb
import pandas as pd
import itertools


def intersect_count(df, valores, columnas):
    l = len(valores)
    rows = []
    for tup in df.itertuples():

        var1 = getattr(tup,columnas[0])
        var2 = getattr(tup,columnas[1])
        if var1 == valores[0] and var2 == valores[1]:
            rows.append(tup)
    for i in range(2, l-1):
        to_remove = []
        for tup in rows:
            if tup[columnas[i]] != valores[i]:
                to_remove.append(tup)
        for tup in to_remove:
            rows.remove(tup)
    return len(rows)


def condicional(df, target_var, variables, a):
    valores = {}
    valores[target_var] = lb.find_variables(df, target_var)
    for var in variables:
        buffer = lb.find_variables(df, var)
        valores[var] = buffer
    lista_vars = []
    for v in valores:
        lista_vars.append(valores[v])

    combos = list(itertools.product(*lista_vars))

    print(len(combos))
    resultados = {}
    card_acum = a
    for elem in variables:
        card_acum = card_acum * lb.cardinalidad(df, elem)
    card_acum_x = card_acum * lb.cardinalidad(df, target_var)
    for combo in combos:
        combo2 = combo[1:]
        numerador1 = intersect_count(df, combo, [target_var]+variables) + a
        denom1 = df.size + card_acum_x
        num2 = intersect_count(df, combo2, variables) + a
        denom2 = df.size + card_acum
        resultados[combo] = (numerador1/denom1)/(num2/denom2)
    print (len(resultados))

data = pd.read_csv("weather.csv")
condicional(data, "outlook", ["temperature", "humidity"],1)
