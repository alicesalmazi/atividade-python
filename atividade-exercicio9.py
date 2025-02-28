#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#9. Solicite um valor em reais e imprima o equivalente em dólares (considere a cotação fixa).

valorReal = float(input("Insira o valor em Reais: "))

valorDolar = round((valorReal / 5.83150),2)

print(f"Você possui {valorDolar} dolares.")