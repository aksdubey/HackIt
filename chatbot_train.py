from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

chatbot = ChatBot(
					'Training Example',
#					storage_adapter='chatterbot.storage.SQLStorageAdapter',
#					database_uri='sqlite:///database.sqlite3'
				logic_adapters=[
								'chatterbot.logic.MathematicalEvaluation',						
								'chatterbot.logic.MathematicalEvaluation',						
								{	
									'import_path':'chatterbot.logic.BestMatch',
									'default_response': 'I am sorry, but I do not understand.',
									'maximum_similarity_threshold': 0.90
								}	
    ]
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "C:/Python37/Lib/site-packages\chatterbot_corpus\data\english/"
    #"C:/Users/ADMIN\chatterbot-corpus-master\chatterbot_corpus\data\english/"
	#"./data/CUBE/"
)
# bot.trainer(ChatterBotCorpusTrainer)
# bot.train("chatterbot.corpus.english")
# for files in os.listdir('C:/Users/ADMIN\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
	# data = open('C:/Users/ADMIN\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files, 'r').readlines()
	# bot.train(data)

# while True:
		# message = input('You:')
		# if message.strip()!='Bye':
				# reply= chatbot.get_response(message)
				# print('YAKSHA:',reply)

		# if message.strip() == 'Bye':
				# print('YAKSHA:Bye') 
				# break
# def setup():
    # chatbot = ChatBot('Bot')
    # storage_adapter=('chatterbot.storage.SQLStorageAdapter')
    # trainer=('chatterbot.trainers.ListTrainer')
    # corpus_path = 'C:/Users/ADMIN\chatterbot-corpus-master\chatterbot_corpus\data\english/'
    # for file in os.listdir(corpus_path):
    #    convData = open('C:/Users/ADMIN\chatterbot-corpus-master\chatterbot_corpus\data\english/' + file,'r').readlines()
        #chatbot.set_trainer(ListTrainer)
        #print("hello")
        #trainer.train(corpus_path + file)
        #trainer = ChatterBotCorpusTrainer(chatbot)
        #chatbot.train(convData)
        #trainer.train(convData)
        #print("Training completed")
#setup()
