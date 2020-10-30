import PySimpleGUI as sg


def login():
    sg.theme("Reddit")
    layout = [
        [sg.Text('Usuario')],
        [sg.InputText(key="loginUsuario")],
        [sg.Text('Senha')],
        [sg.Input(password_char="*", key="loginSenha")],
        [sg.Button("Logar")]
    ]

    janela = sg.Window("Login", layout)
    continuar = None

    verdadeiro = True
    while verdadeiro:
        evento, valores = janela.read()
        # fecha a janela caso voce feche no X
        if evento == sg.WIN_CLOSED:
            continuar = False
            break
        if evento == "Logar":
            if valores["loginUsuario"] == "admin" and valores["loginSenha"] == "123":
                sg.popup("Olá Admin, já pode começar a usar o sistema da Morais Library")
                continuar = True
                verdadeiro = False
            else:
                sg.popup("usuario ou senha invalidos")
                continuar = False
                verdadeiro = True
    janela.close()
    return continuar
