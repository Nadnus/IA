def findVariables(df, col):
    l = []
    for elem in df[col]:
    	if elem not in l:
    		l.append(elem)
    return l
