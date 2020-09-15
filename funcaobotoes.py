import geradoradebotoes
import geradoradeimagens
import geradoradedisciplinas
import geradoradesemestres
import manipuladoradearquivos
import webbrowser
import os
from tkinter import*


class botoes:
    def __init__(self,principal,showwindow,hidewindow,label3):
        self.principal = principal#mesa de trabalho
        self.showwindow = showwindow#self.programa.label
        self.hidewindow = hidewindow#self.programa.label2
        self.label3 = label3 #self.programa.label3
        self.labelbotoes2 =Label(self.principal)

    def get_menu_principal(self):#botoes menu principal(self.programa.label)
        self.showwindow.grid(row=0, column=1)
        self.labelbotoes =Label(self.showwindow)
        self.labelbotoes.place(relx = 0.4,rely = 0.6)
        
        self.botao_Link = geradoradebotoes.CriaBotoes(self.labelbotoes,'/data/imagens/icones/iconesmenu/iconelink.png',1,1,56,56,self.get_link)#cria botao link
        self.botao_Link.place_button()#descarrega o botão link na self.programa.label

        self.botao_Sobre = geradoradebotoes.CriaBotoes(self.labelbotoes,'/data/imagens/icones/iconesmenu/iconesobre.png',1,2,56,56,self.get_video)#cria botao sobre
        self.botao_Sobre.place_button()#descarrega botao sobre na self.programa.label
        
        self.botao_Disciplinas = geradoradebotoes.CriaBotoes(self.labelbotoes,'/data/imagens/icones/iconesmenu/iconedisciplinas.png',1,3,56,56,self.get_disciplinas)#cria botao disciplinas
        self.botao_Disciplinas.place_button()#descarrega botao disciplinas na self.programa.label

        self.botao_Sair = geradoradebotoes.CriaBotoes(self.labelbotoes,'/data/imagens/icones/iconesmenu/iconesair.png',1,5,56,56,self.get_exit)#cria botao sair
        self.botao_Sair.place_button()#descarrega o botao sair na tela na self.programa.label

    def get_disciplinas(self):#chama o menu disciplinas
        self.showwindow.grid_forget()
        self.labelbotoes2.place(relx = 0.47,rely =0.61)

        self.botao_voltar = geradoradebotoes.CriaBotoes(self.labelbotoes2,'/data/imagens/icones/iconesmenu/iconevoltar.png',1,2,56,56,self.get_back)#cria botao sobre
        self.botao_voltar.place_button()#descarrega botao sobre na self.programa.label

        self.botao_Link2 = geradoradebotoes.CriaBotoes(self.labelbotoes2,'/data/imagens/icones/iconesmenu/iconelink.png',1,1,56,56,self.get_link)#cria botao link
        self.botao_Link2.place_button()#descarrega o botão link na self.programa.label

        self.botao_Sair2 = geradoradebotoes.CriaBotoes(self.labelbotoes2,'/data/imagens/icones/iconesmenu/iconesair.png',1,5,56,56,self.get_exit)#cria botao sair
        self.botao_Sair2.place_button()#descarrega o botao sair na tela na self.programa.labe
        
        self.showwindow.grid_forget()#esconde tela principal
        self.hidewindow.grid(row=0, column=1)#descarrega o menu disciplinas

        self.semestre = geradoradesemestres.Semestres(self.principal,'/data/imagens/icones/iconesmenu/iconenassau.png')#carrega os semestres , e carrega imagem de fundo do label da nassau
        self.semestre.get_semestre()#imprime os semestres no label de semestres
        
    def get_back(self):
        self.labelbotoes2.place_forget()
        self.semestre.remove_semestre()
        self.hidewindow.grid_forget()
        self.get_menu_principal()
       
    def get_exit(self):#saida do programa
        self.principal.destroy()#destroi meu programa
        
    def get_link(self):#carrega o site da uninassau
        webbrowser.open('https://vestibular.uninassau.edu.br/')

    def get_video(self):#carrega video contido na pasta do programa 
        webbrowser.open(os.getcwd()+"/data/video/videoads.mp4")
        
        
