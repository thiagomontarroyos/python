# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temp_cels = float(input("Digite a temperatura em graus Celsius a ser convertida em Fahrenheit: "))
convert = (temp_cels*9/5) + 32
print("A temperatura em graus Fahrenheit é igual a:", convert)