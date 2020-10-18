from reader import reader
from utils import *
from marginal.main import estimar_marginal
# from condicional.main import estimar_condicional


def findMarginalProb(evidence, mat):
    for i in mat:
        if i[0] == evidence:
            return i[1]

def findConditionalProb(value1, value2):
    return ""


def inference(df, targetClass, evidenceList, evidenceValueList, alpha):
    for evidenceIndex in range(len(evidenceList)):
        marginales = estimar_marginal(df, evidenceList[evidenceIndex], alpha)
        # conditional = estimar_conditional() # depende del esquema de sebastian, como se calcula la condicional
        evidenceProb = findMarginalProb(
            evidenceValueList[evidenceIndex], marginales)

        targetClassValues = findVariables(df, targetClass)

        result = []
        for value in targetClassValues:
            tempResult = []
            targetAndEvidenceProb = findConditionalProb(
                value, evidenceValueList[evidenceIndex])  # esto es lo de la funcion de Fernando
            mult = evidenceProb * targetAndEvidenceProb
            tempResult.append(mult)
        result.append(tempResult)

    print(result)

df = reader('datasets/training_dataset1.csv')
print(inference(df, 'B', ['A'], ['0'], 1))
