def inference(df, targetClass, evidenceList, evidenceValueList, alpha):
    marginal = estimar_marginal(df, evidenceList, alpha)
    conditional = estimar_condicional(df, evidenceList, targetClass, alpha)
    targetClassValues = getValues(df, targetClass)

    result = []

    for value in targetClassValues:
        prob = marginal[evidenceValueList] * conditional[evidenceList = evidenceValueList & & targetClass = value]
        result.append(prob)

    print("most likely ", max(result))
    return results


print(inference(df, 'Y', ['X'], ['0']))
