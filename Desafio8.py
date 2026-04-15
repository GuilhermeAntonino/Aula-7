class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


class ProdutoDigital(Produto):
    def __init__(self, nome, quantidade, tamanho_arquivo):
        super().__init__(nome, quantidade)
        self.tamanho_arquivo = tamanho_arquivo


p1 = ProdutoDigital("Curso Python", 1, "500MB")
print(p1.nome)
print(p1.quantidade)
print(p1.tamanho_arquivo)