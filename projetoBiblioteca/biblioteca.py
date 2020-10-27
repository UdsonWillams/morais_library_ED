def cadastroDeLivros():
    livrosCadastro = dict()

    livrosCadastro["nome"] = str(input("Digite o nome: "))
    livrosCadastro["fisicoOuEletronico"] = str(input("Livro fisico ou eletronico?: "))

    while livrosCadastro["fisicoOuEletronico"] != "fisico" and livrosCadastro["fisicoOuEletronico"] != "eletronico":
        print("VALOR INVALIDO, DIGA APENAS SE É FISICO OU ELETRONICO ")
        livrosCadastro["fisicoOuEletronico"] = str(input("Livro fisico ou eletronico?: "))
    if livrosCadastro["fisicoOuEletronico"] == "eletronico":
        livrosCadastro['quantidade'] = "Livro em formato Eletronico"
    if livrosCadastro["fisicoOuEletronico"] == "fisico":
        livrosCadastro["alugavel"] = str(input("Este livro é alugavel?: "))
        livrosCadastro["reservavel"] = str(input("Este livro é reservavel?: "))
        livrosCadastro["quantidade"] = int(input("Quantidade de livros: "))
    livrosCadastro["anoLancamento"] = int(input("Qual o ano de lançamento: "))
    livrosCadastro["autor"] = str(input("Qual o autor do livro? "))
    livrosCadastro["assunto"] = str(input("Qual o assunto do livro? "))
    livrosCadastro["alugado"] = "nao"
    livrosCadastro["dataAluguel"] = "NODATE"
    cat_tem = str(input("Deseja cadastrar a categoria e a tematica do livro? [S/N]").lower()[0])
    if cat_tem == "s":
        categoriaETematica(livrosCadastro)
    elif cat_tem == "n":
        livrosCadastro["categoria"] = "NAO FORNECIDO"
        print("Livro cadastrado com sucesso!")
    return livrosCadastro


def categoriaETematica(dicionario):
    dicionario["categoria"] = str(input("Qual a categoria deste livro? "))
    dicionario["tematica"] = str(input("Qual a tematica deste livro? "))


def atualizarQuantidade(nome, valor, dicionario):
    for l in dicionario:
        if l["nome"] == nome:
            l["quantidade"] = valor
            print(f" O livro: {l['nome']} atualizou o valor para {l['quantidade']}")


def removerTitulos(desejo, lista):
    if desejo == 1:
        ano = int(input("Qual o ano desejado para a remoção? "))
        for i in range(0, len(lista)):
            for v in lista:
                if v["anoLancamento"] == ano:
                    v.clear()
                    v["fisicoOuEletronico"] = "Item excluido do acervo"
            ano -= 1
        print(f"Titulos até o ano de {ano} removidos")
    elif desejo == 2:
        nome = str(input("Qual o nome do livro desejado para a remoção? "))
        for v in lista:
            if v["nome"] == nome:
                v.clear()
        print(f"Titulos com nome de {nome} removidos")


def alugarLivro(lista):
    nome = str(input("Qual o nome do livro desejado para o aluguel? "))
    for v in lista:
        if v["fisicoOuEletronico"] == "eletronico":
            print("Livro eletronico, não pode ser alugado")
        elif v["nome"] == nome and v["fisicoOuEletronico"] == "fisico":
            if v["alugavel"] == "sim":
                v["alugado"] = "sim"
                data = str(input("Diga a data de retorno do livro[EM FORMATO DD/MM/ANO]"))
                v["dataAluguel"] = data
                print(f"Livro alugado, data de entrega {data}")
            else:
                print("O livro não pode ser alugado")
