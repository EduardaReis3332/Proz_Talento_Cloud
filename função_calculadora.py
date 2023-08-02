def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("\nEscolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operacao = int(input("Digite o número da operação desejada: "))

    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o divisor é diferente de zero para evitar divisão por zero
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return 0
    else:
        print("Operação inválida.")
        return 0

resultado = calculadora()
print("Resultado:", resultado)