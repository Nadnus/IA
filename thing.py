import lab as lb
import pandas as pd
import itertools
import marginal.main as marg



def intersect_count(df, valores, columnas):
    l = len(valores)
    if l == 1:
        return lb.conteo(df, valores[0], columnas[0])
    rows = []
    for tup in df.itertuples():
        var1 = getattr(tup, columnas[0])
        var2 = getattr(tup, columnas[1])
        e1 = var1 == valores[0]
        e2 = var2 == valores[1]
        if e1 and e2:
            rows.append(tup)
    for i in range(2, l):
        to_remove = []
        for tup in rows:
            a = getattr(tup, columnas[i])
            if a != valores[i]:
                to_remove.append(tup)
        for tup in to_remove:
            rows.remove(tup)
    return len(rows)


def condicional(df, target_var, variables, a, flag = False):
    if not variables:
        return marg.estimar_marginal(df,target_var,a)
    df_len = len(df)
    valores = {}
    valores[target_var] = lb.find_variables(df, target_var)
    for var in variables:
        buffer = lb.find_variables(df, var)
        valores[var] = buffer
    lista_vars = []
    for v in valores:
        lista_vars.append(valores[v])
    lista_trunca = lista_vars[1:]
    combos = list(itertools.product(*lista_vars))
    otros_combos = list(itertools.product(*lista_trunca))

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
        denom2 = df_len + card_acum
        frac1 = (numerador1/denom1)
        frac2 = (num2/denom2)
        resultados[combo] = frac1/frac2
    for c in otros_combos:
        acc = 0
        for val in valores[target_var]:
            key = (val,) + c
            acc = acc + resultados[key]
        for val in valores[target_var]:
            resultados[(val,) + c] = resultados[(val,) + c]/acc
    if flag:
        return ([[target_var, variables],resultados])

    return ((resultados))

def condicionalFijas(df,fijas_nombre,fijas,variables_usadas = []):
    valid_combos = []
    if not variables_usadas:
        variables_usadas = df.columns
    valid_values = []
    for i in range(len(variables_usadas)):
        to_add = []
        if variables_usadas[i] not in fijas_nombre:
            to_add.append(lb.find_variables(df,variables_usadas[i]))
            
        else:
            index = fijas_nombre.index(variables_usadas[i])
            to_add.append([fijas[index]])
        valid_values.append(to_add[0])
    valid_combos  = list(itertools.product(*valid_values))
    return valid_combos

#variables es una lista de listas, condicionales una lista de diccionarios; variables[0] deberia ser la lista de variables que se usan en condicionales[0]
#

#
def probVar(df,var,nombres_fijas,valores_fijas,factores,a):
    valores_var = lb.find_variables(df,var)
    to_return = {}
    for valor in valores_var:
        mult = 1
        for f in factores:
            target = (f[0])[0]
            primers = (f[0])[1]
            param1 = [var] + nombres_fijas
            param2 = [valor] + valores_fijas
            param3 = [target] + primers
            combos = condicionalFijas(df,param1,param2, param3)
            for combo in combos:
                my_cond = f[1]
                mult = mult * my_cond[combo]
        to_return[valor] = mult
    return to_return
        



data = pd.read_csv('weather.csv')
#print(condicionalFijas(data,['play','windy'],['yes','TRUE']))
c = condicional(data,'outlook',['windy','play'],1,True)
c2 = condicional(data,'play',['outlook','windy'],1,True)
print(probVar(data,'outlook',['play','windy'],['yes',True],[c,c2],1))
