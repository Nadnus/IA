import lab as lb
import thing as thing
import marginal.main as marg
import pandas as pd
import math
import random
import itertools
def generate_random_m(size):
    mat = [[random.randint(0,1) for _ in range(size)]for _ in range(size)]
    return mat

def find_aristas(labels, matrix):
    indice_x = 0
    to_return = []
    for variable_origen in matrix:
        indice_j = 0
        for variable_target in variable_origen:
            if variable_target == 1:
                to_return.append((labels[indice_x], labels[indice_j]))
            indice_j = indice_j + 1
        indice_x = indice_x + 1

    return to_return


def entropia(df, matrix, alpha):
    sumatoria = 0

    variables = {}
    for col in df.columns.values:
        # Usamos esto o asumimos que hay islas?
        variables[col] = lb.find_variables(df, col)
    for vertice in df.columns.values:
        marginales = marg.estimar_marginal(df, vertice,alpha)
        for resultado in marginales:
            # llenar la formula version log
            val = (math.log(marginales[resultado]))*(lb.conteo(df,resultado,vertice))
            sumatoria = sumatoria + val

    # USAR EL GRAFO PARA ARMAR LA CONCATENACION DE LAS VARIABLES
    aristas = find_aristas(df.columns.values , matrix)
    for a in aristas:
        origen = a[0]
        final = a[1]
        if origen == final:
            continue
        # llenar la formula de el log
        condicional_combos = thing.condicional(df,origen,[final],alpha)
        lista = [variables[origen],variables[final]]
        combos = list(itertools.product(*lista))
        for c in combos:
            condicional = condicional_combos[c]
            a = (math.log(condicional))
            b = (lb.conteo_interseccion(df,c,df.columns.values))
            val =  a*b
            sumatoria = sumatoria + val
    return sumatoria


data = pd.read_csv("weather.csv")
n_columnas = len(data.columns)
mat = generate_random_m(n_columnas)
print(entropia(data,mat,1))