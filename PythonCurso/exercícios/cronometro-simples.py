import time

tempo=int(input('Digite o tempo em segundos: '))

for i in range(tempo, 0, -1):
    print(f"⏳ Faltam {i} segundos...")
    time.sleep(1)

print("Tempo acabou!")