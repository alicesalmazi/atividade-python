#LISTA DE EXERCÍCICIOS – ENTRADAS E SAÍDAS
#3. Solicite a idade do usuário e imprima uma mensagem indicando se é maior de idade.

idadeUsuario = int(input("Insira sua idade: "))

if idadeUsuario >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")