class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return "Produto não encontrado"]
        