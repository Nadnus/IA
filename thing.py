import lab as lb
import pandas as pd
import itertools


def intersect_count(df, valores, columnas):
    l = len(valores)
    if l == 1:
        return lb.conteo(df,valores[0],columnas[0])
    rows = []
    for tup in df.itertuples():
        var1 = getattr(tup,columnas[0])
        var2 = getattr(tup,columnas[1])
        e1 = var1 == valores[0]
        e2 = var2 == valores[1]
        if e1 and e2:
            rows.append(tup)
    for i in range(2,l):
        to_remove = []
        for tup in rows:
            a = getattr(tup,columnas[i])
            if  a != valores[i]:
                to_remove.append(tup)
        for tup in to_remove:
            rows.remove(tup)
    return len(rows)


def condicional(df, target_var, variables, a):
    df_len = len(df)
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
        denom1 = df_len + card_acum_x
        num2 = intersect_count(df, combo2, variables) + a
        denom2 =  df_len+ card_acum
        resultados[combo] = (numerador1/denom1)/(num2/denom2)
    print ((resultados))

data = pd.read_csv("weather.csv")
condicional(data, "outlook", ["play", "windy"],1)
