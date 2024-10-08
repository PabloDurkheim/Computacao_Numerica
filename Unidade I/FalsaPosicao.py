#FALSA POSIÇÃO (converge SEMPRE)
import math

#intervalos
x0 = 0.05
x1 = 0.1

#Iteraçoes (não mexer)
iteracoes = 1
continuar = 1
xAntigo = 0

#escreva a função aqui no return
def funcao(x):

  return (0.1854/x) - ((8.829*pow(10,-3))/(pow(x,2)))*(1-pow(math.e, (-21*x)))-1.2

#Bolzano
def bolzano(x1, x2):

  return funcao(x1)*funcao(x2)  
  
#Não mexer
while(continuar == 1):

  #falsa posição (não mexer)
  x = x0 - ((x1-x0)*funcao(x0))/(funcao(x1)-funcao(x0))

  print("Iteração ",iteracoes, "\n")
  print("[",x0,", ",x1,"]", "\n")
  
  if(bolzano(x0, x) < 0):
    x1 = x

  elif(bolzano(x, x1)<0):
    x0 = x
        
  
  if(x!= x0 and iteracoes == 1):

    #erro relativo (não mexer)
    Er = abs((x-x0)/x)

    #erro absoluto
    Ea = abs(x-x0)

  if(x!=x1 and iteracoes == 1):

    #erro relativo (não mexer)
    Er = abs((x-x1)/x)

    #erro absoluto
    Ea = abs(x-x1)

  if(iteracoes > 1):
    Er = abs((x-xAntigo)/x)
    Ea = abs(x-xAntigo)

 
  print("x = ", x, "\n")
  print("f(",x0,") = ", funcao(x0),"\n")
  print("f(",x1,") = ", funcao(x1),"\n")
  print("Erro relativo: ", Er,"\n")
  print("Erro absoluto: ", Ea,"\n")
  print("Continuar? não(0) sim(1)")

  xAntigo = x
  
  continuar = int(input())

  if(continuar == 1):
    iteracoes = iteracoes+1
