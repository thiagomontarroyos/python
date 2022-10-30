# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input("Tamanho do arquivo para download em MB: "))
velo = float(input("Velocidade do seu link de internet em Mbps: "))
velo_down = velo/8
tempo = (tamanho/velo_down)/60
print("O tempo aproximado do download de seu arquivo é de: ", str(tempo) "minutos")