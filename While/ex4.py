while True:
    inicio = int(input("Bem-vindo ao leitor de compras(digite 1 para continuar): "))
    if inicio == 1:
        break
ProdutoMaisCaro = ""
PrecoPrdoutoMaisCaro = 0
TotalGasto = 0
while True:
    nome = str(input("Digite um produto: "))
    preco = float(input("Digite o preço: "))
    if preco > PrecoPrdoutoMaisCaro:
        ProdutoMaisCaro = nome
        PrecoPrdoutoMaisCaro = preco
    TotalGasto += preco
    continuar = str(input("Deseja continuar?(S/N): "))
    if continuar.upper() != "S":
        break
print(f"O produto mais caro é: {ProdutoMaisCaro}")
print(f"O total gasto é: {TotalGasto}")
