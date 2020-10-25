import lab as lb
import thing as tg
import collections
import itertools

def getParents(g,df):
    fathers = []
    res = []
    colNames = list(df.columns)
    
    for col in range(len(g)):
        aux = []
        for row in range(len(g)):
            if(m[col][row] == 1):
                aux.append(colNames[row])
        fathers.append(aux)

    for i in range(len(g)):
        yield [colNames[i],fathers[i]]


def compression(var,L): #var es el nombre de la variable que queremos desaparecer
# lista resultante de la multiplicacion
  res = {}
  varNames = [L[0][0]]+L[0][1]

  varIdx = varNames.index(var)

  newNames = L[0].copy()
  
  newNames[1].remove(var)
  
  varPossibleVals = []
  
  for i in L[1]:
  varPossibleVals.append(i[varIdx])
  varPossibleVals = set(varPossibleVals)
  varPossibleVals = list(varPossibleVals)
  
  dictIdxs = []
  for idx in L[1]:
    dictIdxs.append(idx)
  
  newIdxs = []
  for i in dictIdxs:
    i2 = list(i)
    del i2[varIdx]
    
    if tuple(i2) not in res:
      res[tuple(i2)] = L[1][tuple(i)]
    else:
      res[tuple(i2)] += L[1][tuple(i)]
  
  return [newNames,res]


def sumProductVE(df,consulta, ocultas, nombreEvidencia, valorEvidencia, m):

	# definir phi
	parents = getParents(m,df)
	phi = []

	for i in parents:
		phi.append(tg.condicional(df,i[0][0],i[0][1],a,True))

	# z -> lista de variables por eliminarse
	## z definido en los inputs
	z = ocultas



	# cosito raro-> z ordenado topologicamente
	################FUNCION DE CHAVEZ (Modificar z para que este ordenado)
	# z = funcion(z,m)

	# Para todos los elementos de Z
	# hacer sum product eliminate de phi
	for i in z:
		phi = sumProductEliminateVar(z, phi)

	# Ahora phi ya esta lleno con los valores que tenemos (evidencias)
	# La unica desconocida es la consulta
	# Se hace productoria de todos despues de encontrar los valores de las evidencias
	final = {}
	evidencia = {}

	for i in range(len(nombreEvidencia)):
		evidencia[nombreEvidencia[i]] = valorEvidencia[i]

	for i in phi: # forma [ [ a , [b,c]],{(0,0,0):algo,(0,0,1): algomas ...} ]
		e = [i[0][0]] + i[0][1]
		flag = True

		for v in e:
			if v not in nombreEvidencia: # no conocemos los valores
				flag = False

		if flag: #reemplazamos
			

		else: #tenemos que mostrar todas las combinaciones porque la variable desconocida es la consulta
		# añadir al diccionario "final" y multiplicar todo


		return final





def sumProductEliminateVar(z,phi):

	# z ->variable por ser eliminada
	## definida en parametro


	# phi->set de factores
	## definida en parametro

	# phi' -> factores que involucran z
	phi_prime = [x for x phi if z not in []]

	phi_prime = []

	for i in range(len(phi)):
		if z not in phi[i][0][0] and z not in phi[i][0][1]:
			phi_prime.append(phi[i])


	# phi'' -> fectores que no involucran z_i
	phi_prime_prime = []
	for item in phi:
		if item not in phi_prime:
			phi_prime_prime.append(item)



	# Multiplicar todos los elementos de phi', devuelve diccionario
	######### Funcion de chavez
	# psi = funcion(elementos de phi_prime)


	# tau -> Comprimir eliminando z_i del diccionario, los valores iguales se suman
	tau = compression(z,psi)

	# añadir tau al phi''
	phi_prime_prime.append(tau)

	# devolver phi''
	return phi_prime_prime

