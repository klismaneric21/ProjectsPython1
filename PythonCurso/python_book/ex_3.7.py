try: #abre um bloco e tudo dentro deve estar identado (com 4 espaços)
    n1= int(input('Digite o primeiro número: '))
    n2= int(input('Digite o segundo número: '))
    soma = n1 + n2
    print(f'O resultado é: {soma}')
except ValueError: #deve ficar alinhado com try
    print('Por favor, digite apenas números inteiros.')