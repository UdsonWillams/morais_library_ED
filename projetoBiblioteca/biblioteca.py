def cadastroDeLivros():
    livrosCadastro = dict()

    livrosCadastro["nome"] = str(input("Digite o nome: "))
    livrosCadastro["fisicoOuEletronico"] = str(input("Livro fisico ou eletronico?: "))

    while livrosCadastro["fisicoOuEletronico"] != "fisico" and livrosCadastro["fisicoOuEletronico"] != "eletronico":
        print("VALOR INVALIDO, DIGA APENAS SE É FISICO OU ELETRONICO ")
        livrosCadastro["fisicoOuEletronico"] = str(input("Livro fisico ou eletronico?: "))
    if livrosCadastro["fisicoOuEletronico"] == "fisico":
        livrosCadastro["alugavel"] = str(input("Este livro é alugavel?: "))
        livrosCadastro["reservavel"] = str(input("Este livro é reservavel?: "))
        livrosCadastro["quantidade"] = int(input("Quantidade de livros: "))
    livrosCadastro["anoLancamento"] = int(input("Qual o ano de lançamento: "))
    livrosCadastro["autor"] = str(input("Qual o autor do livro? "))
    livrosCadastro["assunto"] = str(input("Qual o assunto do livro? "))
    cat_tem = str(input("Deseja cadastrar a categoria e a tematica do livro? [S/N]").lower()[0])
    if cat_tem == "s":
        categoriaETematica(livrosCadastro)
    elif cat_tem == "n":
        print("Livro cadastrado com sucesso!")
    return livrosCadastro


def categoriaETematica(dicionario):
    dicionario["categoria"] = str(input("Qual a categoria deste livro? "))
    dicionario["tematica"] = str(input("Qual a tematica deste livro? "))


def atualizarAcervo(dicionario):
    dicionario["quantidade"] = int(input("Qual a nova quantidade? "))


def removerTitulos(desejo, lista):
    nomes = []
    if desejo == 1:
        ano = int(input("Qual o ano desejado para a remoção? "))
        for v in lista:
            if v["fisicoOuEletronico"] <= ano:
                v.clear()
        print(f"Titulos do ano de {ano} removidos")
    elif desejo == 2:
        nome = str(input("Qual o nome do livro desejado para a remoção? "))
        for v in lista:
            if v["nome"] == nome:
                v.clear()
        print(f"Titulos com nome de {nome} removidos")
