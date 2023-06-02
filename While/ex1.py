while True:
    inicio = int(input("Descubra a média(digite 1 para continuar): "))
    if inicio == 1:
        break
soma = 0
numNota = 0
while True:
    nota = float(input("Digite uma nota(digite um valor negativo para parar): "))
    if nota >= 0:
        soma += nota
        numNota += 1
    else:
        break
media = soma / numNota
print(f"A média das notas é: {media}")


