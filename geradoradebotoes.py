from tkinter import *
import os
import geradoradeimagens



class CriaBotoes: #criacao de botao na tela#
    def __init__(self,local,icone,posicao_x,posicao_y,tamanhox,tamanhoy,comando,):
        self.local = local #tela que será colocado meu botão
        self.posx = posicao_x # posicionamento do botão com relação horizontal
        self.posy = posicao_y# posicionamento do botão com relação vertical
        self.tamanhox = tamanhox# tamanho do botão com relação horizontal
        self.tamanhoy = tamanhoy #tamanho do botao com relação vertical
        self.icone = self.imagem  = PhotoImage(file = os.getcwd()+icone)#carrega o icone do botão
        self.comando = comando# irá conter  o comando do botão
        self.botao = Button(self.local ,width = self.tamanhox , height = self.tamanhoy,image = self.icone, command = comando)#cria o botão

    def place_button(self):#retorna o botão com os parametros informados
        return self.botao.grid(row= self.posx,column = self.posy)


            
'''kilary = Tk()

kilary.geometry("600x500")

sair = CriaBotoes()
sair_b = FuncoesBotoes()
sair.cria_botao(kilary,"sair",0,0,sair_b.bt_sair)
kilary.mainloop()'''
