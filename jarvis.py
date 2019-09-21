import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit = 5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:  
        print("Sorry, I am not able to recognize please say it again")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hkm0072001@gmail.com', '9450944136')
    server.sendmail('hkm0072001@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
   
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")
            speak("opening geeksforgeeks")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\jarvis_music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open sublime' in query:
            Path = "C:\Program Files\Sublime Text 3\\sublime_text.exe"
            os.startfile(Path)

        elif 'email to hkm' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "himanshuihs2001@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email") 

        elif 'who are you' in query: 
            speak('''Hello, I am Jarvis. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra''') 
           

        elif 'who made you' in query or 'created you' in query: 
            speak('I am created by HKM')
           

        elif 'language' in query or 'written' in query: 
            speak('I am written in python language')
          

        elif 'sleep' in query or 'quit' in query: 
            speak("Ok sir have a nice day")
            break 
          
          