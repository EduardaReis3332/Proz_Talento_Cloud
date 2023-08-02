def mostrar_andares_hotel():
    andar_atual = 20

    while andar_atual >= 1:
        if andar_atual != 13:
            print("Andar:", andar_atual)
        andar_atual -= 1

mostrar_andares_hotel()