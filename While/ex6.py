while True:
    inicio = int(input("Bem-Vindo à calculadora(digite 1 para continuar): "))
    if inicio == 1:
        break
while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um outro número: "))
    operacao = int(input("Escolha a operação\n1-soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n"))
    if operacao == 1:
        print(f"{num1 + num2}")
    elif operacao == 2:
        print(f"{num1 - num2}")
    elif operacao == 3:
        print(f"{num1 * num2}")
    elif operacao == 4:
        print(f"{num1 / num2}")
    continuar = str(input("Deseja continuar?(S/N): "))
    if continuar.upper() == "N":
        break