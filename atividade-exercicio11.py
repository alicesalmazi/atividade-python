#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#11. Solicite um número inteiro e imprima se é par ou ímpar.

numero = int(input("Insira um número: "))

verificadorNumeroImpar = numero % 2

if verificadorNumeroImpar == 1:
    print(f"O número {numero} é impar.")
else:
    print(f"O número {numero} é par.")