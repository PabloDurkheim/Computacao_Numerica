#Método de Jacobi

#Se lembre meu patrão, que nesse método, as variáveis 
#x1, x2, x3... só são atualizadas após cada iteração,
#e o erro relativo é a norma infinito do vetor novo menos o antigo
#sobre a norma infinito do vetor novo.

import numpy as np

#não mexer
iteracao = 1
continuar = 1

#Valores do vetor x0 (altere se tiver mais ou menos variáveis)
x1 = 0; x2 = 0; x3 = 0; x4 = 0

while(continuar == 1):

	#vetor x0 - Solução inical (altere se tiver mais ou menos variáveis)
	x0 = np.array([[x1], [x2], [x3],[x4]])
	
	#Isolando (altere se tiver mais ou menos variáveis)
	X1 = (0.25*x2 + 0.25*x3)
	X2 = (0.25*x1 + 0.25*x4)
	X3 = (0.25 + 0.25*x1 + 0.25*x4)
	X4 = (0.25 + 0.25*x2)

	#vetor resultado (altere se tiver mais ou menos variáveis)
	X = np.array([[X1],[X2],[X3],[X4]])

	#Erro relativo (norma infinito) - não mexer
	vetor = X-x0
	Er = abs((max(abs(vetor)))/max(abs(X)))

	#Erro absoluto (norma infinito) - não mexer
	Ea = max(abs(vetor))

	print("Iteração ",iteracao, "\n")
	print("Antigo: \n\n",x0,"\n")
	print("Novo: \n\n",X,"\n")
	print("Subtração dos vetores (Novo - Antigo): \n\n",vetor,"\n")
	print("Norma infinito da subtração dos vetores: ", max(abs(vetor)))
	print("Norma infinito do vetor solução(Novo): ",max(abs(X)),"\n")
	print("Erro relativo: ",max(abs(vetor))," / ",max(abs(X))," = ",Er)
	print("Erro absoluto: ",Ea,"\n")

	x1 = X1
	x2 = X2
	x3 = X3
	x4 = X4
	
	iteracao = iteracao + 1

	print("Continuar? Não(0) Sim(1)")
	continuar = int(input())
	print("\n")
