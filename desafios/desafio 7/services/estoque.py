from models.produtos import Produto


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.produtos.append(produto)
        return "Produto adicionado"

    def listar_produtos(self):
        return [p.to_dict() for p in self.produtos]