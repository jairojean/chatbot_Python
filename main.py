from Config.ChatBot import ChatBot

Bot = ChatBot('Chappie')
while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)
    if frase == 'tchau':
        break
