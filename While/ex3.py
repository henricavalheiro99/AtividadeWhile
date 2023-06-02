while True:
    inicio = int(input("Bem-vindo ao leitor de números(digite 1 para continuar): "))
    if inicio == 1:
        break
while True:
    num = int(input("Digite um número(Digite um valor negativo ou 999 para parar): "))
    if num == 999 or num < 0:
        break