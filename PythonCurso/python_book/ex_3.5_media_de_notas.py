matéria_1 = float(input('Digite a primeira nota: '))
matéria_2 = float(input('Digite a segunda nota: '))
matéria_3 = float(input('Digite a terceira nota: '))
aprovado = (matéria_1 >= 7) and (matéria_2 >= 7) and (matéria_3 >= 7)
if aprovado:
    print('Aprovado.')
else:
    print('Reprovado.')
