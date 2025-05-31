import os

HISTORICO = "historico.txt"

def salvar_historico(operacao, resultado):
    with open(HISTORICO, "a") as arquivo:
        arquivo.write(f"{operacao} = {resultado}\n")

def exibir_historico():
    limpar_tela()
    print("-" * 50)
    print(" " * 15 + "Histórico de Cálculos")
    print("-" * 50)
    if not os.path.exists(HISTORICO):
        print("Nenhum histórico encontrado.")
    else:
        with open(HISTORICO, "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip() == "":
                print("Nenhum histórico encontrado.")
            else:
                print(conteudo)
    print("-" * 50)
    input("Pressione Enter para voltar ao menu...")

def deletar_historico():
    with open("historico.txt","w") as arquivo:
        pass
        # arquivo.write("")

print("Histórico deletado com sucesso.")    

# def arquivo(nome_do_arquivo):
#     if os.path.isfile(nome_do_arquivo):
#         return True
#     else:
#         return False

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")




def ler_historico(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
       
            history = file.readlines()
            history = [line.strip() for line in history]
            return history
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
        return None
    except PermissionError:
        print(f"Erro: Permissão negada para acessar '{file_path}'.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {str(e)}")
        return None
    
