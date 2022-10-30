# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # a. Para homens: (72.7*h) - 58
    # b. Para mulheres: (62.1*h) - 44.7

h = float(input("Digite a sua altura em centímetros: "))
a = (72.7*h)-58
b = (62.1*h)-44.7
print("Caso você seja homem, seu peso ideal em quilos é igual a:", a)
print("Caso você seja mulher, seu peso ideal em quilos é igual a:", b)