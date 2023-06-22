import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import ssl
import os
import pywhatkit
import smtplib
from email.message import EmailMessage
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
email_sender = 'youremail@website.com'
email_password = 'youremailkey'

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
    except Exception as e:
        speak("i beg your pardon maa lick")
        return "None"

    return query

def open_application(application):
    app_paths = {
        "notepad": "C:\\Windows\\system32\\notepad.exe",
        "calculator": "C:\\Windows\\system32\\calc.exe",

    }

    if application in app_paths:
        os.startfile(app_paths[application])
    else:
        speak("Sorry, I don't know how to open that application.")



if __name__ == '__main__':
    speak("Namaskar, I am Mangal ai built by the great programmer Abhyudh")
    authenticated = False

    while not authenticated:
        speak("Please provide your identity.")
        identity = input("Identity: ").lower()

        if identity == 'abhyudh' or identity == 'your name':
            authenticated = True
            speak("Access granted. Welcome Maa lick!")
            speak("What shall we do today?")
        else:
            speak("Access denied.")

    while True:
         query = takeCommand().lower()
         if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

         elif 'stop' in query or 'exit' in query or 'ruk ja' in query or 'bye' in query or 'bas' in query:
             speak("Goodbye! Have a great day.")
             exit()
         elif 'how are you' in query:
             speak("I am super amazing fantastic")

         elif 'i love you' in query:
             speak("Ohh....no one has ever said that to me... that is so nice of you maa lick")

         elif 'send a mail' in query or 'mail bhejo' in query:
             speak("Whom do you want to send the mail")
             mailr = takeCommand().lower()
             if 'importantdude' in mailr:
                 email_receiver = "someone@example.com"
             elif 'myself' in mailr:
                 email_receiver = "youremail@website.com"
             elif 'importantguy' in mailr:
                 email_receiver = "someone@example.com"
             elif 'importantperson' in mailr:
                 email_receiver = "someone@example.com"
             else:
                 speak("I don't have the mail details for that.......kindly provide me the mail address")
                 print("Mail: ", end="")
                 atoxyz = query
                 atoxyzadd = str(input())
                 email_receiver = atoxyzadd
             speak("What should be the subject of the mail?")
             subject = takeCommand().lower()

             speak("What should be the body of the mail?")
             body = takeCommand().lower()
             speak("To - ", email_receiver)
             speak("Subject - ", subject)
             speak("Body - ", body)
             print("To - ", email_receiver)
             print("Subject - ", subject)
             print("Body - ", body)
             speak("Should I send the mail?")
             emailsendornot = takeCommand().lower()
             if 'yes' in emailsendornot or 'yeah' in emailsendornot:
                 em = EmailMessage()
                 em['From'] = email_sender
                 em['To'] = email_receiver
                 em['subject'] = subject
                 em.set_content(body)

                 context = ssl.create_default_context()

                 with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                     smtp.login(email_sender, email_password)
                     smtp.sendmail(email_sender, email_receiver, em.as_string())
                 speak("Mail sent Maalick")
                 speak("Any other task?")
             else:
                 speak("Alright I am not going to send it")
                 speak("Any other task?")
         elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube Right Away Sir...")

         elif "open app" in query:
             speak("which app should i open?")
             application = takeCommand().lower()
             open_application(application)
             speak("Opening right away maa lick!")

         elif "open website" in query:
             speak("Please provide me the link for the website")
             webby = str(input("link: "))
             webbrowser.open(webby)

         elif 'play music' in query or 'play songs' in query or 'play a song' in query:
             speak("Which song do you want me to play?")
             song = query.lower()
             if song == None:
                 speak("I beg your pardon maa lick")
                 song = query.lower()
             if 'any' == song:
                 pywhatkit.playonyt("SHAPE OF YOU")
             else:
                 pywhatkit.playonyt(song)

         elif 'a jio' in query or 'ajio' in query:
             webbrowser.open("https://www.ajio.com")
             speak("Opening a jio Right Away Sir...")

         elif 'shopify' in query:
             webbrowser.open("https://www.shopify.com")
             speak("Opening shopify Right Away Sir...")

         elif 'google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening google Right Away Sir...")

         elif 'amazon' in query:
            webbrowser.open("https://www.amazon.com")
            speak("Opening amazon Right Away Sir...")

         elif 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("Opening flipkart Right Away Sir...")

         elif 'gmail' in query:
            webbrowser.open("https://www.gmail.com")
            speak("Opening mail Right Away Sir...")

         elif 'pinterest' in query:
            webbrowser.open("https://in.pinterest.com")
            speak("Opening pinterest Right Away Sir...")

         elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
