# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    # C = 5 * ((F-32) / 9).

temp_fah = float(input("Digite a temperatura em graus Fahrenheit a ser convertida em Celsius: "))
convert = 5*((temp_fah-32)/9)
print("A temperatura em graus Celsius é igual a:", convert)