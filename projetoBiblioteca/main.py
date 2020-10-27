import biblioteca

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
while continuar != "sair":
    voltarMenu = " "
    print("1 - adcionar livros\n2 - atualizar quantidade de livros\n3 - Remover titulos\n4 - sair")
    escolha = int(input("Oque voce deseja? "))
    if escolha == 1:
        while voltarMenu != "menu":
            livro = biblioteca.cadastroDeLivros()
            livros.append(livro.copy())
            voltarMenu = str(input("Digite menu para voltar ao menu ou ENTER para continuar ").lower())

    elif escolha == 2:
        nome = str(input("Qual nome do livro que você quer mudar a quantidade?: "))
        valor = int(input("Novo valor de quantidade do livro: "))
        for l in livros:
            if l["nome"] == nome:
                l["quantidade"] = valor
                print(f" O livro: {l['nome']} atualizou o valor para {l['quantidade']}")

    elif escolha == 3:
        print("Deseja remover titulos do acervo por:"
              "\n1 - Por Ano (obs:. Serao removido qualquer titulo de mesmo ano ou de anos anteriores ao desejado)"
              "\n2 - Por titulo")
        desejo2 = int(input("Qual você deseja fazer? "))
        if desejo2 == 1:
            biblioteca.removerTitulos(desejo2, livros)
        if desejo2 == 2:
            biblioteca.removerTitulos(desejo2, livros)

    elif escolha == 4:
        continuar = "sair"
