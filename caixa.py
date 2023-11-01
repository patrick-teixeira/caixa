import tkinter as tk
import customtkinter
from tkinter import messagebox, simpledialog
import json
from functions import * 

class interface(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mangá Livre")
        self.geometry("500x430")
        self.carrinho = []
        self.home()
        
    def home(self):
        label = customtkinter.CTkLabel(master=self, text="Bem Vindo a Mangá Livre", font=("Arial", 18))
        label.pack(pady=20)
        customtkinter.CTkButton(master=self, text="1. Adicionar Mangá ao carrinho de compras", command=self.adicionar_ao_carrinho).pack(fill=tk.X, padx=50, pady=5)
        customtkinter.CTkButton(master=self, text="2. Adicionar Mangá ao estoque", command=self.adicionar_ao_estoque).pack(fill=tk.X, padx=50, pady=5)
        customtkinter.CTkButton(master=self, text="3. Ver carrinho de compras", command=self.ver_carrinho).pack(fill=tk.X, padx=50, pady=5)
        customtkinter.CTkButton(master=self, text="4. Ver mangás disponíveis", command=self.ver_mangas_disponiveis).pack(fill=tk.X, padx=50, pady=5)
        customtkinter.CTkButton(master=self, text="5. Finalizar compras", command=self.finalizar_compras).pack(fill=tk.X, padx=50, pady=5)
        customtkinter.CTkButton(master=self, text="6. Sair", command=self.sair).pack(fill=tk.X, padx=50, pady=5)
        label2 = customtkinter.CTkLabel(master=self, text="📚 Mangá Livre - A sua loja de mangás!", font=("Arial", 12))
        label2.pack(pady=20)

    def adcionar_btn(self):
        manga = self.adcionar_input.get()
        if pesquisar(manga) == True:
            valor = valor_manga(manga)
            volume = customtkinter.CTkInputDialog(text=f'Qual volume deseja adcionar? (Volumes {quant_volumes(manga)})', title='Volume')
            volume = volume.get_input()
            self.carrinho.append(f'{manga}:{volume}:{valor}')
            messagebox.showinfo('Carrinho', f'''{manga.capitalize()} Volume {volume} Adcionado ao carrinho ''')
            self.destroy_widgets()
            self.home()
        else:
            messagebox.showerror('Erro', 'Mangá não existe ou esta fora de estoque')

    def destroy_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def adicionar_ao_carrinho(self):
        manga = customtkinter.CTkInputDialog(text=f'Qual mangá deseja adcionar?', title='Adcionar')
        manga = manga.get_input()
        try:
            if pesquisar(manga) == True:
                valor = valor_manga(manga)
                volume = customtkinter.CTkInputDialog(text=f'Qual volume deseja adcionar? (Volumes {quant_volumes(manga)})', title='Volume')
                volume = volume.get_input()
                self.carrinho.append(f'{manga}:{volume}:{valor}')
                messagebox.showinfo('Carrinho', f'''{manga.capitalize()} Volume {volume} Adcionado ao carrinho ''')
                self.destroy_widgets()
                self.home()
            else:
                messagebox.showerror('Erro', 'Mangá não existe ou esta fora de estoque')
        except:
            pass

    def escrever_textbox(self, msg):
        self.itens.configure(state='normal')
        self.itens.insert(customtkinter.END, f'{msg}\n')
        self.itens.yview(customtkinter.END)
        self.itens.configure(state='disabled')


    def add_btn(self, nome, autor, genero, editora, volume, preco):
        try:
            add_manga(nome, autor, genero, editora, volume, preco)
            messagebox.showinfo('Aviso', f'{nome.capitalize()} Adcionado ao estoque')
            self.voltar()
        except Exception as e:
            print(e)
            messagebox.showerror("Erro", "Digite os dados corretamente")

    def adicionar_ao_estoque(self): 
        self.destroy_widgets()
        customtkinter.CTkLabel(master=self, text='Nome').pack(fill=tk.X, padx=50, pady=1)
        nome = customtkinter.CTkEntry(master=self)
        nome.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkLabel(master=self, text='Autor').pack(fill=tk.X, padx=50, pady=1)
        autor = customtkinter.CTkEntry(master=self)
        autor.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkLabel(master=self, text='Genero').pack(fill=tk.X, padx=50, pady=1)
        editora = customtkinter.CTkEntry(master=self)
        editora.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkLabel(master=self, text='Editora').pack(fill=tk.X, padx=50, pady=1)
        genero = customtkinter.CTkEntry(master=self)
        genero.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkLabel(master=self, text='Volume').pack(fill=tk.X, padx=50, pady=1)
        volume = customtkinter.CTkEntry(master=self)
        volume.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkLabel(master=self, text='Preço').pack(fill=tk.X, padx=50, pady=1)
        preco = customtkinter.CTkEntry(master=self)
        preco.pack(fill=tk.X, padx=50, pady=1)
        customtkinter.CTkButton(master=self, text='Voltar', command=self.voltar).pack(padx=50, pady=2)
        customtkinter.CTkButton(master=self, text='Adcionar', command=lambda: self.add_btn(nome.get(), autor.get(), genero.get(), editora.get(), volume.get(), preco.get())).pack(padx=50, pady=5)

    def voltar(self):
        self.destroy_widgets()
        self.home()

    def ver_carrinho(self):
        self.destroy_widgets()
        self.itens = customtkinter.CTkTextbox(master=self, state='disabled')
        self.itens.pack(padx=10, pady=10)
        voltar = customtkinter.CTkButton(master=self, text='Voltar', command=self.voltar)
        voltar.pack()
        for manga in self.carrinho:
            volume = manga.split(':')[1]
            manga = manga.split(':')[0]
            self.escrever_textbox(f'{manga.capitalize()} Volume {volume}')
        
    def ver_mangas_disponiveis(self):
        self.destroy_widgets()
        self.itens = customtkinter.CTkTextbox(master=self, state='disabled')
        self.itens.pack(padx=10, pady=10) 
        voltar = customtkinter.CTkButton(master=self, text='Voltar', command=self.voltar)
        voltar.pack()
        mangas = mangas_estoque() 
        for manga in mangas:
            self.escrever_textbox(manga.capitalize())

    def finalizar_compras(self):
        valor = 0
        desconto = 0 
        if len(self.carrinho) == 0:
            messagebox.showinfo('Finalizar', 'Nenhum mangá no carrinho')
            return
        for manga in self.carrinho:
            valor += float(manga.split(':')[2])
        cupom = customtkinter.CTkInputDialog(text=f'Cupom', title='Finalizar')
        desconto = cupom.get_input()
        desconto = (valor * float(desconto))/100
        valor = valor - desconto
        valor = float(valor)
        while True:
            dinheiro = customtkinter.CTkInputDialog(text=f'Valor R$ {valor}', title='Finalizar') 
            dinheiro = dinheiro.get_input()
            dinheiro = float(dinheiro)
            if dinheiro < valor:
                messagebox.showerror('Erro', f'Valor insuficiente falta: R${valor - dinheiro}')
            elif dinheiro > valor:
                messagebox.showinfo('Compra Finalizada', f'Compra finalizada. Troco R${dinheiro - valor}')
                self.carrinho = []
                break     
            else:
                messagebox.showinfo('Compra Finalizada', 'Compra finalizada')                    
                self.carrinho = []
                break
    def sair(self):
        self.root.destroy()


Interface = interface()
Interface.mainloop()