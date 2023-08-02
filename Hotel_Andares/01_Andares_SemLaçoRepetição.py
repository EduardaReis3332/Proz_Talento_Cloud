def mostrar_andares_hotel():
    andares = list(range(20, 0, -1))
    andares.remove(13)
    print("Andares:", ", ".join(map(str, andares)))

mostrar_andares_hotel()