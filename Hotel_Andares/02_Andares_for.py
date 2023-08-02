def mostrar_andares_hotel():
    andares = list(range(20, 0, -1))
    andares.remove(13)
    for andar in andares:
        print("Andar:", andar)

mostrar_andares_hotel()