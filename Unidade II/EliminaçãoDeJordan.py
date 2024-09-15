#Eliminação de Jordan

import numpy as np

#digite aqui sua matriz (se lembre que é a matriz toda, 
#incluindo a igualdade)
matriz = np.array([[2,3,-1,5],[4,4,-3,3],[2,-3,1,-1]], dtype = float)

#digite aqui o total de linhas e colunas
linhas = 3
colunas = 4

#não mexer
L = np.eye(3,4)

print("Matriz original: \n\n",matriz,"\n\n")

#Tem que ir baseando nas linhas (não mexer)
for i in range(0, linhas):

	pivor = matriz[i,i]
	
	for j in range((i+1),linhas):

		m = matriz[j,i]/pivor
		L[j,i] = m
		matriz[j] = matriz[j]-(m*matriz[i])
		
		
print("Matriz U: \n\n",matriz,"\n\n")
print("Matriz L: \n\n",L, "\n\n")
#print(matriz.dot(L))

#Tem que ir baseando nas linhas (não mexer)
for i in range(linhas-1, -1, -1):
	
	pivor = matriz[i,i]
	#print(pivor)
	
	for j in range((i-1),-1, -1):
		
		m = matriz[j,i]/pivor
		L[j,i] = m
		matriz[j] = matriz[j]-(m*matriz[i])

print("Matriz de Jordan: \n\n",matriz)
