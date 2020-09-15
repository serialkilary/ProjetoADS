from tkinter import *
import os
import geradoradeimagens
import geradoradesemestres
import geradoradebotoes
import manipuladoradearquivos

class Disciplinas:
    def __init__(self,label,labeldeArquivos):
        self.label = label #label das disciplinas
        self.labeldeArquivos = labeldeArquivos#label dos meus arquivos
                
    def get_disciplinas_primeiro_semestre(self):#cria os botões das disciplinas do primeiro semestre
        
        self.acao_botao_comexpress = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/comunicacaoeexpressao/")
        self.botao_comexpress = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/comunicacaoeexpressao.png',1,1,416,42,self.acao_botao_comexpress.get_arquivos)
        self.botao_comexpress.place_button()

        self.acao_botao_desenpes = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/desenvolvimentopessoal/")
        self.botao_desenpes = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/desenvolvimentopessoal.png',2,1,416,42,self.acao_botao_desenpes.get_arquivos)
        self.botao_desenpes.place_button()

        self.acao_botao_infor = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/informatica/")
        self.botao_infor = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/informatica.png',3,1,416,42,self.acao_botao_infor.get_arquivos)
        self.botao_infor.place_button()

        self.acao_botao_logmat = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/logicamatematica/")
        self.botao_logmat = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/logicamatematica.png',4,1,416,42,self.acao_botao_logmat.get_arquivos)
        self.botao_logmat.place_button()

        self.acao_botao_siscomp = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/sistemascomputacionais/")
        self.botao_siscomp = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/sistemascomputacionais.png',5,1,416,42,self.acao_botao_siscomp.get_arquivos)
        self.botao_siscomp.place_button()

        self.acao_botao_teoadm = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/teoriasdaadm/")
        self.botao_teoadm = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/teoriasdaadm.png',6,1,416,42,self.acao_botao_teoadm.get_arquivos)
        self.botao_teoadm.place_button()

        self.acao_botao_intead = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/primeiroperiodo/introducaoaead/")
        self.botao_intead = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/primeiroperiodo/introducaoaead.png',7,1,416,42,self.acao_botao_intead.get_arquivos)
        self.botao_intead.place_button()

    def get_disciplinas_segundo_semestre(self):#cria os botões das disciplinas do segundo semestre
        self.acao_botao_ecomer = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/economiaemercado/")
        self.botao_ecomer = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/economiaemercado.png',1,1,416,42,self.acao_botao_ecomer.get_arquivos)
        self.botao_ecomer.place_button()

        self.acao_botao_evopen = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/evolucaodopensamento/")
        self.botao_evopen = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/evolucaodopensamento.png',2,1,416,42,self.acao_botao_evopen.get_arquivos)
        self.botao_evopen.place_button()

        self.acao_botao_logprog = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/logicadeprogramacao/")
        self.botao_logprog = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/logicadeprogramacao.png',3,1,416,42,self.acao_botao_logprog.get_arquivos)
        self.botao_logprog.place_button()

        self.acao_botao_matapli = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/matematicaaplicada/")
        self.botao_matapli = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/matematicaaplicada.png',4,1,416,42,self.acao_botao_matapli.get_arquivos)
        self.botao_matapli.place_button()

        self.acao_botao_prog = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/programacao/")
        self.botao_prog = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/programacao.png',5,1,416,42,self.acao_botao_prog.get_arquivos)
        self.botao_prog.place_button()

        self.acao_botao_topint = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/topicosintegradoresi/")
        self.botao_topint = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/topicosintegradoresi.png',6,1,416,42,self.acao_botao_topint.get_arquivos)
        self.botao_topint.place_button()

        self.acao_botao_usainter = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/segundoperiodo/usabilidadeeinterface/")
        self.botao_usainter = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/segundoperiodo/usabilidadeeinterface.png',7,1,416,42,self.acao_botao_usainter.get_arquivos)
        self.botao_usainter.place_button()
        
    def get_disciplinas_terceiro_semestre(self):#cria os botões das disciplinas do terceiro semestre
        self.acao_botao_bandad = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/bancodedados/")
        self.botao_bandad = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/bancodedados.png',1,1,416,42,self.acao_botao_bandad.get_arquivos)
        self.botao_bandad.place_button()

        self.acao_botao_empre = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/empreendedorismo/")
        self.botao_empre = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/empreendedorismo.png',2,1,416,42,self.acao_botao_empre.get_arquivos)
        self.botao_empre.place_button()
        

        self.acao_botao_eticid = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/eticaecidadania/")
        self.botao_eticid = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/eticaecidadania.png',3,1,416,42,self.acao_botao_eticid.get_arquivos)
        self.botao_eticid.place_button()
        
        self.acao_botao_fundest = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/fundamentosdeestatistica/")
        self.botao_fundest = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/fundamentosdeestatistica.png',4,1,416,42,self.acao_botao_fundest.get_arquivos)
        self.botao_fundest.place_button()

        self.acao_botao_orgarq = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/organizacaoearquitetura/")
        self.botao_orgarq = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/organizacaoearquitetura.png',5,1,416,42,self.acao_botao_orgarq.get_arquivos)
        self.botao_orgarq.place_button()

        self.acao_botao_progori = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/programacaoorientada/")
        self.botao_progori = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/programacaoorientada.png',6,1,416,42,self.acao_botao_progori.get_arquivos)
        self.botao_progori.place_button()

        self.acao_botao_redes = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/terceiroperiodo/redes/")
        self.botao_redes = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/terceiroperiodo/redes.png',7,1,416,42,self.acao_botao_redes.get_arquivos)
        self.botao_redes.place_button()
    
        
    def get_disciplinas_quarto_semestre(self):#cria os botões das disciplinas do quarto semestre
        self.acao_botao_anal = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/analise/")
        self.botao_anal = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/analise.png',1,1,416,42,self.acao_botao_anal.get_arquivos)
        self.botao_anal.place_button()

        self.acao_botao_arqsoft = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/arquiteturasoft/")
        self.botao_arqsoft = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/arquiteturasoft.png',2,1,416,42,self.acao_botao_arqsoft.get_arquivos)
        self.botao_arqsoft.place_button()

        self.acao_botao_engsoft = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/engenhariasoft/")
        self.botao_engsoft= geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/engenhariasoft.png',3,1,416,42,self.acao_botao_engsoft.get_arquivos)
        self.botao_engsoft.place_button()

        self.acao_botao_lider = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/lideranca/")
        self.botao_lider = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/lideranca.png',4,1,416,42,self.acao_botao_lider.get_arquivos)
        self.botao_lider.place_button()

        self.acao_botao_metodo = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/metodologia/")
        self.botao_metodo = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/metodologia.png',5,1,416,42,self.acao_botao_metodo.get_arquivos)
        self.botao_metodo.place_button()

        self.acao_botao_responsa = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/responsabilidade/")
        self.botao_responsa = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/responsabilidade.png',6,1,416,42,self.acao_botao_responsa.get_arquivos)
        self.botao_responsa.place_button()

        self.acao_botao_topint2 = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quartoperiodo/topicosii/")
        self.botao_topint2 = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quartoperiodo/topicosii.png',7,1,416,42,self.acao_botao_topint2.get_arquivos)
        self.botao_topint2.place_button()
        
        
    def get_disciplinas_quinto_semestre(self):#cria os botões das disciplinas do quinto semestre
        self.acao_botao_aplica = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/aplicacoes/")
        self.botao_aplica = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/aplicacoes.png',1,1,416,42,self.acao_botao_aplica.get_arquivos)
        self.botao_aplica.place_button()

        self.acao_botao_dispmov = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/dispositivosmoveis/")
        self.botao_dispmov = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/dispositivosmoveis.png',2,1,416,42,self.acao_botao_dispmov.get_arquivos)
        self.botao_dispmov.place_button()

        self.acao_botao_fundseg = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/fundamentosseguranca/")
        self.botao_fundseg = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/fundamentosseguranca.png',3,1,416,42,self.acao_botao_fundseg.get_arquivos)
        self.botao_fundseg.place_button()

        self.acao_botao_gerconfig = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/gerenciaconfig/")
        self.botao_gerconfig = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/gerenciaconfig.png',4,1,416,42,self.acao_botao_gerconfig.get_arquivos)
        self.botao_gerconfig.place_button()

        self.acao_botao_gerproj = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/gerenciaprojetos/")
        self.botao_gerproj = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/gerenciaprojetos.png',5,1,416,42,self.acao_botao_gerproj.get_arquivos)
        self.botao_gerproj.place_button()
        
        self.acao_botao_pratica = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/pratica/")
        self.botao_pratica = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/pratica.png',6,1,416,42,self.acao_botao_pratica.get_arquivos)
        self.botao_pratica.place_button()

        self.acao_botao_testsoft = manipuladoradearquivos.Manipuladora(self.labeldeArquivos,"/data/disciplinas/quintoperiodo/testesoft/")
        self.botao_testsoft = geradoradebotoes.CriaBotoes(self.label,'/data/imagens/icones/iconesdisciplinas/quintoperiodo/testesoft.png',7,1,416,42,self.acao_botao_testsoft.get_arquivos)
        self.botao_testsoft.place_button()
        
        

        
        
    
        
        
        



