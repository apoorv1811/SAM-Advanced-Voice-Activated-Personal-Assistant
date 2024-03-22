import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from googlesearch import search
import random
import subprocess

# pyttsx3 configurations

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

voiceEngine = pyttsx3.init()

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')

#print(rate)
#print(volume)
#print(voice)

#  speak function defination
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish function defination
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am SAM. how can i help")       

# command taking function 
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.operation_timeout= 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception :
        # print(e)    
        print("Say that again please...")  
        word=random.choice(["Sorry, i didnt get that", "Please ,say that again" , "Pardon..","come again..."])
        speak(word)
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        # searching the wiki

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        # opening random command 

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("opening Google")
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")

        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("www.github.com")  

        elif 'open netflix' in query:
            speak("opening netflix")
            subprocess.call("Netflix")  
 

        elif 'open code' in query:
            speak("opening Code")
            codePath = "D:\\IMP\\Program\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open your code' in query:
            speak("opening my DNA")
            codePath = "D:\\clg\\Projects\\Sam\\SAM.py"
            os.startfile(codePath)

        elif 'open word' in query:
            speak("opening Microsoft Word")
            os.startfile('C:\\Program Files\\Microsoft Office\\Office15\\WINWORD.exe')   


        # google search

        elif "search on google" in query:
            speak("What should i search")
            query=takeCommand()
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
                speak(j)
            speak("should i open this ?")
            query=takeCommand()
            if 'yes' in query:
                os.startfile(j)
            else :
                speak('ok')

     

        # Random commands

        elif 'play music' in query:
            speak("playing your playlist")
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "play random songs on youtube" in query:
            speak("playing random songs!")
            os.startfile('https://www.youtube.com/watch?v=weRTCk-mJyE&list=PLx0sYbCqOb8QTF1DCJVfQrtWknZFzuoAE&index=1')        

        elif "who made you" in query:
            #os.startfile('C:\\Users\\Ambade\\Downloads\\Queen.mp3')
            speak("SAM stands for Shreyas , Atharva , Mrugakshi . they are my creaters....")


        # Hangman code


        elif 'open hangman game with graphics' in query:
            speak("opening hangman ")
            os.startfile('D:\\clg\\Programmes\\Hangman-master\\hangman.py')


        elif 'open hangman game' in query:
            speak("opening hangman ")
            os.startfile('D:\\clg\\Projects\\Sam\\asa_hangman.py')



        # Database Project link :
            
        elif 'open appointment' in query:
            speak("opening hospital appointments")
            os.startfile("C:\\Sam\\appointment.py")

        elif 'display appointments' in query:
            speak("displaying all the current appoiments")
            os.startfile("C:\\Sam\\display.py")

        elif 'update the appointments' in query:
            speak("opening the file to update the appointments") 
            os.startfile("C:\\Sam\\update.py")

        elif "make an appointment" in query:
            speak("booking an appointnment")
            


        
        # to email        
                
        elif "send an email to atharva" in query:
             server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.elho()
             server.starttls()
             server.login("sender@gmail.com","*******") #Add your own email and password
             speak("What should I say?")
             content = takeCommand()
             print(content)
             speak("to whom should i send ?")
             to = "receiver@gmail.com"
             server.sendmail("sender@gmail.com" , to, content)
             speak("message sent")
             server.quit() 
             break      

        
         # Ineraction

        elif "hi" in query:
            word=random.choice(["Hi", "Hello","How can i help you", "Any problem again?"])
            speak(word)

        elif "google assistant" in query:
            word=random.choice(["oh yes !!!!", "that bitch , why? whats the problem", "we are cousins ,although im elder", "why , what did i do wrong?"])
            speak(word)

        elif "siri" in query:
            word=random.choice(["nahhhhhh , its better not to know that...", "Bad choice indeed ", "I am far far far far more better", "we were roommates"])
            speak(word)    

        elif "how are you " in query:
            word=random.choice(["Fine as fresh new wine ","good, what about you"])
            speak(word)

        elif "tell me about yourself" in query:
            word=random.choice([])    

            
         # quit       

        elif "bye" in query  or "that would be all sam" in query:
            speak("i'll go to sleep now")
            break

