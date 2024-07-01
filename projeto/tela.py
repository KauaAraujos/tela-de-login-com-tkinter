# from sys import byteorder
from bancodatela import *
from tkinter import *
from customtkinter import *
from telaDeCriacao import *
from telaInicial import *

class Tela:
    def __init__(self, janela, home):
        self.janela = janela
        self.janela.geometry("250x250")
        self.janela.title("Tela inicial")
        self.janela.resizable(width=False, height=False)
        self.janela.config(bg='white')
        self.home = home
        self.home.home()

    
        
class TelaCriacao(Inicio):
    def adicionando(self):
        nome = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        adicionar(nome, senha)
        self.frame = CTkFrame(self.janela, width=250, height=250)
        self.frame.grid(row=0)
        
        self.label_usuario = CTkLabel(self.frame, font=('robotic', 20),text='Conta criada com sucesso!', width=230, height=50, fg_color='green')
        self.label_usuario.place(x=8, y=10)
        
        self.botao_voltar = CTkButton(self.frame, width=40, height=30, text='Voltar', fg_color='#b6160b', hover_color='#770000', command=self.home)
        self.botao_voltar.place(x=155, y=190)
        
    def telaLogin(self):
        nome = self.entrada_usuario_login.get()
        senha = self.entrada_senha_login.get()
        login(nome, senha)
if __name__ == "__main__":
    janela = CTk()
    casa = TelaCriacao
    app = Tela(janela, casa)
    janela.mainloop()
