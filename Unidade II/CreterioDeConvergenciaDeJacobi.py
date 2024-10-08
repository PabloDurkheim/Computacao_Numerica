#Critério de convergência de Jacobi

#Sistemas Lineares Ax = b viram => x = Bx+g

import numpy as np

#Escreva a sua matriz aqui
matriz = np.array([[-6,2,1],[1,4,1],[-1,-1,3]], dtype = float)

#escreva sua matriz B aqui (matriz com diagonal zerada)
B = np.array([[0,0,0],[0,0,0],[0,0,0]], dtype = float)

#Escreva a quantidade de linhas e colunas
linhas = 3
colunas = 3

print("Sua matriz: \n\n",matriz,"\n\n")

#NORMA INFINITO DA MATRIZ:

#Esmaga a matriz de lado
#Tem que somar as linhas em módulo (não mexer)
soma = 0
vetor = []
print("Norma infinito da matriz: \n\n")

#não mexer
for i in range(0,linhas):
	for j in range(0,colunas):
		soma = soma + abs(matriz[i,j])
	print("Soma da linha",(i+1),"(em módulo): ", soma,"\n")
	vetor.append(soma)
	soma = 0

if(max(vetor)<1):
	print("Norma infinito = ",max(vetor),"=> converge \n\n")
else:
	print("Norma infinito = ",max(vetor),"=> não sei se converge \n\n")

#NORMA 1

#Esmaga a matriz de cima pra baixo
#tem que somar as colunas (não mexer)
#sempre usa a matriz B
soma1 = 0
vetor1 = []
print("Norma 1 da matriz: \n\n")

for i in range(0,linhas):
	for j in range(0,colunas):
		soma1 = soma1 + abs(matriz[j,i])
	print("Soma da coluna",(i+1),"(em módulo): ", soma1,"\n")
	vetor1.append(soma1)
	soma1 = 0

if(max(vetor1)<1):
	print("Norma 1 = ",max(vetor1),"=> converge \n\n")
else:
	print("Norma 1 = ",max(vetor1),"=> não sei se converge\n\n")

#Critério das linhas
#verifica se a soma das linhas é menor
#que o elemento da diagonal

soma2 = 0
converge = True

print("Critério das linhas: \n\n")

for i in range(0,linhas):

	pivor = matriz[i,i]
	
	for j in range(0,colunas):
		soma2 = soma2 + abs(matriz[i,j])
	soma2 = soma2 - abs(pivor)
	print("Pivor =",pivor)
	print("Soma da linha",(i+1),"sem o pivor (em módulo): ", soma2,"\n")

	if(soma2 >= abs(pivor)):
		converge = False
	soma2 = 0

if(converge == True):
	print("Converge \n\n")
else:
	print("Não sei se converge \n\n")

#Critério das colunas
#divide a linha inteira pelo pivor
#depois verifica a soma das colunas sem o pivor

soma3 = 0
converge = True

print("Critério das colunas: \n\n")

#divide as linhas pelo pivor
for i in range(0,linhas):

	pivor = matriz[i,i]
	
	for j in range(0,colunas):
		matriz[i,j] = matriz[i,j]/pivor
	print("Dividu a linha",(i+1),"por",pivor)

print("\n\n",matriz, "\n\n")

#verifica a soma das colunas
for i in range(0,linhas):
	
	for j in range(0,colunas):
		soma3 = soma3 + abs(matriz[j,i])
	soma3 = soma3 - 1
	print("Soma da coluna",(i+1),"sem o pivor (em módulo): ", soma3,"\n")

	if(soma3 >= 1):
		converge = False
	soma3 = 0
		
if(converge == True):
	print("Converge \n\n")
else:
	print("Não sei se converge \n\n")
