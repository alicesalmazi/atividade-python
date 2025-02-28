#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#8. Peça ao usuário para digitar um número e imprima se é positivo ou negativo.

numero = float(input("Insira um número: "))

if numero < 0:
    print(f" {numero} é um número negativo.")
else:
    print(f"{numero} é um número positivo.")