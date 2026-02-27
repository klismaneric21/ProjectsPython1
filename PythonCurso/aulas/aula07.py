# Ordem de Precedência (Operadores aritiméticos)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto vale {}, a divisão vale {}'.format(s, m, d), end='')
print(' \n A divisão inteira é {}, \n a Exponênciação é {}'.format(di, e))