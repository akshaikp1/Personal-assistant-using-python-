import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyowm



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def welcomeMessage():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is aric here. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing input...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
         print("Can you please repeat...")
         return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akki0510@gmail.com', 'anagha18')
    server.sendmail('akki0510@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    welcomeMessage()
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
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'what can you do' in query:
            speak("i can do internet surfing, search in wikipedia , play music, update you on weather forecast , send email on your behalf, tell you the current time and you can always modify or personalize the way you want ")
            speak("what would you like me to do")

        elif 'facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'search google' in query:
            speak("what would you like to search")
            q = takeCommand()
            webbrowser.open( "https://www.google.com/search?source=hp&ei=CRzyXaPcG_fXz7sP3e6-uAc&q="+q)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\aksha\\Music\\fav'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'send a mail' in query:
            try:
                speak("to whom should i send")
                to = takeCommand().lower()
                mail = {'akshay': 'akshaikp1@gmail.com', 'joseph': 'akshaydileep@karunya.edu.in'}
                if(to == 'send it to akshay' or 'send to akshay' or 'akshay'):
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(mail['akshay'], content)
                    speak("Email has been sent!")

                elif(to == 'send it to joseph' or 'send to joseph' or 'joseph'):
                    speak("What should I say?")
                    content = takeCommand()
                    sendEmail(mail['joseph'], content)
                    speak("Email has been sent!")
                else:
                    speak("sorry the provided contact is not stored in my database.")
                    
            except Exception as e:
                print(e)
                speak("Sorry i wasn't able to send the mail please try again")

        elif 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                speak("As you say sir, Have a Good day")
                exit()
            else:
                speak("As you say sir, Have a good night")
                exit()
        
        elif 'weather' in query:
            own = pyowm.OWM('44c64ad532fd41e5c1f2a1adaf1da03c')
            location = own.weather_at_place('Coimbatore')
            weather = location.get_weather()
            temperature = weather.get_temperature('celsius')
            print("The temperature in coimbatore is: ",temperature['temp'], "°C ")
            gettemp = temperature['temp']
            speak(f"The temperature in coimbatore is {gettemp} degree celsius")

        elif query != 'none':
            webbrowser.open("https://www.google.com/search?source=hp&ei=CRzyXaPcG_fXz7sP3e6-uAc&q="+query)


