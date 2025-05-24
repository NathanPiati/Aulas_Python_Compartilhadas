from datetime import date
import customtkinter as ctk


tela = ctk.CTk()
tela.title("Validador de Idade")
tela.geometry("500x200")
ctk.set_appearance_mode("dark")


frame_botoes = ctk.CTkFrame(tela)
frame_botoes.pack(side="bottom")

lebel_anoNasc = ctk.CTkLabel(tela, text="Digite o ano do seu nascimento no formato XX/XX/XXXX:")
lebel_anoNasc.pack()

input_anoNasc = ctk.CTkEntry(tela, placeholder_text="Digite o ano do seu nascimento")
input_anoNasc.pack()

resultado = ctk.CTkLabel(tela, text="Resultado:")
resultado.pack()    


def calcular():
    ano_atual = date.today().year
    try:
        dia, mes, ano_nasc = map(int, input_anoNasc.get().split('/'))
        idade = ano_atual - ano_nasc
        if idade >= 18:
            resultado.configure(text="Pode entrar na festa! Beba sem moderação!")
        else:
            resultado.configure(text="Não pode entrar na festa! Vou chamar sua mãe!")
    except ValueError:
        resultado.configure(text="Erro: Data inválida!")


botao_validar = ctk.CTkButton(frame_botoes, text="Validar", command=calcular)
botao_validar.pack()

tela.mainloop()

