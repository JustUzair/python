try:
	import pyttsx3
	import datetime
	import speech_recognition as sr
	import wikipedia
	import webbrowser
	import os
	import random
	import smtplib
except Exception as e:
	speak("something went wrong,Can't import library")

dt=datetime.datetime.now()
try:
	fh=open('C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\password.txt')
	for line in fh:
		if line.startswith('Password'):
			passw=line[9:]
		elif line.startswith('Email'):
			my_email=line[6:]
	fh.close()
except Exception as e:
	speak('Fetching of email and passsword failed')
songs=[]

try:
	#set chrome as default browser
	webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
except Exception as e:
	speak('Something went wronng!')

engine=pyttsx3.init('sapi5') # initializing speech application programming interface
voices=engine.getProperty('voices') # get existing voices 
engine.setProperty('voices',voices[1].id) # choose any voice from an existing ones 

def speak(audio):
	#function to speak to user
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	# function to wish user
	hour=int(datetime.datetime.now().hour)
	if hour<12 and hour>=0:
		speak('Good Morning!')
	elif hour>=12 and hour<16:
		speak('Good Afternoon!')
	else:
		speak('Good Evening!')

def askTask():
	#ask user for task 
	speak('i am Jarvis, Please tell me how may i help you?')

def sendEmail(to_email,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(my_email,passw)
	server.sendmail(my_email,to_email,content)
	server.close()

def takeCommand():
	#get speech commands from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Sorry, I didn't quite hear what you said")  
        return "None"
    return query
if __name__ == '__main__':
	wishMe()
	askTask()
	# Logic to Perform Tasks!
	while True:
		query=takeCommand().lower()

		if 'tell me about' in query:
			if query.startswith('jarvis tell me about'):
				query=query.replace('jarvis tell me about','')
			else:
				query=query.replace('tell me about','')
			results=wikipedia.summary(query,sentences=3)
			speak(results)

		elif 'goodbye' in query:
			speak('goodbye, sir')
			quit()

		elif 'shutdown' in query:
			speak('as you wish, sir')
			quit()
	
		elif 'how are you' in query:
			speak('i am doing well sir, thanks for asking') 
		
		elif 'what time is it' in query:
			time_str=datetime.datetime.now().strftime('%H:%M')
			time_str='it is '+time_str
			speak(time_str)
		
		elif 'hello jarvis' in query:
			speak("hello sir, it's nice to see you again")
		
		elif 'who are you' in query:
			speak('i am Jarvis, Sir')

		elif 'what is your name' in query:
			speak('it is Jarvis, Sir')
		
		elif 'open youtube' in query:
			try:
				speak('Opening Youtube')
				webbrowser.get('chrome').open('youtube.com')
			except Exception as e:
				speak('Command execution failed')

		elif 'open google' in query:
			speak('Opening Google')
			webbrowser.get('chrome').open('google.com')

		elif 'open stackoverflow' in query:
			speak('Opening stckoverflow')
			webbrowser.get('chrome').open('stackoverflow.com')
		
		elif 'play music' in query:
			music_dir="G:\\songs\\eminem"
			songs.extend(os.listdir(music_dir))
			
			random.shuffle(songs)
			os.startfile(os.path.join(music_dir,songs[0]))

		elif 'send email' in query:
			try:
				speak('whom should i send it to')
				to_email=str(input('Enter email address:'))
				speak('what do you want me to send')
				content=takeCommand()
				sendEmail(to_email,content)
				speak('sir email has been deliverd successfully')
			except Exception as e:
				speak('sorry sir, delivery of email failed')
		elif 'thank you' in query:
			speak("you're welcome")

		elif 'what month is it' in query:
			month="It's"+dt.strftime('%B')
			speak(month)

		elif 'what year is it' in query:
			year="It's"+dt.strftime('%Y')
			speak(year)

		elif 'today\'s date' in query:
			today_date=dt.strftime('%d %B %Y')
			speak(today_date)	

		elif "what day is today" in query:
			today="It's"+dt.strftime('%A')
			speak(today)

		elif "i'm sorry" in query:
			speak("It's Okay!")

		elif 'open chrome' in query:
			try:
				speak('Opening Google Chrome')
				os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
			except Exception as e:
				speak('Cannot open Google Chrome')

		elif 'open sublime' in query:
			try:
				speak('Opening Sublime Text Editor..')
				os.startfile('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')	
			except Exception as e:
				speak('Cannot open sublime text editor')

		elif 'open wynk' in query:
			try:
				speak('Opening Wynk Music')
				webbrowser.get('chrome').open('wynk.com')
			except Exception as e:
				speak('Cannot open wynk music')

		elif 'open spotify' in query:
			try:
				speak('Opening spotify')
				webbrowser.get('chrome').open('spotify.com')
			except Exception as e:
				speak('Cannot open spotify')
		elif 'open a website' in query:
			try:
				speak('What website do you want me to open?')
				url=input('Enter website Url: ')
				webbrowser.get('chrome').open(url)
				peak(f'Opening {url}')
			except Exception as e:
				speak(f'Cannot open {url}')
		elif 'open zoom' in query:
			try:
				speak('Opening Zoom Video Communications')
				os.startfile('C:\\Users\\user\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
			except Exception as e:
				speak("can't open zoom, something went wrong")
