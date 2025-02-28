#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#6. Peça ao usuário para inserir dois números e imprima o resultado da multiplicação entre eles.

from decimal import Decimal

numero1 = Decimal(input("Insira o primeiro número: "))
numero2 = Decimal(input("Insira o segundo número: "))

multiplicacaoNumeros = numero1 * numero2

print("Resultado da multiplicação:", multiplicacaoNumeros)