# dissecando uma variável

objeto = input('Digite o nome do objeto: ')
print('O objeto é do tipo primivito ', type(objeto))
print('É número? ', objeto.isnumeric())
print('Tem espaços?', objeto.isspace())
print('Está em letra minuscula? ', objeto.islower())
print('Está em letra maiscula? ', objeto.isupper())
print('Está captalizada? ', objeto.istitle())
print('É alphanumerico? ', objeto.isalpha())