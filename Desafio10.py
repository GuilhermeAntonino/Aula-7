def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()

    if rota == "/produtos" and metodo == "POST":
        if not dados or "nome" not in dados or "quantidade" not in dados:
            return "Dados inválidos"
        return post_produto(dados["nome"], dados["quantidade"])

    if rota == "/produtos/buscar" and metodo == "GET":
        if not dados or "nome" not in dados:
            return "Dados inválidos"
        return get_produto_por_nome(dados["nome"])

    return "Rota não encontrada"