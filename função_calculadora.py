def calculadora(num1, num2, operacao):
    if (operacao == 1):
        return num1 + num2
    elif (operacao == 2):
        return num1 - num2
    elif (operacao == 3):
        return num1 * num2
    elif (operacao == 4):
        return num1 / num2
    else:
        return 0
    
resultado = calculadora(6, 3, 1)
print(resultado)
resultado = calculadora(6, 3, 2)
print(resultado)
resultado = calculadora(6, 3, 3)
print(resultado)
resultado = calculadora(6, 3, 4)
print(resultado)