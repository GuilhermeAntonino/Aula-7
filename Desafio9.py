class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def apresentar(self):
        return f"Produto: {self.nome} - {self.quantidade}"


class ProdutoPerecivel(Produto):
    def apresentar(self):
        return f"Perecível: {self.nome} - {self.quantidade}"


class ProdutoDigital(Produto):
    def apresentar(self):
        return f"Digital: {self.nome} - {self.quantidade}"


produtos = [
    ProdutoPerecivel("Leite", 5),
    ProdutoDigital("Curso", 1)
]

for p in produtos:
    print(p.apresentar())