#Eliminação de Gauss

import numpy as np

#digite aqui sua matriz (se lembre que é a matriz toda, 
#incluindo a igualdade)
matriz = np.array([[6,2,-1,7],[2,4,1,7],[3,2,8,13]], dtype = float)

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
print("Matriz L: \n\n",L)
