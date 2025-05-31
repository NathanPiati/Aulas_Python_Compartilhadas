from os import system as limp
import os
import datetime
import getpass

limp("cls")

def gerar_codigo_usuario():
    return f"ID{str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))[-4:]}"

def capturar_informacoes_usuario():
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    email = input("Digite o seu email: ")
    return {"Nome": nome, "Idade": idade, "Email": email}

def salvar_informacoes_usuario(usuario, codigo):
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("C:\\Users\\Aluno\\Desktop\\NathanPython\\Projetodados\\teste.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Código: {codigo}, Nome: {usuario['Nome']}, Idade: {usuario['Idade']}, Email: {usuario['Email']}, Data: {data_atual}\n")

def ler_arquivo():
    with open("C:\\Users\\Aluno\\Desktop\\NathanPython\\Projetodados\\teste.txt", "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def ler_registro_especifico():
    codigo = input("Digite o código do registro que deseja ler: ")
    with open("C:\\Users\\Aluno\\Desktop\\NathanPython\\Projetodados\\teste.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith(f"Código: {codigo}"):
                print("\nConteúdo do registro:\n")
                print(linha)
                return
    print("Registro não encontrado!")

def deletar_registro():
    senha = getpass.getpass("Digite a senha do usuário: ")
    if senha == "123456":
        codigo = input("Digite o código do registro que deseja deletar: ")
        with open("C:\\Users\\Aluno\\Desktop\\NathanPython\\Projetodados\\teste.txt", "r+", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            arquivo.seek(0)
            for linha in conteudo:
                if not linha.startswith(f"Código: {codigo}"):
                    arquivo.write(linha)
                arquivo.truncate()
        print("Registro deletado com sucesso!")
    else:
        print("Senha incorreta!")

if __name__ == "__main__":
    print("Data e hora atual:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("Diretório atual:", os.getcwd())

    while True:
        print("\n" + "*" * 50)
        print("  MENU  ".center(50, "*"))
        print("*" * 50)
        print(" 1 - Inserir dados  ".center(50))
        print(" 2 - Ler dados  ".center(50))
        print(" 3 - Ler dados específicos  ".center(50))
        print(" 4 - Deletar dados  ".center(50))
        print(" 5 - Sair  ".center(50))
        print("*" * 50)
        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            usuario = capturar_informacoes_usuario()
            codigo = gerar_codigo_usuario()
            salvar_informacoes_usuario(usuario, codigo)
            print("\nArquivo 'teste.txt' foi salvo com sucesso.")
        elif escolha == "2":
            print("\nNovo conteúdo do arquivo:\n")
            print(ler_arquivo())
        elif escolha == "3":
            ler_registro_especifico()
        elif escolha == "4":
            deletar_registro()
        elif escolha == "5":
            break
        else:
            print("Opção inválida!")

