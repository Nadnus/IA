from pandas import *

def count(df,values,recurrences):
    dfValues = df.values
    dfColumns = df.columns
    res = []
    index = -1
    for i in range(len(values)):
        count = 0
        for j in range(len(dfColumns)):
            if dfColumns[j] == values[i]:
                index = j
        for k in range(len(dfValues)):
            if(dfValues[k][index]==recurrences[i]):
                count+=1
        res.append(count)
    return res
