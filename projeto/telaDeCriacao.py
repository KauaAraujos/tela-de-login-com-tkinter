from customtkinter import *
from tela import Tela
from tela import *
class Criacao(Tela):
    def telaCriacao(self):
            self.frame = CTkFrame(self.janela, width=250, height=250)
            self.frame.grid(row=0)
            
            self.label_usuario = CTkLabel(self.frame, font=('robotic', 30),text='Criar conta', width=230, height=50)
            self.label_usuario.place(x=10, y=10)
            
            self.entrada_usuario = CTkEntry(self.frame, width=170, placeholder_text='usuario')
            self.entrada_usuario.place(x=35, y=65)
            
            self.entrada_senha = CTkEntry(self.frame, width=170, placeholder_text='senha')
            self.entrada_senha.place(x=35, y=125)
            
            self.botao_criar = CTkButton(self.frame, width=40, height=30, text='Criar', command=self.telaCriacao)
            self.botao_criar.place(x=35, y=190)
            
            self.botao_voltar = CTkButton(self.frame, width=40, height=30, text='Voltar', fg_color='#b6160b', hover_color='#770000', command=self.home)
            self.botao_voltar.place(x=155, y=190)
