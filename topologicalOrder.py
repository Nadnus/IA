def searchForRoots(graph, graphColumnNames, hiddenVariables):
    roots = []
    flag = True
    for i in hiddenVariables:
        index = graphColumnNames.index(i)
        for j in range(len(graph)):
            if(graph[j][index] == 1):
                flag = False
                break
        if(flag):
            roots.append(i)
        else:
            flag=True
    return roots


def rest(roots, hiddenVariables):
    rest = []
    for i in hiddenVariables:
        if(i not in roots):
            rest.append(i)
    return rest


# funcion principal
def orderedList(graph, graphColumnNames, hiddenVariables):
    roots = searchForRoots(graph, graphColumnNames, hiddenVariables)
    leafs = rest(roots, hiddenVariables)
    print(roots)
    print(leafs)
    return roots + leafs


graph = [	[0, 0, 1, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]
          ]
print(orderedList(graph,['A','B','C','D'],['A','C','B']))