#Método da secante (converge SEMPRE)
import math

#intervalos
x0 = 0
x1 = 6

#Iteraçoes (não mexer)
iteracoes = 1
continuar = 1

#escreva a função aqui no return
def funcao(x):

  return math.pi*pow(x, 2)*(3-x/3)-30 

#Não mexer
while(continuar == 1):

  #Método da secante (não mexer)
  x2 = x1 - ((x1-x0)*funcao(x1))/(funcao(x1)-funcao(x0))

  #erro relativo (não mexer)
  Er = abs((x2-x1)/x2)

  #erro absoluto
  Ea = abs(x2-x1)

  print("Iteração ",iteracoes, "\n")
  print("f(",x0,") = ", funcao(x0),"\n")
  print("f(",x1,") = ", funcao(x1),"\n")
  print("Erro relativo: ", Er,"\n")
  print("Erro absoluto: ", Ea,"\n")
  print("x = ", x2, "\n")
  print("Continuar? não(0) sim(1)")

  continuar = int(input())

  if(continuar == 1):
    iteracoes = iteracoes+1
    x0 = x1
    x1 = x2
