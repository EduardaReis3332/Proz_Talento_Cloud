def verificar_categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas):
    if quantidade_rodas == 2 or quantidade_rodas == 3:
        return "Categoria A"
    elif quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500:
        return "Categoria B"
    elif quantidade_rodas >= 4 and quantidade_pessoas > 8:
        return "Categoria D"
    elif quantidade_rodas >= 4 and peso_bruto > 6000:
        return "Categoria E"
    else:
        return "Categoria C"

def categoria():
    try:
        quantidade_rodas = int(input("Digite a quantidade de rodas do veículo: "))
        peso_bruto = float(input("Digite o peso bruto do veículo em quilogramas: "))
        quantidade_pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

        categoria = verificar_categoria_habilitacao(quantidade_rodas, peso_bruto, quantidade_pessoas)
        print(f"A melhor categoria de habilitação para este veículo é: {categoria}")
    except ValueError:
        print("Por favor, digite valores válidos para a quantidade de rodas, peso bruto e quantidade de pessoas.")

categoria()