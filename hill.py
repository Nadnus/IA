
import numpy

def hill(df,heuristic, iters):
    size = len(df.columns)
    matrix= numpy.zeros((size,size))
    #memory is optional
    memory = []
    val = heuristic(matrix)
    memory.append(matrix)
    for i in range (iters):
        for config in getNeighbors(matrix):
            if config in memory or heuristic(config) < val:
                continue
            else:
                    val = heuristic(config)
                    matrix = config
                    memory.append[config]
    return matrix


