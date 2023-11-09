import datetime
import pyttsx3
import speech_recognition as sr


def take_commands():
	
	# Making the use of Recognizer and Microphone
	# Method from Speech Recognition for taking
	# commands
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			
			# for listening the command in indian english
			Query = r.recognize_google(audio, language='en-in')
			
			# for printing the query or the command that we give
			print("the query is printed='", Query, "'")
		except Exception as e:
			
			# this method is for handling the exception 
			# and so that assistant can ask for telling 
			# again the command
			print(e) 
			print("Say that again sir")
			return "None"
		
	return Query

def Speak(audio):
	
	# initial constructor of pyttsx3
	engine = pyttsx3.init()
	
	# getter and setter method
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(audio)
	engine.runAndWait()


# Driver Code
if __name__ == '__main__': 
	command=take_commands()
	
	Speak(command)
