while True:
    inicio = int(input("Descubra a soma dos pares(digite 1 para continuar): "))
    if inicio == 1:
        break
somaPares = 0
while True:
    num = float(input("Digite um número(digite 0 para parar): "))
    if num == 0:
        break
    elif num % 2 == 0:
        somaPares += num
print(f"A soma dos pares é: {somaPares}")