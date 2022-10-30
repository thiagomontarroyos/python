# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

din_hora = float(input("Quanto você ganha por hora: "))
horas_mes = int(input("Quantas horas você trabalha por mes: "))
din_mes = din_hora*horas_mes
print("Você ganha por mes: R$:", din_mes)