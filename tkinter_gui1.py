from chatterbot import ChatBot
import tkinter as tk
try:
	import ttk as ttk
	import ScrolledText
except ImportError:
	import tkinter.ttk as ttk
	import tkinter.scrolledtext as ScrolledText
import time, os
import pyttsx3
import speech_recognition as sr


class TkinterGUIExample(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.chatbot = ChatBot(
			"GUI Bot",#storage_adapter="chatterbot.storage.SQLStorageAdapter",
			logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
			#database_uri="sqlite:///database.db"
		)
		self.title("YAKSHA")
		self.initialize()



	def initialize(self):
		
		self.grid()
		self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
		self.conversation_lbl.grid(column=0, row=0, columnspan=2, sticky='W', padx=3, pady=3)
		
		self.conversation = ScrolledText.ScrolledText(self, state='disabled')
		self.conversation.grid(column=0, row=1, columnspan=2, sticky='nesw', padx=3, pady=3)
		
		self.respond = ttk.Button(self, text='ASk question', command=self.process_speech)
		#self.respond.grid(column=1, row=2, sticky='nesw', padx=3, pady=3)
		ttk.Style().configure("TButton", padding=3, relief="flat",background="red")
		self.respond = ttk.Button(self,text='Get Response', command=self.get_response)
		self.respond.grid(column=1, row=3,sticky='nesw', padx=3, pady=3)
		self.usr_input = ttk.Entry(self, state='normal')
		self.usr_input.grid(column=0, row=3, sticky='nesw', padx=3, pady=3)
		
		

	def get_response(self, event=None):
		user_input = self.usr_input.get()
		self.say_out_loud(str(user_input), 1)
		self.usr_input.delete(0, tk.END)
		response = self.chatbot.get_response(user_input)
		self.conversation['state'] = 'normal'
		self.conversation.insert(			
			tk.END, "You: " + user_input + "\n" + "Yaksha: " + str(response.text) + "\n"
		)
		self.say_out_loud(str(response.text), 0)
		self.conversation['state'] = 'disabled'
		
	def say_out_loud(self, text_speech, male_or_female):
		engine = pyttsx3.init() # object creation
		""" RATE"""
		rate = engine.getProperty('rate')   # getting details of current speaking rate
		print (rate)                        #printing current voice rate
		engine.setProperty('rate', 125)     # setting up new voice rate
		"""VOLUME"""
		volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
		print (volume)                          #printing current volume level
		engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
		"""VOICE"""
		voices = engine.getProperty('voices')       #getting details of current voice
		if male_or_female is 0:
			engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
		elif male_or_female is 1:
			engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
		engine.say(text_speech)
		engine.runAndWait()
		engine.stop()
	
	def process_speech(self):
		r = sr.Recognizer()
		mic = sr.Microphone()
		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		print('speech ennds')
		speech_text = r.recognize_google(audio)
		print('speech text' + str(speech_text))
		self.say_out_loud(str(speech_text), 1)
		self.usr_input.delete(0, tk.END)
		response = self.chatbot.get_response(str(speech_text))
		self.conversation['state'] = 'normal'
		self.conversation.insert(			
			tk.END, "You: " + str(speech_text) + "\n" + "Yaksha: " + str(response.text) + "\n"
		)
		self.say_out_loud(str(response.text), 0)
		self.conversation['state'] = 'disabled'


gui_example = TkinterGUIExample()
gui_example.bind('<Return>', gui_example.get_response)
gui_example.mainloop()
			