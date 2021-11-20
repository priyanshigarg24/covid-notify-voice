import pyttsx3
import speech_recognition as sr
import datetime
engine=pyttsx3.init('sapi5') # Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications
#to use windows voice
voices=engine.getProperty('voices')
print(voices[0].id)
#voices available on windows)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
      hour=int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
          speak("Good morning")
     
      elif hour>=12 and hour<18:
          speak("Good afternoon")
      
      else:
          speak("Good evening")
     
      speak("I am your assistant. How can i help you?")
wishMe()

#it itakes microphone input from user and return string output
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        r.pause_threshold = 1  #seconds of non-speaking audio before a sentence in completed
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    
    return query

takeCommand()
