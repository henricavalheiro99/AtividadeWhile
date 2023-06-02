while True:
    inicio = int(input("Verificando gênero(digite 1 para continuar): "))
    if inicio == 1:
        break
while True:
    genero = str(input("Digite o seu gênero(M para masculino e F para feminino: "))
    if genero.upper() == "M":
        print("Seu gênro é masculino")
        break
    if genero.upper() == "F":
        print("Seu gênero é feminino")
        break