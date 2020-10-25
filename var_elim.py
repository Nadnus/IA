import lab as lb
import thing as tg
import collections
import itertools


def find_parents(df, vertice, grafo, a):

    # hacer que el parents que se le pasa sea un default dict, con una lista vacia si no hay elementos


def eliminacion_single(df, grafo, parents, Z, a):
    phi_prima = {}
    not_phi_prima = {}
    variables = set()
    for P in parents:
        if Z in parents[P]:
            phi_prima[P] = parents[P]
        else:
            not_phi_prima[(parents[P])]
    trinche = {}
    tau = {}
    condicionales = []
    for factor in phi_prima:
        cond = tg.condicional(df, factor, parents[factor], a)
        condicionales.append(cond)
        for parent in phi_prima[factor]:
            variables.add(parent)
    valores = []
    for v in variables:
        valores.append(lb.find_variables(df, v))
    combos = list(itertools.product(*list(valores)))
    combos_tau = list(itertools.product(*(list(valores)[1:])))
    for combo in combos:
        trinche[combo] = 1
        for dicc in condicionales:
            trinche[combo] = dicc[combo] * trinche[combo]
    for c in combos_tau:
        tau[c] = 0
        for evidencia in valores[0]:
            tau[c] = trinche[(evidencia,)+c] + tau[c]
    return tau


def eliminacion(df, grafo, consulta, evidencia, ocultas, a):
    factores = {}
    for vertice in grafo:
        find_parents(df, vertice, grafo)
        factores[vertice] = find_parents(df, vertice, grafo)

    # make good
