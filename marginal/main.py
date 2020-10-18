from .count import count

def createQueue(df,X):
    index = -1
    queue = []
    for i in range(len(df.columns)):
        if df.columns[i] == X:
            index = i 
    for j in range(len(df.values)):
        if df.values[j][index] not in queue:
            queue.append(df.values[j][index])
    return queue

def estimar_marginal(df, X, alpha):
    queue = createQueue(df,X)
    size = len(df.values)
    res = []
    for i in queue:
        freqX = count(df,[X],[i])
        f = (freqX[0] + alpha)/(size+(alpha*len(queue)))
        res.append(f)

    result = []
    for j in range(len(queue)):
        insideList = []
        insideList.append(queue[j])
        insideList.append(res[j])
        result.append(insideList)
    
    return result

# df = reader('weather.csv')
# estimar_marginal(df, 'outlook', 2)