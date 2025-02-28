#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#14. Peça a temperatura em graus Celsius e imprima a equivalente em Fahrenheit.

temperaturaCelsius = round((float(input("Insira a temperatura em graus Celsius:"))), 2)

temperaturaFahrenheit = round(((temperaturaCelsius * 1.8) + 32), 2)

print(f"{temperaturaCelsius} °C equivale à {temperaturaFahrenheit} °F.")