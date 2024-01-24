#Usar versão 3.8 do python ou inferior
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Meu ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinando o chatbot com o corpus em português
trainer.train("chatterbot.corpus.portuguese")

while True:
    request = input('Você: ')
    response = chatbot.get_response(request)
    print('ChatBot: ', response)