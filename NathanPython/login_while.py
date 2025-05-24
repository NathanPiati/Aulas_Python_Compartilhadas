from os import system as limp
limp("cls")


usuario_correto = "admin"
senha_correta = "python123"

while True:
    usuario = input("Digite o usuario: ")

    if usuario != usuario_correto:
        print("Seu usuário incorreto, tente novamente!")

    else:
        senha_digitada = input("Digite a senha: ")

        if senha_digitada != senha_correta:
            print("Senha incorreta, tente novamente!")
        else:
            print("Senha correta!")
            print("Acesso liberado!")
            break


