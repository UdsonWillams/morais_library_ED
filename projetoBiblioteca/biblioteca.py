TEMATICA = "tematica"
QUANTIDADE = 'quantidade'
FISICO_OU_ELETRONICO = "fisicoOuEletronico"
CATEGORIA = "categoria"
DATA_ALUGUEL = "dataAluguel"
ALUGADO = "alugado"
ASSUNTO = "assunto"
AUTOR = "autor"
ANO_LANCAMENTO = "anoLancamento"
QUANTIDADE = "quantidade"
RESERVAVEL = "reservavel"
ALUGAVEL = "alugavel"
NOME = "nome"

def cadastroDeLivros():
    livrosCadastro = dict()

    livrosCadastro[NOME] = str(input("Digite o nome: "))
    livrosCadastro[FISICO_OU_ELETRONICO] = str(input("Livro fisico ou eletronico?: "))

    while livrosCadastro[FISICO_OU_ELETRONICO] != "fisico" and livrosCadastro[FISICO_OU_ELETRONICO] != "eletronico":
        print("VALOR INVALIDO, DIGA APENAS SE É FISICO OU ELETRONICO ")
        livrosCadastro[FISICO_OU_ELETRONICO] = str(input("Livro fisico ou eletronico?: "))
    if livrosCadastro[FISICO_OU_ELETRONICO] == "eletronico":
        livrosCadastro[QUANTIDADE] = "Livro em formato Eletronico"
    if livrosCadastro[FISICO_OU_ELETRONICO] == "fisico":
        livrosCadastro[ALUGAVEL] = str(input("Este livro é alugavel?: "))
        livrosCadastro[RESERVAVEL] = str(input("Este livro é reservavel?: "))
        livrosCadastro[QUANTIDADE] = int(input("Quantidade de livros: "))
    livrosCadastro[ANO_LANCAMENTO] = int(input("Qual o ano de lançamento: "))
    livrosCadastro[AUTOR] = str(input("Qual o autor do livro? "))
    livrosCadastro[ASSUNTO] = str(input("Qual o assunto do livro? "))
    livrosCadastro[ALUGADO] = "nao"
    livrosCadastro[DATA_ALUGUEL] = "NODATE"
    cat_tem = str(input("Deseja cadastrar a categoria e a tematica do livro? [S/N]").lower()[0])
    if cat_tem == "s":
        categoriaETematica(livrosCadastro)
    elif cat_tem == "n":
        livrosCadastro[CATEGORIA] = "NAO FORNECIDO"
        print("Livro cadastrado com sucesso!")
    return livrosCadastro


def categoriaETematica(dicionario):
    dicionario[CATEGORIA] = str(input("Qual a categoria deste livro? "))
    dicionario[TEMATICA] = str(input("Qual a tematica deste livro? "))


def atualizarQuantidade(nome, valor, dicionario):
    for l in dicionario:
        if l[NOME] == nome:
            l[QUANTIDADE] = valor
            print(f" O livro: {l['nome']} atualizou o valor para {l['quantidade']}")


def removerTitulos(desejo, lista):
    if desejo == 1:
        ano = int(input("Qual o ano desejado para a remoção? "))
        for i in range(0, len(lista)):
            for v in lista:
                if v[ANO_LANCAMENTO] == ano:
                    v.clear()
                    v[FISICO_OU_ELETRONICO] = "Item excluido do acervo"
            ano -= 1
        print(f"Titulos até o ano de {ano} removidos")
    elif desejo == 2:
        nome = str(input("Qual o nome do livro desejado para a remoção? "))
        for v in lista:
            if v[NOME] == nome:
                v.clear()
        print(f"Titulos com nome de {nome} removidos")


def alugarLivro(lista):
    nome = str(input("Qual o nome do livro desejado para o aluguel? "))
    for v in lista:
        if v[FISICO_OU_ELETRONICO] == "eletronico":
            print("Livro eletronico, não pode ser alugado")
        elif v[NOME] == nome and v["fisicoOuEletronico"] == "fisico":
            if v[ALUGAVEL] == "sim":
                v[ALUGADO] = "sim"
                data = str(input("Diga a data de retorno do livro[EM FORMATO DD/MM/ANO]"))
                v[DATA_ALUGUEL] = data
                print(f"Livro alugado, data de entrega {data}")
            else:
                print("O livro não pode ser alugado")
