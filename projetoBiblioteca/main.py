import biblioteca

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
lista = []

while continuar != "sair":
    voltarMenu = " "
    print("1 - adcionar livros\n2 - atualizar quantidade de livros\n3 - sair")
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
        nome = str(input("Qual nome do livro que você quer ver os dados?: "))
        for l in livros:
            if l["nome"] == nome:
                print(f"O nome do livro é {l['nome']}\n"
                      f"Ele é {l['fisicoOuEletronico']}\n"
                      f"Lançado em {l['anoLancamento']}")

    elif escolha == 6:
        escolha = str(input('Como você quer buscar o livro? [ano, titulo, autor, assunto] ').lower())
        if escolha == 'ano':
            ano = int(input('Digite o ano para a pesquisa: '))
            for l in livros:
                if l['anoLancamento'] == ano:
                    lista.append(l['nome'])
            print(lista)
            lista.clear()
        elif escolha == 'titulo':
            titulo = input('Insira o titulo do livro: ').lower()
            for l in livros:
                if titulo in l['nome']:
                    lista.append(l['nome'])
            print(lista)
            lista.clear
        elif escolha == 'autor':
            autor = input('Insira o autor do livro: ').lower()
            for l in livros:
                if autor in l['autor']:
                    lista.append(l['nome'])
            print(lista)
            lista.clear
        elif escolha == 'assunto':
            assunto = input('Insira o assunto do livro: ').lower()
            for l in livros:
                if assunto in l['assunto']:
                    lista.append(l['nome'])
            print(lista)
            lista.clear

        
        