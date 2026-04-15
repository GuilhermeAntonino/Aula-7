from services.estoque import Estoque

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


# Teste
print(executar_rota("/produtos", "POST", {"nome": "Pizza", "quantidade": 10}))
print(executar_rota("/produtos", "GET"))