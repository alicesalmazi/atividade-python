#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#7. Solicite a altura e o peso do usuário. Calcule o IMC (Índice de Massa Corporal) e imprima o resultado.

#from decimal import Decimal

peso = float(input("Insira seu peso em Kg: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso / pow(altura,2)

if imc < 16:
    print("Seu estado é de magreza grave\nProcure um médico ou nutricionista.")
elif imc < 17:
    print("Seu estado é de magreza moderada\nPrecisa rever sua alimentação.")
elif imc < 18.5:
    print("Seu estado é de magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
    print("Seu estado é saudável\nParabéns!")
elif imc < 30:
    print("Seu estado é de sobrepesol\nPrecisa rever sua alimentação.")
elif imc < 35:
    print("Seu estado é de obesidade grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
    print("Seu estado é de obesidade grau II (severa)\nProcure um médico ou nutricionista.")
else:
    print("Seu estado é de obesidade grau III (mórbida)\nProcure um médico ou nutricionista.")