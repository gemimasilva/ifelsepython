def calcular_media(nome, nota1, nota2):
    media = (nota1 + nota2) / 2
    return nome, media

# Obtendo informações do usuário
nome1 = input("Gemima: ")
nota1_1 = float(input("Digite a primeira nota {}: ".format(nome1)))
nota1_2 = float(input("Digite a segunda nota {}: ".format(nome1)))

nome2 = input("grace: ")
nota2_1 = float(input("Digite a primeira nota {}: ".format(nome2)))
nota2_2 = float(input("Digite a segunda nota {}: ".format(nome2)))

# Calculando médias
nome_media1, media1 = calcular_media(nome1, nota1_1, nota1_2)
nome_media2, media2 = calcular_media(nome2, nota2_1, nota2_2)

# Exibindo resultados
print("A média de {} é: {:.2f}".format(nome_media1, media1))
print("A média de {} é: {:.2f}".format(nome_media2, media2))
