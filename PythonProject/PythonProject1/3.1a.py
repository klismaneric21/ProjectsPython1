#tabela que identifica se número é inteiro ou ponto flutuante

quantidade =  int(input("Quantos números você quer inserir?: "))
print("\nNúmero\t\tTipo")
print("-" * 30)
for i in range(quantidade):
    valor = input("Digite um número: ")
    if "." in valor:
        numero =  float(valor)
        print(numero, "\t\tPonto Flutuante (float)")

    else:
        numero= int(valor)
        print(numero, "\t\tInteiro (int)")

