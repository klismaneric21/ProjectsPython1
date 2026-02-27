#tabela para identificar e marcar se número é inteiro ou flutuante

numeros = [5, 5.0, 4.3, -2, 100, 1.333]

for n in numeros:
    if isinstance(n, int):
        print(n, "-> Inteiro (int)")
    elif isinstance(n, float):
        print(n, "-> Ponto flutuante (float)")