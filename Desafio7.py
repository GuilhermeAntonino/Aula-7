class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def to_dict(self):
        return {"nome": self.nome, "quantidade": self.quantidade}


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.produtos.append(produto)
        return "Produto adicionado"

    def listar_produtos(self):
        return [p.to_dict() for p in self.produtos]


estoque = Estoque()

def get_produtos():
    return estoque.listar_produtos()

def post_produto(nome, quantidade):
    return estoque.adicionar_produto(nome, quantidade)

def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        return post_produto(dados["nome"], dados["quantidade"])

    return "Rota não encontrada"

print(executar_rota("/produtos", "POST", {"nome": "Pizza", "quantidade": 10}))
print(executar_rota("/produtos", "GET"))