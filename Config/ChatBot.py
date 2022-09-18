import sys
import os
import subprocess as os_linux
from Config.Memoria import Memoria

class ChatBot:
    def __init__(self, nome):
        self.nome = nome
        self.historico = ['primeiro']
        self.frases = Memoria.busca_conversa()

        self.conhecidos = []
    def escuta(self):
        frase= input('>: ')
        frase = frase.lower()
        return frase
    def aprender(self):
        novidade = input('Digite o que vou ouvir: ')
        resposta = input('Digite o que responderei: ')
        self.frases[novidade] = resposta

        return 'Aprendido!'

    def pensa(self, frase):
        if frase == 'manutenção':
            self.manutencao(frase)
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
           return self.aprender()

        if self.historico[-1] == "Olá, qual seu nome?":
            nome = self.pega_nome(frase)
            resp = self.respondeNome(nome)
            self.historico.append(frase)
            return  resp
        try:
            resp = str(eval(frase))
            return resp
        except:
            novidade = frase
            print("Não entendi. ")
            resposta = input('Oque devo responder a isso? ')
            self.frases[novidade] = resposta
            Memoria.salva_conversa(self.frases)
            return 'Aprendido!'
        return 'Não entendi!'

    def fala(self, frase):
        ## Abrindo programas externos
        if 'executa' in frase:
            platforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'Win' in platforma:
                os.startfile(comando)
            if 'linux' in platforma:
                try:
                    os_linux.Popen(comando)
                except FileNotFoundError:
                    os_linux.Popen(['xdg-open', comando])
        else:
            print(frase)
            self.historico.append(frase)

    def pega_nome(self, nome):
        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        conhecidos = Memoria.busca_nome()
        if nome in conhecidos:
            frase = "Bom te ver "
        else:
            frase =("Prazer em conhecer você ")
            conhecidos.append(nome)
            Memoria.salva_nome(conhecidos)
        return frase + nome

    def manutencao(self, frase):
        if frase == 'manutenção':
            print(self.frases)