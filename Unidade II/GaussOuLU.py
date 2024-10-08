#Método de Gauss ou LU

import numpy as np

#digite aqui sua matriz
#se for Gauss: se lembre que é a matriz toda (AUMENTADA),
#incluindo a igualdade
#se for LU: é apenas a sua matriz normal
matriz = np.array([[5,2,1],[3,1,4],[1,1,3]], dtype = float)

#digite aqui o nº de linhas e colunas
linhas = 3
colunas = 3

#não mexer
L = np.eye(linhas,colunas)

print("Matriz original: \n\n",matriz,"\n\n -------------------------------------- \n")

#se for Gauss, o resultado é apenas a matriz U, ignore L

#Tem que ir baseando nas linhas (não mexer)
for i in range(0, linhas):

	pivor = matriz[i,i]
	
	for j in range((i+1),linhas):
		
		m = matriz[j,i]/pivor
		print("Pivor: ",pivor,"   m = ",matriz[j,i],"/",pivor," = ",m)
		print("L",(j+1), " = ", "L",(j+1)," - m*L",(i+1),"\n\n")
		L[j,i] = m
		matriz[j] = matriz[j]-(m*matriz[i])
		print("Matriz U: \n\n",matriz,"\n")
		print("-------------------------------------- \n")
		
		
print("Matriz L: \n\n",L)
