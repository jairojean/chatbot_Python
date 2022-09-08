from ChatBot import ChatBot

Bot = ChatBot('jairo')

while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if frase == 'tchau':
        break
    else:
        print('Digite outra coisa')
print("Tchau Tchau...!!!")
