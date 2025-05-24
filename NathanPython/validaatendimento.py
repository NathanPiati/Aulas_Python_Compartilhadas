import tkinter as tk
from tkinter import messagebox

class ValidadorAtendimento:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Atendimento")
        self.root.geometry("600x400")  # Aumentar o tamanho da janela principal

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label="Cadastrar Paciente", command=self.abrir_cadastro)
        menu.add_command(label="Pré Atendimento", command=self.abrir_pre_atendimento)

        self.clientes = []

    def abrir_cadastro(self):
        self.janela_cadastro = tk.Toplevel(self.root)
        self.janela_cadastro.title("Cadastro de Paciente")
        self.janela_cadastro.geometry("350x250")  # Aumentar o tamanho da janela de cadastro

        self.label_nome = tk.Label(self.janela_cadastro, text="Nome:")
        self.label_nome.grid(column=0, row=0)

        self.entry_nome = tk.Entry(self.janela_cadastro)
        self.entry_nome.grid(column=1, row=0)

        self.label_cpf = tk.Label(self.janela_cadastro, text="CPF:")
        self.label_cpf.grid(column=0, row=1)

        self.entry_cpf = tk.Entry(self.janela_cadastro)
        self.entry_cpf.grid(column=1, row=1)

        self.button_salvar = tk.Button(self.janela_cadastro, text="Salvar", command=self.salvar_cliente)
        self.button_salvar.grid(column=1, row=2)

    def abrir_pre_atendimento(self):
        self.janela_pre_atendimento = tk.Toplevel(self.root)
        self.janela_pre_atendimento.title("Pré Atendimento")
        self.janela_pre_atendimento.geometry("350x250")  # Aumentar o tamanho da janela de pré-atendimento

        self.label_cliente = tk.Label(self.janela_pre_atendimento, text="Paciente:")
        self.label_cliente.grid(column=0, row=0)

        self.combo_cliente = tk.StringVar()
        if self.clientes:
            self.combo_cliente.set(self.clientes[0]["nome"])
        self.combobox_cliente = tk.OptionMenu(self.janela_pre_atendimento, self.combo_cliente, *self.clientes)
        self.combobox_cliente.grid(column=1, row=0)

        self.button_selecionar = tk.Button(self.janela_pre_atendimento, text="Selecionar", command=self.selecionar_cliente)
        self.button_selecionar.grid(column=1, row=1)

    def criar_campos_atendimento(self):
        self.frame_atendimento = tk.Frame(self.janela_pre_atendimento)
        self.frame_atendimento.grid(column=0, row=5, columnspan=2)

        self.label_temp = tk.Label(self.frame_atendimento, text="Temperatura:")
        self.label_temp.grid(column=0, row=0)

        self.entry_temp = tk.Entry(self.frame_atendimento)
        self.entry_temp.grid(column=1, row=0)

        self.label_bat = tk.Label(self.frame_atendimento, text="Batimentos:")
        self.label_bat.grid(column=0, row=1)

        self.entry_bat = tk.Entry(self.frame_atendimento)
        self.entry_bat.grid(column=1, row=1)

        self.label_pressao = tk.Label(self.frame_atendimento, text="Pressão:")
        self.label_pressao.grid(column=0, row=2)

        self.entry_pressao = tk.Entry(self.frame_atendimento)
        self.entry_pressao.grid(column=1, row=2)

        self.button_validar = tk.Button(self.frame_atendimento, text="Validar", command=self.validar)
        self.button_validar.grid(column=1, row=3)

        self.resultado = tk.Label(self.frame_atendimento, text="")
        self.resultado.grid(column=0, row=4, columnspan=2)

    def salvar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        self.clientes.append({"nome": nome, "cpf": cpf})
        self.janela_cadastro.destroy()

    def selecionar_cliente(self):
        selecionado = self.combo_cliente.get()
        for cliente in self.clientes:
            if cliente["nome"] == selecionado:
                self.cliente_selecionado = cliente
                break
        self.label_cliente.config(text=f"Paciente: {selecionado}")
        self.button_selecionar.destroy()
        self.criar_campos_atendimento()

    def validar(self):
        try:
            temperatura = float(self.entry_temp.get().replace(",", "."))
            batimentos = int(self.entry_bat.get().replace(",", "."))
            pressao = int(self.entry_pressao.get().replace(",", "."))

            resultadotemp = ""
            if temperatura <= 35:
                resultadotemp = "Hipotermia"
            elif 35 < temperatura <= 37.5:
                resultadotemp = "Temperatura normal"
            elif 37.6 <= temperatura <= 39:
                resultadotemp = "Febre leve"
            elif temperatura >= 39:
                resultadotemp = "Febre alta"

            resultadobat = ""
            if batimentos >= 100:
                resultadobat = "Taquicardia"
            elif batimentos <= 60:
                resultadobat = "Bradicardia"
            elif 60 < batimentos < 100:
                resultadobat = "Batimentos normais"

            resultadopressao = ""
            if pressao <= 10:
                resultadopressao = "Pressão baixa"
            elif pressao >= 20:
                resultadopressao = "Pressão alta"
            elif 10 < pressao < 20:
                resultadopressao = "Pressão normal"

            if resultadotemp == "Temperatura normal" and resultadobat == "Batimentos normais" and resultadopressao == "Pressão normal":
                resultado = "Atendimento normal"
            elif resultadotemp == "Febre leve" and resultadobat == "Batimentos normais" and resultadopressao == "Pressão normal":
                resultado = "Atendimento normal"
            elif resultadotemp == "Febre alta" and resultadobat == "Taquicardia" and resultadopressao == "Pressão alta":
                resultado = "Atendimento grave"
            elif resultadotemp == "Hipotermia" and resultadobat == "Bradicardia" and resultadopressao == "Pressão baixa":
                resultado = "Atendimento urgente"
            else:
                resultado = "Atendimento especial"

            self.resultado.config(text=f"Temp: {resultadotemp}, Bat: {resultadobat}, Press: {resultadopressao}\n{resultado}")

        except ValueError:
            self.resultado.config(text="Erro: Verifique os valores inseridos")

root = tk.Tk()
validador = ValidadorAtendimento(root)
root.mainloop()

