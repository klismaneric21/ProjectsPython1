class Produto:
    def __init__(self, nome: str, preco: float, estoque: int, id: int = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __repr__(self):
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco}, estoque={self.estoque})"
