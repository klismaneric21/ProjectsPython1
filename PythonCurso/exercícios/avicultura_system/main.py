from database.connection import create_tables
from models.produto import Produto
from services.produto_service import cadastrar_produto, listar_produtos


def main():
    create_tables()

    print("=== Cadastro de Produto ===")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))

    produto = Produto(nome=nome, preco=preco, estoque=estoque)
    cadastrar_produto(produto)

    print("\n=== Produtos cadastrados ===")
    produtos = listar_produtos()
    for p in produtos:
        print(p)


if __name__ == "__main__":
    main()
