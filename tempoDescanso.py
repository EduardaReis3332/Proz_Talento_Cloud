import time

tempoInicial = 1
tempoFinal = 45

print("Iniciando o descanso...")

for i in range(tempoInicial, tempoFinal + 1):
    print(i)
    time.sleep(1)

print("Fim descanso!")