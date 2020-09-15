from tkinter import *
from PIL import ImageTk, Image

import os
import geradoradeimagens
import geradoradesemestres
import geradoradebotoes
import geradoradedisciplinas
import webbrowser

class Manipuladora:
    def __init__(self,canvas,diretorio):
        self.canvas = canvas #labeldeArquivo
        self.diretorio = diretorio[1:] #diretorio informado
    
    def get_arquivos(self): #função que carrega os arquivos da minha pasta
        #Achando caminho da imagem que o canvas irá receber 
        diretorio_da_imagem = self.diretorio + os.listdir(self.diretorio)[0]
        
        #Carregando imagem com as funções do modulo PIL
        #ImageTk nos permite carregar imagens com formatos além de .gif .ppm .pwm
        img = ImageTk.PhotoImage(self.resize_image(diretorio_da_imagem))  

        #Adicioando imagem ao canvas
        self.canvas.create_image(5, 35, anchor=NW, image=img) 

        #Dizendo que a imagem a ser mostrada é a imagem carregada agora
        self.canvas.image = img

        return self.diretorio
                  
    def get_item(self,evento):
        sel = self.list.curselection() #retorna a posição do item clicado
        filename = self.list.get(int(sel[0])) #retorna o nome do arquivo clicado
        webbrowser.open(os.getcwd()+self.diretorio+filename) #abre o arquivo basedo no diretorio e nome do arquivo

    def resize_image(self, caminho_da_imagem: str):
        """
            Função responsável por ajustar imagem dentro do canvas
            sem que ela fique cortada.
        """

        #Carregando imagem a ser mudada tamanho
        imagem = Image.open(caminho_da_imagem)
        
        image_size = imagem.size
        canvas_size = (self.canvas.winfo_width()-10, self.canvas.winfo_height() - 10)
        
        #Criando variável que recebe o quosciente entre os tamanhos da imagem (razão)
        image_resolution = image_size[0]/image_size[1]

        #Gerando novos tamanhos relacionando altura do canvas e razão da imagem
        new_image_size = (canvas_size[0], round(canvas_size[0] / image_resolution))

        #Gerando nova imagem com tamanho ajustado
        imagem = imagem.resize(new_image_size, Image.ANTIALIAS)

        return imagem


        
