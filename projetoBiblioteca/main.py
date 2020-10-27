import biblioteca

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
lista = []

while continuar != "sair":
    voltarMenu = " "
HEAD
    print("1 - Adcionar livros\n2 - Atualizar quantidade de livros\n3 -  Remover titulos do acervo"
          "\n4 - Mostrar dados do livro\n5 - Buscar por exemplares[ano, titulo, autor, assunto]"
          "\n6 - Importar dados \n7 - Obter status de um livro \n8 - Gerar relatórios \n10 - Sair")

    print("1 - Adcionar livros\n2 - Atualizar quantidade de livros \n6 - Buscar livros \n7 - Importar dados \n"+
        "8 - Obter status de um livro \n9 - Gerar relatório \n10 - Sair")
c4648cf54cf30e6ceeccca7af1a87a99c0ce4142
    escolha = int(input("O que voce deseja? "))
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
HEAD
        print("Deseja remover titulos do acervo por:"
              "\n1 - Por Ano (obs:. Serao removido qualquer titulo de mesmo ano ou de anos anteriores ao desejado)"
              "\n2 - Por titulo")
        desejo2 = int(input("Qual você deseja fazer? "))
        if desejo2 == 1:
            biblioteca.removerTitulos(desejo2, livros)
        if desejo2 == 2:
            biblioteca.removerTitulos(desejo2, livros)

    elif escolha == 4:

 c4648cf54cf30e6ceeccca7af1a87a99c0ce4142
        nome = str(input("Qual nome do livro que você quer ver os dados?: "))
        for l in livros:
            if l["nome"] == nome:
                print(f"O nome do livro é {l['nome']}\n"
                      f"Ele é {l['fisicoOuEletronico']}\n"
                      f"Lançado em {l['anoLancamento']}")

 HEAD
    elif escolha == 5:  # buscar livros

    elif escolha == 6: #buscar livros
 c4648cf54cf30e6ceeccca7af1a87a99c0ce4142
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
                if titulo in l['nome'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear
        elif escolha == 'autor':
            autor = input('Insira o autor do livro: ').lower()
            for l in livros:
                if autor in l['autor'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear
        elif escolha == 'assunto':
            assunto = input('Insira o assunto do livro: ').lower()
            for l in livros:
                if assunto in l['assunto'].lower():
                    lista.append(l['nome'])
            print(lista)
            lista.clear
HEAD

    elif escolha == 6:  # importar dados
        pass

    elif escolha == 7:  # obter status do livro
        titulo = input('Insira o titulo do livro para saber sua situação: ').lower
        for l in livros:
            if titulo == l['nome']:
                print(f"Situação do livro {l['nome']}\n"
                      f"Quantidade disponível: {l['quantidade']}\n")

    elif escolha == 8:
        print('1 - Gerar relatório do acervo \n2 - Gerar relatório por categoria \n' +
              '3 - Gerar relatório por assunto')
        escolha3 = int(input('O que você deseja? '))
        if escolha3 == 1:
            print('Gerando relatório...')
            relatorio = open('relatorio do acervo.txt', 'w', encoding="utf8")
            relatorio.writelines('RELATÓRIO DO ACERVO DA MORAIS LIBRARY \n\n')

            for l in livros:
                if l["fisicoOuEletronico"] == "eletronico":
                    l['quantidade'] = "Livro em formato Eletronico"
                relatorio.writelines(f"Livro: {l['nome']} \n" +
                                     f"    Autor: {l['autor']}\n" +
                                     f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                     f"    Ano da Edição: {l['anoLancamento']}\n" +
                                     f"    Assunto: {l['assunto']}\n" +
                                     f"    Quantidade: {l['quantidade']}\n"
                                     )
            relatorio.close()
            print('Relatório gerado com sucesso!!')
        elif escolha3 == 2:
            escolha3 = input('Digite a categoria a ser gerado o relatório: ').lower()
            print('Gerando relatório...')
            relatorio = open(f'Relatório - Categoria {escolha3}.txt', 'w', encoding="utf8")
            relatorio.write(f'RELATÓRIO SOBRE A CATEGORIA {escolha3.upper()}\n')

            for l in livros:
                if escolha3 == l['categoria']:
                    relatorio.write(f"Livro: {l['nome']} \n" +
                                    f"    Autor: {l['autor']}\n" +
                                    f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                    f"    Ano da Edição: {l['ano']}\n" +
                                    f"    Assunto: {l['assunto']}\n" +
                                    f"    Quantidade: {l['quantidade']}\n"
                                    )

            print('Relatório gerado com sucesso!!')

        elif escolha3 == 3:
            escolha3 = input('Digite o assunto a ser gerado o relatório: ').lower()
            print('Gerando relatório...')
            relatorio = open(f'Relatório - Assunto {escolha3}.txt', 'w', encoding="utf8")
            relatorio.write(f'RELATÓRIO SOBRE O ASSUNTO {escolha3.upper()}')
            for l in livros:
                if escolha3 == l['assunto']:
                    relatorio.write(f"Livro: {l['nome']} \n" +
                                    f"    Autor: {l['autor']}\n" +
                                    f"    Tipo: {l['fisicoOuEletronico']}\n" +
                                    f"    Ano da Edição: {l['ano']}\n" +
                                    f"    Assunto: {l['assunto']}\n" +
                                    f"    Quantidade: {l['quantidade']}\n"
                                    )

            print('Relatório gerado com sucesso!!')

    elif escolha == 10:
        continuar = 'sair'
        
    elif escolha == 7: #importar dados
        pass

    elif escolha == 8: #obter status do livro
        titulo = input('Insira o titulo do livro para saber sua situação: ').lower
        for l in livros:
                if titulo == l['nome']:
                    print(f"Situação do livro {l['nome']}\n"
                      f"Quantidade disponível: {l['quantidade']}\n")

    elif escolha == 9:
        print('1 - Gerar relatório do acervo \n2 - Gerar relatório por categoria \n'+
                        '3 - Gerar relatório por assunto')
        escolha = int(input('O que você deseja? '))
        if escolha == 1:
            print('Gerando relatório...')
            relatorio = open('Relatório do Acervo.txt', 'w')
            relatorio.writelines('RELATÓRIO DO ACERVO DA MORAIS LIBRARY \n\n')
            
            for l in livros:
                relatorio.writelines(f"Livro: {l['nome']} \n"+
                                f"    Autor: {l['autor']}\n"+
                                f"    Tipo: {l['fisicoOuEletronico']}\n"+
                                f"    Ano da Edição: {l['anoLancamento']}\n"+
                                f"    Assunto: {l['assunto']}\n"+
                                f"    Quantidade: {l['quantidade']}\n"
                )

            print('Relatório gerado com sucesso!!')
        elif escolha == 2:
            escolha = input('Digite a categoria a ser gerado o relatório: ').lower()
            print('Gerando relatório...')
            relatorio = open(f'Relatório - Categoria {escolha}.txt', 'w')
            relatorio.write(f'RELATÓRIO SOBRE A CATEGORIA {escolha.upper()}')

            for l in livros:
                if escolha == l['categoria']:
                    relatorio.write(f"Livro: {l['nome']} \n"+
                                f"    Autor: {l['autor']}\n"+
                                f"    Tipo: {l['fisicoOuEletronico']}\n"+
                                f"    Ano da Edição: {l['ano']}\n"+
                                f"    Assunto: {l['assunto']}\n"+
                                f"    Quantidade: {l['quantidade']}\n"
                )
            
            print('Relatório gerado com sucesso!!')

    elif escolha == 3:
        escolha = input('Digite o assunto a ser gerado o relatório: ').lower()
        print('Gerando relatório...')
        relatorio = open(f'Relatório - Assunto {escolha}.txt', 'w')
        relatorio.write(f'RELATÓRIO SOBRE O ASSUNTO {escolha.upper()}')       
        for l in livros:
            if escolha == l['assunto']:
                relatorio.write(f"Livro: {l['nome']} \n"+
                            f"    Autor: {l['autor']}\n"+
                            f"    Tipo: {l['fisicoOuEletronico']}\n"+
                            f"    Ano da Edição: {l['ano']}\n"+
                            f"    Assunto: {l['assunto']}\n"+
                            f"    Quantidade: {l['quantidade']}\n"
            )
        
        print('Relatório gerado com sucesso!!')

    elif escolha == 10:
        continuar = 'sair'
c4648cf54cf30e6ceeccca7af1a87a99c0ce4142
