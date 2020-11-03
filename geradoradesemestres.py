from tkinter import *
import os
import geradoradeimagens
import geradoradebotoes
import geradoradedisciplinas
import webbrowser

class Semestres:
    def __init__(self,tela,imagenzinha):
        self.tela  = tela #self.program.label2(contém as disciplinas)
        
        self.Semestres = Label(self.tela)#cria label contendo semestres
        self.Semestres.place(relx = 0.15,rely =0.2)#descarrega label contendo semestres em self.program.label2

        self.Disciplinas = Label(self.tela)#cria label contendo disciplinas
        self.Disciplinas.place(relx = 0.15,rely =0.27)#descerrega label que irá conter as disciplinas em self.program.label2

        """ Criando o canvas que receberá as imagens que explicará as disciplinas """
        self.Arquivos = Canvas(self.tela, width = 450, height = 340, bg = "White")
        self.Arquivos.place(relx = 0.615,rely =0.27)#descarrega o label dos arquivos

        self.matriz = Label(self.tela)#cria label que irá conter o botao que da acesso a matrizcurricular
        self.matriz.place(relx = 0.15,rely =0.13)#descarrega o label da matriz  em self.program.label2
        self.botao_matriz = geradoradebotoes.CriaBotoes(self.matriz,'/data/imagens/icones/botaomatriz.png',1,8,150,42,self.get_matriz)#cria botao matriz curricular no self.matriz
        self.botao_matriz.place_button()#descarrega o botao self.botao_matriz no label self.matriz

        self.fotonassau = Frame(self.tela)#cria label que irá conter o simbolo da nassau em self.program.label2
        self.fotonassau.place(relx = 0.465,rely =0.27) #descarrega o label self.fotonassau em self.program.label2

        self.imagenzinha = geradoradeimagens.DeImagem()#classe para carregar imagem
        self.imagenzinha.img = self.imagenzinha.carrega_imagem(imagenzinha) #carregando imagem da nassau da pasta
        self.imagenzinha.fundo = Label(self.fotonassau,width = 194,height =250,image =self.imagenzinha.img )#label  para foto da nassau
        self.imagenzinha.fundo.pack()# descarrega o label da foto nassau dentro do label self.fotonassau
        
        
    def get_semestre(self):#função que imprime os botoes do semestre
        
        acao_botao_primeiro_semestre = geradoradedisciplinas.Disciplinas(self.Disciplinas,self.Arquivos)#cria botao do primeiro semestre
        self.botao_Primeirosemestre = geradoradebotoes.CriaBotoes(self.Semestres,'/data/imagens/icones/iconessemestres/primeirosemestre.png',1,1,150,42,acao_botao_primeiro_semestre.get_disciplinas_primeiro_semestre)#cria botao do primeiro semestre
        self.botao_Primeirosemestre.place_button()#descarrega botao primeiro semestre dentro do label de semestres
        
        acao_botao_segundo_semestre= geradoradedisciplinas.Disciplinas(self.Disciplinas,self.Arquivos)
        self.botao_Segundosemestre = geradoradebotoes.CriaBotoes(self.Semestres,'/data/imagens/icones/iconessemestres/segundosemestre.png',1,2,150,42,acao_botao_segundo_semestre.get_disciplinas_segundo_semestre)#cria botao do segundo semestre
        self.botao_Segundosemestre.place_button()#descarrega botao segundo semestre dentro do label de semestres
        
        acao_botao_terceiro_semestre= geradoradedisciplinas.Disciplinas(self.Disciplinas,self.Arquivos)
        self.botao_Terceirosemestre = geradoradebotoes.CriaBotoes(self.Semestres,'/data/imagens/icones/iconessemestres/terceirosemestre.png',1,3,150,42,acao_botao_terceiro_semestre.get_disciplinas_terceiro_semestre)#cria botao do terceiro semestre
        self.botao_Terceirosemestre.place_button()#descarrega botao terceiro semestre dentro do label de semestres
        
        acao_botao_quarto_semestre = geradoradedisciplinas.Disciplinas(self.Disciplinas,self.Arquivos)
        self.botao_Quartosemestre = geradoradebotoes.CriaBotoes(self.Semestres,'/data/imagens/icones/iconessemestres/quartosemestre.png',1,4,150,42,acao_botao_quarto_semestre.get_disciplinas_quarto_semestre)#cria botao do quarto semestre
        self.botao_Quartosemestre.place_button()#descarrega botao quarto semestre dentro do label de semestres
        
        acao_botao_quinto_semestre = geradoradedisciplinas.Disciplinas(self.Disciplinas,self.Arquivos)
        self.botao_Quintosemestre = geradoradebotoes.CriaBotoes(self.Semestres,'/data/imagens/icones/iconessemestres/quintosemestre.png',1,5,150,42,acao_botao_quinto_semestre.get_disciplinas_quinto_semestre)#cria botao do quinto semestre
        self.botao_Quintosemestre.place_button()#descarrega botao quinto semestre dentro do label de semestres
        

    def remove_semestre(self):
        self.Semestres.place_forget()
        self.Disciplinas.place_forget()
        self.Arquivos.place_forget()
        self.matriz.place_forget()
        self.fotonassau.place_forget()
        self.imagenzinha.fundo.pack_forget()

    def get_matriz(self):
        webbrowser.open(os.getcwd()+"/data/MatrizADS.pdf")

        
        
        
        
        
