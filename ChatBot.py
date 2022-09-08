import json
import sys
import os
import subprocess as os_linux
class ChatBot:
    def __init__(self, nome):
        try:
            memoria = open('memoria/arquivo.json','r')
        except FileNotFoundError:
            memoria = open('memoria/arquivo.json','w')
            memoria.write('["Adamus"]')
            memoria.close()
            memoria = open('memoria/arquivo.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        self.historico = []
        memoria.close()
        self.frases = {'oi': 'Olá, qual seu nome?', 'ola': 'Ooi', 'opa': 'Opá', 'tchau': 'Thau Tchau, foi bom falar com você.'}

    def escuta(self):
        frase= input('>: ')
        frase = frase.lower()
        return frase

    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'aprende':
            novidade = input('Digite o que vou ouvir: ')
            resposta = input('Digite o que responderei: ')
            self.frases[novidade] = resposta
            return 'Aprendido!'

        if self.historico[-1] == "Olá, qual seu nome?":
            nome = self.pega_nome(frase)
            resp = self.respondeNome(nome)
            return  resp
        ## Comandos de manutenção
        if frase == 'frases':
            return self.frases
        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
            return 'Não entendi,amigo.'
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

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = "Bom te ver "
        else:
            frase =("Prazer em conhecer você ")
            self.conhecidos.append(nome)
            memoria = open('memoria/arquivo.json','w')
            json.dump(self.conhecidos, memoria)
            memoria.close()
        return frase + nome
    def pega_nome(self, nome):
        nome = nome.title()
        return nome

    def teste(self):
        print(self.nome, self.conhecidos)
