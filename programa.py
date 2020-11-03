from tkinter import *
import os
import geradoradeimagens
import geradoradesemestres
import geradoradebotoes
import geradoradedisciplinas
import funcaobotoes
import webbrowser


class MeuPrograma:
    def __init__(self,programa,screen_width,screen_height):
        self.programa = Frame(programa)#mesa de trabalho
        self.programa.grid(row=0, column=1)#descarrega mesa de trabalho

        self.programa.fundo_1 = geradoradeimagens.DeImagem()#chama a classe carregadoradeImagem
        self.programa.fundo_menu_principal = self.programa.fundo_1.resolucao_fundo(screen_width,screen_height)#carrega imagem de fundo baseado na resolução da tela
        self.programa.label = Label(self.programa,image  = self.programa.fundo_menu_principal)#coloca imagem no fundo
        self.programa.label.grid(row=0, column=1)#carrega o pacote que contem os widgets do menu principal

        self.programa.fundo_2 = geradoradeimagens.DeImagem() #chama a classe carregadoradeImagem
        self.programa.fundo2_menu_disciplinas = self.programa.fundo_2.resolucao_fundo2(screen_width,screen_height)#carrega imagem de fundo baseado na resolução da tela
        self.programa.label2 = Label(self.programa,image  = self.programa.fundo2_menu_disciplinas)#coloca imagem no fundo

        self.programa.fundo_3 = geradoradeimagens.DeImagem() #chama a classe carregadoradeImagem
        self.programa.fundo3_menu_creditos = self.programa.fundo_3.resolucao_fundo2(screen_width,screen_height)#carrega imagem de fundo baseado na resolução da tela
        self.programa.label3 = Label(self.programa,image  = self.programa.fundo3_menu_creditos)#coloca imagem no fundo

        self.programa.botoes_menu_principal= funcaobotoes.botoes(programa,self.programa.label,self.programa.label2,self.programa.label3)#carregaclasse botoes do arquivo funcaobotoes
        self.programa.botoes_menu_principal.get_menu_principal()#funcao da classe botoes que joga botoes do menu principal na tela

programa = Tk()
screen_width = programa.winfo_screenwidth()
screen_height = programa.winfo_screenheight()
MeuPrograma(programa,screen_width,screen_height)
programa.attributes("-fullscreen",True)
programa.mainloop()

input()









