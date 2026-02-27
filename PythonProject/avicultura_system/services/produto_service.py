from database.connection import get_connection
from models.produto import Produto


def cadastrar_produto(produto: Produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco, estoque)
        VALUES (?, ?, ?)
    """, (produto.nome, produto.preco, produto.estoque))

    conn.commit()
    conn.close()


def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
    rows = cursor.fetchall()

    produtos = []
    for row in rows:
        produto = Produto(id=row[0], nome=row[1], preco=row[2], estoque=row[3])
        produtos.append(produto)

    conn.close()
    return produtos
