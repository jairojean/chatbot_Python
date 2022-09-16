import json
import sys
import os
import subprocess as os_linux
class Memoria:

    @staticmethod
    def busca_nome():
        try:
            nomes = open('memoria/nomes.json', 'r')
            conhecidos = json.load(nomes)
            nomes.close()
            return conhecidos
        except FileNotFoundError:
            nomes = open('memoria/nomes.json', 'w')
            nomes.write('["Adamus"]')
            nomes.close()
            nomes = open('memoria/nomes.json', 'r')
            conhecidos = json.load(nomes)
            nomes.close()
        return conhecidos

    def salva_nome(conhecidos):
        memoria = open('memoria/nomes.json', 'w')
        json.dump(conhecidos, memoria)
        memoria.close()

    @staticmethod
    def busca_conversa():
        memoria = open('memoria/conversas.json', 'r')
        conversas = json.load(memoria)
        memoria.close()
        return conversas

    def salva_conversa(frase):
        memoria = open('memoria/conversas.json', 'w')
        json.dump(frase, memoria)
        memoria.close()

