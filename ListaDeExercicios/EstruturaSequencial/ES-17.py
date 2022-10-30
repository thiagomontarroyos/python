# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        # comprar apenas latas de 18 litros;
        # comprar apenas galões de 3,6 litros;
        # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

m2 = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
lit = m2/6
caplata = 18
precolata = 80
capgalao = 3.6
precogalao = 25
lata = lit/caplata
total_lata = lata*precolata
galao = lit/capgalao
total_galao = galao*precogalao
print("Você precisará comprar ", str(lata) "latas de tintas e o preço total da compra será de " str(total_lata))
print("Você precisará comprar ", str(galao) "galões de tintas e o preço total da compra será de " str(total_galao))