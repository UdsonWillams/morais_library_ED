import json

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


def menu():
    print("""
         |============================================================|
         |                SEJA BEM VINDO A MORAIS LIBRARY             |
         |============================================================|
         |  1 - Adcionar livros                                       |
         |  2 - Cadastrar categoria e tematica                        |
         |  3 - Atualizar quantidade de livros                        |
         |  4 - Remover titulos do acervo                             |
         |  5 - Mostrar dados do livro                                |
         |  6 - Buscar por exemplares[ano, titulo, autor, assunto]    |
         |  7 - Importar dados                                        |
         |  8 - Obter status de um livro                              |
         |  9 - Gerar relatórios                                      |
         |  10 - Alugar livro                                         |
         |  11 - Sair                                                 |
         |                                                            |  
         |============================================================|
           """)


def cadastroDeLivros():
    livrosCadastro = dict()

    livrosCadastro[NOME] = str(input("Nome do Livro: "))
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
    livrosCadastro[ANO_LANCAMENTO] = str(input("Qual o ano de lançamento: "))
    livrosCadastro[AUTOR] = str(input("Qual o autor do livro? "))
    livrosCadastro[ASSUNTO] = str(input("Qual o assunto do livro? "))
    livrosCadastro[ALUGADO] = "nao"
    livrosCadastro[DATA_ALUGUEL] = "NODATE"
    cat_tem = str(input("Deseja cadastrar a categoria e a tematica do livro? [S/N]").lower()[0])
    if cat_tem == "s":
        categoriaETematica(livrosCadastro)
    elif cat_tem == "n":
        livrosCadastro[CATEGORIA] = "NAO FORNECIDO"
        livrosCadastro[TEMATICA] = "NAO FORNECIDO"
        print("Livro cadastrado com sucesso!")

    return livrosCadastro


def escreveInfoLivro(relatorio, livro):
    if len(livro) == 0:
        pass
    elif livro[NOME] == "LIVRO EXCLUIDO":
        pass
    else:
        return relatorio.write(f"\n    Livro: {livro[NOME]} \n" +
                               f"    Autor: {livro[AUTOR]}\n" +
                               f"    Tipo: {livro[FISICO_OU_ELETRONICO]}\n" +
                               f"    Ano da Edição: {livro[ANO_LANCAMENTO]}\n" +
                               f"    Assunto: {livro[ASSUNTO]}\n" +
                               f"    Quantidade: {livro[QUANTIDADE]}\n" +
                               f"    Alugado:  {livro[ALUGADO]}\n" +
                               f"    Fim do Aluguel {livro[DATA_ALUGUEL]}\n")


def categoriaETematica(dicionario):
    dicionario[CATEGORIA] = str(input("Qual a categoria deste livro? "))
    dicionario[TEMATICA] = str(input("Qual a tematica deste livro? "))


def atualizarQuantidade(nome, valor, dicionario):
    for l in dicionario:
        if l[NOME] == nome:
            l[QUANTIDADE] = valor
            print(f" O livro: {l['nome']} atualizou o valor para {l['quantidade']}")


def removerTitulos(desejo, lista):
    cont1 = 0
    if desejo == 1:
        ano = int(input("Qual o ano desejado para a remoção? "))
        for i in range(0, len(lista)):
            for v in lista:
                if v[ANO_LANCAMENTO] == ano:
                    v.clear()
                    v[NOME] = "LIVRO EXCLUIDO"
                    v[FISICO_OU_ELETRONICO] = "Item excluido do acervo"
            ano -= 1
        print(f"Titulos até o ano de {ano} removidos")
    elif desejo == 2:
        nome = str(input("Qual o nome do livro desejado para a remoção? "))
        for v in lista:
            if v[NOME] == nome:
                v.clear()
                v[NOME] = "LIVRO EXCLUIDO"
            else:
                cont1 += 1
        if cont1 == len(lista):
            print("Livro não encontrado")
        else:
            print(f"Titulos com nome de {nome} removidos")


def alugarLivro(lista):
    nome = str(input("Qual o nome do livro desejado para o aluguel? "))
    for v in lista:
        if v[FISICO_OU_ELETRONICO] == "eletronico":
            print("Livro eletronico, não pode ser alugado fisicamente")
        elif v[NOME] == nome and v["fisicoOuEletronico"] == "fisico" and v[QUANTIDADE] > 1:
            if v[ALUGAVEL] == "sim":
                v[ALUGADO] = "sim"
                data = str(input("Diga a data de retorno do livro[EM FORMATO DD/MM/ANO]"))
                v[DATA_ALUGUEL] = data
                v[QUANTIDADE] -= 1
                print(f"Livro alugado, data de entrega {data}")
        elif v[QUANTIDADE] <= 1:
            print("Livro nao pode ser Alugado")


def escreverJson(dado):
    with open('arquivo1.json', 'w', encoding='utf8') as f:
        json.dump(dado, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


def lerJson1():
    with open('arquivo1.json', 'r', encoding='utf8') as f:
        return json.load(f)


def lerJson2():
    with open('arquivo2.json', 'r', encoding='utf8') as f:
        return json.load(f)
