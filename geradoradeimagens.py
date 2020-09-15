from tkinter import *
import os
from PIL import ImageTk, Image

class DeImagem:
     def __init__(self):
          self.imagem = None
          
     def carrega_imagem(self,path_image):#carrega imagem direto da basta com o fornecimento do caminho#
          self.imagem  = ImageTk.PhotoImage(Image.open(os.getcwd()+path_image))
          return self.imagem

     def resolucao_fundo(self,screen_width,screen_height):#carrega a imagem de fundo de acordo com a resolução do monitor#
          self.width = screen_width# dimensões do monitor
          self.height = screen_height# dimensões do monitor
          if self.width == 1366 and self.height == 768 :# condições para carregamento da foto de fundo base
              return self.carrega_imagem("/data/imagens/fundos/fundo1366x768.png")
          elif self.width == 800 and self.height == 600 :
              return self.carrega_imagem("/data/imagens/fundos/fundo800x600.png")

     def resolucao_fundo2(self,screen_width,screen_height):#carrega a imagem de fundo de acordo com a resolução do monitor#
          self.width = screen_width# dimensões do monitor
          self.height = screen_height# dimensões do monitor
          if self.width == 1366 and self.height == 768 :# condições para carregamento da foto de fundo2
              return self.carrega_imagem("/data/imagens/fundos/fundo2_1366x768.png")
          elif self.width == 800 and self.height == 600 :
              return self.carrega_imagem("/data/imagens/fundos/fundo2_800x600.png")
