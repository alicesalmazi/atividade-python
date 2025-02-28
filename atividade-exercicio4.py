#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#4. Peça o raio de um círculo e calcule sua área. Em seguida, imprima o resultado.

import math

raioCirculo = float(input("Insira o raio do círculo: "))

areaCirculo = round((math.pi * pow(raioCirculo, 2)),2)

print("A área do círculo é:", areaCirculo)
