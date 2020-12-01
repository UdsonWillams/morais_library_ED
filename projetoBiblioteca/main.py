import projetoBiblioteca.biblioteca
import projetoBiblioteca.telaLogin
from projetoBiblioteca import telaLogin

livro = dict()
livros = list()
continuar = " "
voltarMenu = " "
lista = []
cont1, cont2 = 0, 0
validaCT = None
gerarAcervo = None
gerarCategoria = None
gerarAssunto = None

'''
dicionario = {
    'nome': 'jose',
    'fisicoOuEletronico': 'fisico',
    'alugavel': 'sim',
    'reservavel': 'nao',
    'quantidade': 10,
    'anoLancamento': '2009',
    'autor': 'jose pedro',
    'assunto': 'drama',
    'alugado': 'nao',
    'categoria': "NAO FORNECIDO",
    'tematica': "NAO FORNECIDO",
    'dataAluguel': "SEM DADOS"
}
'''

iniciar = telaLogin.login()

if iniciar is True:
    while continuar != "sair":
        voltarMenu = " "
        projetoBiblioteca.biblioteca.menu()

        escolha = int(input("O que voce deseja? "))
        if escolha == 1:
            while voltarMenu != "menu":
                livro = projetoBiblioteca.biblioteca.cadastroDeLivros()
                livros.append(livro.copy())
                voltarMenu = str(input("Digite MENU para voltar ao menu ou ENTER para continuar ").lower())

        elif escolha == 2:
            ctnome = str(input("Nome do livro para alterar a categoria e a tematica"))
            for ct in livros:
                if ct['nome'] == ctnome:
                    projetoBiblioteca.biblioteca.categoriaETematica(ct)
                    validaCT = True
            if validaCT:
                print("Categoria e Tematica cadastrados com sucesso!")
            else:
                print("Não foi possivel cadastrar a categoria e a tematica")
            validaCT = None

        elif escolha == 3:
            nome = str(input("Qual nome do livro que você quer mudar a quantidade?: "))
            for a in livros:
                if a['nome'] == nome:
                    valor = int(input("Novo valor de quantidade do livro: "))
                    projetoBiblioteca.biblioteca.atualizarQuantidade(nome, valor, livros)
                else:
                    cont1 += 1
            if cont1 == len(livros):
                print("Livro nao encontrado")
                cont1 = 0

        elif escolha == 4:
            print("Deseja remover titulos do acervo por:"
                  "\n1 - Por Ano (obs:. Serao removido qualquer titulo de mesmo ano ou de anos anteriores ao desejado)"
                  "\n2 - Por titulo")
            desejo2 = int(input("Qual você deseja fazer? "))
            if desejo2 == 1:
                projetoBiblioteca.biblioteca.removerTitulos(desejo2, livros)
            if desejo2 == 2:
                projetoBiblioteca.biblioteca.removerTitulos(desejo2, livros)

        elif escolha == 5:
            nome = str(input("Qual nome do livro que você quer ver os dados?: "))
            for li in livros:
                if li["nome"] == nome:
                    print(f"O nome do livro é: {li['nome']}\n"
                          f"Ele é do tipo: {li['fisicoOuEletronico']}\n"
                          f"Lançado em: {li['anoLancamento']}\n"
                          f"Nome do autor: {li['autor']}\n"
                          f"Quantidade disponivel: {li['quantidade']}")

        elif escolha == 6:  # buscar livros
            escolha = str(input('Como você quer buscar o livro? [ano, titulo, autor, assunto] ').lower())
            if escolha == 'ano':
                ano = str(input('Digite o ano para a pesquisa: '))
                for l in livros:
                    if l['anoLancamento'] == ano:
                        lista.append(l['nome'])
                    else:
                        cont2 += 1
                if cont2 == len(livros):
                    print("Livro não encontrado no acervo")
                else:
                    print("Os livros encontrados foram: ")
                    print(lista)
                lista.clear()
                cont2 = 0

            elif escolha == 'titulo':
                titulo = input('Insira o titulo do livro: ').lower()
                for l in livros:
                    if titulo in l['nome'].lower():
                        lista.append(l['nome'])
                    else:
                        cont2 += 1
                if cont2 == len(livros):
                    print("Livro não encontrado no acervo")
                else:
                    print("Os livros encontrados foram: ")
                    print(lista)
                lista.clear()
                cont2 = 0

            elif escolha == 'autor':
                autor = input('Insira o autor do livro: ').lower()
                for l in livros:
                    if autor in l['autor'].lower():
                        lista.append(l['nome'])
                    else:
                        cont2 += 1
                if cont2 == len(livros):
                    print("Livro não encontrado no acervo")
                else:
                    print("Os livros encontrados foram: ")
                    print(lista)
                lista.clear()
                cont2 = 0

            elif escolha == 'assunto':
                assunto = input('Insira o assunto do livro: ').lower()
                for l in livros:
                    if assunto in l['assunto'].lower():
                        lista.append(l['nome'])
                    else:
                        cont2 += 1
                if cont2 == len(livros):
                    print("Livro não encontrado no acervo")
                else:
                    print("Os livros encontrados foram: ")
                    print(lista)
                lista.clear()
                cont2 = 0

        elif escolha == 7:  # importar dados
            dados1 = projetoBiblioteca.biblioteca.lerJson1()
            dados2 = projetoBiblioteca.biblioteca.lerJson2()
            livros.append(dados1)
            livros.append(dados2)
            print('Dados adicionados')

        elif escolha == 8:  # obter status do livro
            titulo = str(input('Insira o titulo do livro para saber sua situação: ').lower())
            for liv in livros:
                if liv['nome'] == titulo:
                    print(f"Situação do livro {liv['nome']} é:\n"
                          f"A Quantidade disponível: {liv['quantidade']}\n"
                          f"Esta alugado? :  {liv['alugado']}\n"
                          f"Fim do Aluguel {liv['dataAluguel']}")

        elif escolha == 9: #gerando relatorios
            print('1 - Gerar relatório do acervo \n2 - Gerar relatório por categoria \n' +
                  '3 - Gerar relatório por assunto')

            escolha3 = int(input('O que você deseja? '))
            if escolha3 == 1:
                for b in livros:
                    if len(livros) != 0 and b["nome"] != "LIVRO EXCLUIDO":
                        relatorio = open('relatorioDoAcervo.txt', 'w', encoding="utf8")
                        relatorio.writelines(f'RELATÓRIO DO ACERVO DA MORAIS LIBRARY \n\nQuantidade de livros: {len(livros)}')
                        gerarAcervo = True
                        for n in livros:
                            projetoBiblioteca.biblioteca.escreveInfoLivro(relatorio, n)
                        relatorio.close()
                if gerarAcervo:
                    print('Relatório do acervo gerado com sucesso!!')
                else:
                    print("Não foi possivel gerar o relatorio, sem dados no acervo")
                gerarAcervo = None

            elif escolha3 == 2:
                escolha4 = input('Digite a categoria a ser gerado o relatório: [A CATEGORIA -NAO FORNECIDO- É O PADRÃO'
                                 ' CASO NÃO TENHAM CADASTRADO NENHUMA]').lower()
                for c in livros:
                    if c['categoria'] == escolha4:
                        relatorio = open(f'Relatório - Categoria {escolha4}.txt', 'w', encoding="utf8")
                        relatorio.write(f'RELATÓRIO SOBRE A CATEGORIA {escolha4.upper()}\n\n')
                        for l in livros:
                            if escolha4 == l['categoria']:
                                projetoBiblioteca.biblioteca.escreveInfoLivro(relatorio, l)
                        relatorio.close()
                        gerarCategoria = True
                if gerarCategoria:
                    print('Relatório gerado com sucesso!!')
                else:
                    print("Não foi possivel gerar o relatorio, categoria não existente")
                gerarCategoria = None

            elif escolha3 == 3:
                escolha5 = input('Digite o assunto a ser gerado o relatório: ').lower()
                for d in livros:
                    if d['assunto'] == escolha5:
                        relatorio = open(f'Relatório - Assunto {escolha5}.txt', 'w', encoding="utf8")
                        relatorio.write(f'RELATÓRIO SOBRE O ASSUNTO {escolha5.upper()}\n\n')
                        for l in livros:
                            if escolha5 == l['assunto']:
                                projetoBiblioteca.biblioteca.escreveInfoLivro(relatorio, l)
                        relatorio.close()
                        gerarAssunto = True
                if gerarAssunto:
                    print('Relatório gerado com sucesso!!')
                else:
                    print("Não foi possivel gerar o relatorio, assunto não existente")
                gerarAssunto = None

        elif escolha == 10:
            projetoBiblioteca.biblioteca.alugarLivro(livros)

        elif escolha == 11:
            continuar = 'sair'
