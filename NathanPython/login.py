from datetime import date
import customtkinter as ctk

tela_login = ctk.CTk()
tela_login.title("tela de login")
tela_login.geometry("500x300")
ctk.set_appearance_mode("dark")


label_bemvindo = ctk.CTkLabel(tela_login, text="Bem vindo ao login")
label_bemvindo.pack()

frame_botoes = ctk.CTkFrame(tela_login)
frame_botoes.pack(side="bottom")

lebel_usuario = ctk.CTkLabel(tela_login, text="Digite seu usuário:")
lebel_usuario.pack()

input_usuario = ctk.CTkEntry(tela_login, placeholder_text="Usuario")
input_usuario.pack()


label_senha = ctk.CTkLabel(tela_login, text="Digite sua senha:")
label_senha.pack()

input_senha = ctk.CTkEntry(tela_login, placeholder_text="Senha", show="*")
input_senha.pack()  

resultado = ctk.CTkLabel(tela_login, text="Resultado:")
resultado.pack()

def calcular():
    senha = input_senha.get()
    if senha == "python123":
        resultado.configure(text="Acesso liberado!") 
    else:
        resultado.configure(text="Acesso negado!")  


botao_validar = ctk.CTkButton(frame_botoes, text="Validar", command=calcular)
botao_validar.pack()



tela_login.mainloop()
  