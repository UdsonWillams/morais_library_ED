import biblioteca

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
while continuar != "sair":
    voltarMenu = " "
    print("1 - adcionar livros\n2 - atualizar quantidade de livros\n3 - sair")
    escolha = int(input("Oque voce deseja? "))
    if escolha == 1:
        while voltarMenu != "menu":
            livro = biblioteca.cadastroDeLivros()
            livros.append(livro.copy())
            voltarMenu = str(input("Digite menu para voltar ao menu ou ENTER para continuar ").lower())

    if escolha == 2:
        nome = str(input("Qual nome do livro que você quer mudar a quantidade?: "))
        valor = int(input("Novo valor de quantidade do livro: "))
        for l in livros:
            if l["nome"] == nome:
                l["quantidade"] = valor
                print(f" O livro: {l['nome']} atualizou o valor para {l['quantidade']}")

    if escolha == 3:
        continuar = "sair"

    if escolha == 4:
        nome = str(input("Qual nome do livro que você quer ver os dados?: "))
        for l in livros:
            if l["nome"] == nome:
                print(f"O nome do livro é {l['nome']}\n"
                      f"Ele é {l['fisicoOuEletronico']}\n"
                      f"Lançado em {l['anoLancamento']}")
print(livros)
