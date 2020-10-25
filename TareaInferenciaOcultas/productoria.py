def findCommonVariable(factores):
    bucket = []
    for k in factores:
        for i in k[0]:
            if(type(i) is list):
                for j in i:
                    if(j in bucket):
                        return j
                    else:
                        bucket.append(j)
            else:
                if i in bucket:
                    return i
                else:
                    bucket.append(i)


def findStartIndex(var, factores):
    for i in range(len(factores)):
        if(factores[i][0][0] == var):
            return i
    return -1


def genList(var, factores, factorIndex, targetIndex):
    for i in factores[factorIndex][0][1]:
        if( i != var and i not in factores[targetIndex][0][1]):
            factores[targetIndex][0][1].append(i)
    return factores[targetIndex][0]

def productoria(factores):
    var = findCommonVariable(factores)
    factorIndex = findStartIndex(var, factores)

    targetIndex = -1
    if(factorIndex == 0):
        targetIndex = 1
    else:
        targetIndex = 0

    listOfVariables = genList(var, factores, factorIndex, targetIndex)

    dic = factores[targetIndex][1]
    for i in dic:
        mult = dic[i] * factores[factorIndex][1][i[2]]
        dic[i] = mult
    return dic


c1 = [['D', []], {0: 0.4, 1: 0.6}]
c2 = [['C', ['B', 'D']], {(0, 0, 0): 0.2,
                          (1, 0, 0): 0.8,
                          (0, 1, 0): 0.6,
                          (1, 1, 0): 0.4,
                          (0, 0, 1): 0.7,
                          (1, 0, 1): 0.3,
                          (0, 1, 1): 0.1,
                          (1, 1, 1): 0.9}]

factores = [c1, c2]
print(productoria(factores))
