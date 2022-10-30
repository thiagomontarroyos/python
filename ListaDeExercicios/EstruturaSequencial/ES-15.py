# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # a. salário bruto.
    # b. quanto pagou ao INSS.
    # c. quanto pagou ao sindicato.
    # d. o salário líquido.
    # e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        # + Salário Bruto : R$
        # - IR (11%) : R$
        # - INSS (8%) : R$
        # - Sindicato ( 5%) : R$
        # = Salário Liquido : R$
        
        # Obs.: Obs.: Salário Bruto - Descontos = Salário Líquido.

hora_din = float(input("Quanto você ganha por hora: "))
hora_mes = float(input("Quantas horas você trabalha por mês: "))
din_mes = hora_din*hora_mes
a = din_mes
b = din_mes*8/100
c = din_mes*5/100
d = din_mes*76/100
e = din_mes*11/100
print("+ Salário Bruto : R$", a)
print("- IR (11%) : R$", e)
print("- INSS (8%) : R$", b)
print("- Sindicato ( 5%) : R$", c)
print("= Salário Liquido : R$", d)