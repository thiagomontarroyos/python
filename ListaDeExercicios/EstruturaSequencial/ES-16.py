# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

m2 = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
lit = m2/3
caplata = 18
precolata = 80
lata = lit/caplata
total = lata*precolata
print("Você precisará comprar ", str(lata) "latas de tintas e o preço total da compra será de " str(total))