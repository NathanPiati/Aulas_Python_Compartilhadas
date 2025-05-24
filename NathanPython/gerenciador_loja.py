import json
import os
from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox

ARQUIVO_PRODUTOS = "produtos_naturais.json"
ARQUIVO_VENDAS = "vendas.json"

class GerenciadorLoja:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Produtos Naturais")
        self.produtos = self.carregar_produtos()
        self.vendas = self.carregar_vendas()
        self.criar_interface()

    def carregar_produtos(self):
        if os.path.exists(ARQUIVO_PRODUTOS):
            with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def salvar_produtos(self):
        with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as f:
            json.dump(self.produtos, f, indent=4, ensure_ascii=False)

    def carregar_vendas(self):
        if os.path.exists(ARQUIVO_VENDAS):
            with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def salvar_vendas(self):
        with open(ARQUIVO_VENDAS, 'w', encoding='utf-8') as f:
            json.dump(self.vendas, f, indent=4, ensure_ascii=False)

    def criar_interface(self):
        self.frame_opcoes = ctk.CTkFrame(self.root)
        self.frame_opcoes.pack(padx=10, pady=10)

        ctk.CTkButton(self.frame_opcoes, text="Listar Produtos", command=self.listar_produtos).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Adicionar Produto", command=self.adicionar_produto).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Atualizar Produto", command=self.atualizar_produto).grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Remover Produto", command=self.remover_produto).grid(row=1, column=1, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Buscar Produto", command=self.buscar_produto).grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Registrar Venda", command=self.registrar_venda).grid(row=2, column=1, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Ver Vendas", command=self.listar_vendas).grid(row=3, column=0, padx=5, pady=5)
        ctk.CTkButton(self.frame_opcoes, text="Sair", command=self.sair).grid(row=3, column=1, padx=5, pady=5)

    def listar_produtos(self):
        produtos_janela = ctk.CTkToplevel(self.root)
        produtos_janela.title("Produtos Cadastrados")
        if not self.produtos:
            messagebox.showinfo("Informação", "Nenhum produto cadastrado.")
            return
        for p in self.produtos:
            ctk.CTkLabel(produtos_janela, text=f"Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Estoque: {p['estoque']}").pack()

    def adicionar_produto(self):
        def salvar():
            try:
                nome = entry_nome.get().strip()
                preco = float(entry_preco.get())
                estoque = int(entry_estoque.get())
                self.produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
                messagebox.showinfo("Informação", "Produto adicionado com sucesso!")
                janela.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Preço ou estoque inválido.")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Adicionar Produto")

        ctk.CTkLabel(janela, text="Nome do Produto:").pack()
        entry_nome = ctk.CTkEntry(janela)
        entry_nome.pack()

        ctk.CTkLabel(janela, text="Preço (R$):").pack()
        entry_preco = ctk.CTkEntry(janela)
        entry_preco.pack()

        ctk.CTkLabel(janela, text="Quantidade em Estoque:").pack()
        entry_estoque = ctk.CTkEntry(janela)
        entry_estoque.pack()

        ctk.CTkButton(janela, text="Salvar", command=salvar).pack()

    def atualizar_produto(self):
        def atualizar():
            try:
                indice = int(entry_indice.get()) - 1
                if 0 <= indice < len(self.produtos):
                    nome = entry_nome.get().strip()
                    preco = entry_preco.get()
                    estoque = entry_estoque.get()

                    if nome:
                        self.produtos[indice]['nome'] = nome
                    if preco:
                        self.produtos[indice]['preco'] = float(preco)
                    if estoque:
                        self.produtos[indice]['estoque'] = int(estoque)

                    messagebox.showinfo("Informação", "Produto atualizado com sucesso!")
                    janela.destroy()
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida.")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Atualizar Produto")

        ctk.CTkLabel(janela, text="Número do Produto:").pack()
        entry_indice = ctk.CTkEntry(janela)
        entry_indice.pack()

        ctk.CTkLabel(janela, text="Novo Nome (deixe em branco para manter):").pack()
        entry_nome = ctk.CTkEntry(janela)
        entry_nome.pack()

        ctk.CTkLabel(janela, text="Novo Preço (deixe em branco para manter):").pack()
        entry_preco = ctk.CTkEntry(janela)
        entry_preco.pack()

        ctk.CTkLabel(janela, text="Novo Estoque (deixe em branco para manter):").pack()
        entry_estoque = ctk.CTkEntry(janela)
        entry_estoque.pack()

        ctk.CTkButton(janela, text="Atualizar", command=atualizar).pack()

    def remover_produto(self):
        def remover():
            try:
                indice = int(entry_indice.get()) - 1
                if 0 <= indice < len(self.produtos):
                    produto_removido = self.produtos.pop(indice)
                    messagebox.showinfo("Informação", f"Produto '{produto_removido['nome']}' removido.")
                    janela.destroy()
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida.")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Remover Produto")

        ctk.CTkLabel(janela, text="Número do Produto:").pack()
        entry_indice = ctk.CTkEntry(janela)
        entry_indice.pack()

        ctk.CTkButton(janela, text="Remover", command=remover).pack()

    def buscar_produto(self):
        def buscar():
            termo = entry_termo.get().strip().lower()
            encontrados = [p for p in self.produtos if termo in p['nome'].lower()]
            if encontrados:
                for p in encontrados:
                    ctk.CTkLabel(resultados_janela, text=f"Nome: {p['nome']}, Preço: R${p['preco']:.2f}, Estoque: {p['estoque']}").pack()
            else:
                messagebox.showinfo("Informação", "Nenhum produto encontrado.")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Buscar Produto")

        ctk.CTkLabel(janela, text="Nome ou parte do nome do produto:").pack()
        entry_termo = ctk.CTkEntry(janela)
        entry_termo.pack()

        ctk.CTkButton(janela, text="Buscar", command=buscar).pack()

        resultados_janela = ctk.CTkToplevel(janela)
        resultados_janela.title("Resultados da Busca")

    def registrar_venda(self):
        def registrar():
            try:
                indice = int(entry_indice.get()) - 1
                if 0 <= indice < len(self.produtos):
                    produto = self.produtos[indice]
                    quantidade = int(entry_quantidade.get())
                    if 0 < quantidade <= produto['estoque']:
                        total = quantidade * produto['preco']
                        produto['estoque'] -= quantidade
                        venda = {
                            "produto": produto['nome'],
                            "quantidade": quantidade,
                            "preco_unitario": produto['preco'],
                            "total": total,
                            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        self.vendas.append(venda)
                        messagebox.showinfo("Informação", f"Venda registrada! Total: R${total:.2f}")
                        janela.destroy()
                    else:
                        messagebox.showerror("Erro", "Estoque insuficiente.")
                else:
                    messagebox.showerror("Erro", "Produto não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "Entrada inválida.")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Registrar Venda")

        ctk.CTkLabel(janela, text="Número do Produto:").pack()
        entry_indice = ctk.CTkEntry(janela)
        entry_indice.pack()

        ctk.CTkLabel(janela, text="Quantidade Vendida:").pack()
        entry_quantidade = ctk.CTkEntry(janela)
        entry_quantidade.pack()

        ctk.CTkButton(janela, text="Registrar", command=registrar).pack()

    def listar_vendas(self):
        vendas_janela = ctk.CTkToplevel(self.root)
        vendas_janela.title("Vendas Realizadas")
        if not self.vendas:
            messagebox.showinfo("Informação", "Nenhuma venda registrada.")
            return
        for v in self.vendas:
            ctk.CTkLabel(vendas_janela, text=f"Produto: {v['produto']}, Quantidade: {v['quantidade']}, Total: R${v['total']:.2f}, Data: {v['data']}").pack()

    def sair(self):
        self.salvar_produtos()


    def sair(self):
        self.salvar_produtos()
        self.salvar_vendas()
        self.root.destroy()  # Fecha a interface

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # ou "Light", "Dark"
    ctk.set_default_color_theme("blue")  # temas: "blue", "green", "dark-blue"
    root = ctk.CTk()
    app = GerenciadorLoja(root)
    root.mainloop()






