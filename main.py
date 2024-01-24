#Usar versão 3.8 do python ou inferior
#pip install rasa
#pip uninstall python-dateutil sqlalchemy
#pip install python-dateutil==2.7.5 sqlalchemy==1.2.19
#pip uninstall rasa pykwalify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Meu ChatBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinando o chatbot com o corpus em português
trainer.train("chatterbot.corpus.portuguese")

while True:
    request = input('Você: ')
    response = chatbot.get_response(request)
    print('ChatBot: ', response)