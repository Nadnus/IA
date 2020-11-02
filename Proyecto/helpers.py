import copy
import math
import pandas as pd
import itertools


def isDAG(g): #g es una matriz de adyacencia
    visited = []
    q = [0]
    while len(q) != 0:
        curr = q[0]
        for i in range(len(g)):
            if g[i][curr] == 1:
                if i in visited:
                    return False
                else:
                    q.append(i)
        visited.append(curr)
        q.pop(0)
    return True

def addEdge(g):
    l = []
    for i in range(len(g)):
        for j in range(len(g)):
            if i!=j and g[i][j] == 0:
                aux = copy.deepcopy(g)
                aux[i][j] = 1
                if isDAG(aux):
                    l.append(aux)
    return l

def rmvEdge(g):
    l = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 1:
                aux = copy.deepcopy(g)
                aux[i][j] = 0
                l.append(aux)
    return l

def invEdge(g):
    l = []
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 1:
                aux = copy.deepcopy(g)
                aux[i][j] = 0
                aux[j][i] = 1
                if isDAG(aux):
                    l.append(aux)
    return l

def findVariables(df, col):
    l = []
    for elem in df[col]:
    	if elem not in l:
    		l.append(elem)
    return l

def getCardinality(df, col):
    return len(findVariables(df,col))

def getParents(varName, df, g):
    colNames = list(df.columns)
    idx = colNames.index(varName)
    result = [varName]
    aux = []
    for i in range(len(g)):
         if(g[idx][i] == 1):
             aux.append(colNames[i])
    result.append(aux)
    return result

def calcQ(varName,df,g):
    prod = 1
    parents = getParents(varName,df,g)[1]
    if len(parents) > 0:
        for p in parents:
            prod*=getCardinality(df,p)
    return prod

def Qpossibilities(List):
    res = []
    for r in itertools.product(*List):
        aux = []
        for i in range(len(r)):
            aux.append(r[i])
        res.append(aux)
    return res

def Nij(df,i,j,g):
    colNames = list(df.columns)
    parent = getParents(colNames[i],df,g)
    result = 0
    
    L = []
    
    for p in parent[1]:
        L.append(findVariables(df, p))
    
    possibilities = Qpossibilities(L)
    x = possibilities[j]
    for index,row in df.iterrows():
        a = []
        for i in range(len(parent[1])):
            if(row[colNames[i]] == x[i]):
                a.append(True)
            else:
                a.append(False)
        
        if(all(a)):
            result+=1
    return result

def Nijk(df,i,j,k,g):
    colNames = list(df.columns)
    parent = getParents(colNames[i],df,g)
    result = 0
    iPossibilities = findVariables(df,colNames[i])
    
    L = []
    
    for p in parent[1]:
        L.append(findVariables(df,p))
    
    possibilities = Qpossibilities(L)
    x = possibilities[j]
    
    for index, row in df.iterrows():
        a = []
        for i in range(len(parent[1])):
            if(row[colNames[i]] == x[i]):
                a.append(True)
            else:
                a.append(False)
        if(all(a) and row[colNames[i]] == iPossibilities[k]):
            result+=1
    return result

def k2(df,g):
    colNames = list(df.columns)
    accum1 = 1
    
    for i in range(len(colNames)):
        accum2 = 1
        for j in range(calcQ(colNames[i],df,g)):
            num = math.factorial(getCardinality(df,colNames[i])-1 + Nij(df,i,j,g))
            denom = math.factorial(getCardinality(df,colNames[i])-1 + Nij(df,i,j,g))
            
            accum3 = 1
            for k in range(getCardinality(df,colNames[i])):
                accum3 *= math.factorial(Nijk(df,i,j,k,g))
            
            accum2 *= (num/denom)*accum3
        accum1 *= accum2
    return accum1


def hillClimbing(df,initialState): #initialState tiene la misma forma que g
    state = initialState
    auxState = state
    currScore = k2(df,state)
    auxScore = currScore
    
    while(1):
        neighbors = addEdge(state)+rmvEdge(state)+invEdge(state)
        for n in neighbors:
            auxScore = k2(df,n)
            print("curr",currScore)
            print("aux",auxScore)
            if auxScore > currScore:
                auxState = copy.deepcopy(n)
                currScore = auxScore
        if state == auxState:
            return state
        else:
            state = copy.deepcopy(auxState)

df = pd.read_csv("../datasets/weather.csv")

s = [[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

print(hillClimbing(df,s))