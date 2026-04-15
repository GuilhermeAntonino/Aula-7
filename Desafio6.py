class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def atualizar_quantidade(self, nome, nova_quantidade):
        if not isinstance(nova_quantidade, int) or nova_quantidade < 0:
            return "Quantidade inválida"

        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                return "Quantidade atualizada"
        return "Produto não encontrado"

p1 = Produto("Pizza", 10)
estoque = Estoque()
estoque.adicionar_produto(p1)

print(estoque.atualizar_quantidade("Pizza", -5))
print(p1.quantidade)