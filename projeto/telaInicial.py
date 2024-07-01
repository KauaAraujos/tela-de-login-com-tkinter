from tela import *
from telaDeCriacao import *
class Inicio(Criacao):
    def home(self):
            # Cria um rótulo (label)
            self.frame = CTkFrame(self.janela, width=250, height=250)
            self.frame.grid(row=0)
            
            self.label_usuario = CTkLabel(self.frame, font=('robotic', 30),text='Login', width=230, height=50)
            self.label_usuario.place(x=10, y=10)
            
            self.entrada_usuario_login = CTkEntry(self.frame, width=170, placeholder_text='usuario')
            self.entrada_usuario_login.place(x=35, y=65)
            
            self.entrada_senha_login = CTkEntry(self.frame, width=170, placeholder_text='senha')
            self.entrada_senha_login.place(x=35, y=125)
            
            self.botao_entrar = CTkButton(self.frame, width=40, height=30, text='Entrar')
            self.botao_entrar.place(x=35, y=190)
            # Cria um botão
            self.botao_criar_conta = CTkButton(self.frame, width=40, height=30, text='Criar conta', hover_color='#082006',fg_color='green', command=self.telaCriacao)
            self.botao_criar_conta.place(x=125, y=190)