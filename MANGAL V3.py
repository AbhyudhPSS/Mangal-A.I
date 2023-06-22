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
email_sender = 'abhyudhsolanki@gmail.com'
email_password = 'samjehzqashoikar'

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
    except Exception as e:
        speak("i beg your pardon maa lick")
        return "None"

    return query


if __name__ == '__main__':
    speak("Hello, I am  Mangal  AI built by ABHYUDH")
    authenticated = False

    while not authenticated:
        speak("Please provide your identity.")
        identity = input("Identity: ").lower()

        if identity == 'abhyudh' or identity == 'avi':
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

         elif 'how are you' in query:
             speak("I am super amazing fantastic")

         elif 'i love you' in query:
             speak("Ohh....no one has ever said that to me... that is so nice of you maa lick")
         elif 'send a mail' in query:
                speak("Whom do you want to send the mail")
                mailr = takeCommand().lower()
                if 'didi' in mailr:
                    email_receiver = "smimansha2408@gmail.com"
                elif 'myself' in mailr:
                    email_receiver = "abhyudh@gmail.com"
                elif 'papa' in mailr:
                    email_receiver = "vikas@doomshell.com"
                elif 'mama' in mailr:
                    email_receiver = "priyanka@doomshell.com"
                else:
                    speak("I don't have the mail details for that.......kindly provide me the mail address")
                    print("Mail: ", end="")
                    atoxyz=query
                    atoxyzadd = str(input())
                    email_receiver = atoxyzadd
                speak("What should be the subject of the mail?")
                subject = takeCommand().lower()

                speak("What should be the body of the mail?")
                body = takeCommand().lower()

                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['subject'] = subject
                em.set_content(body)

                context = ssl.create_default_context()

                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
                speak("Mail sent Boss")
                speak("Any other task?")

         elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube Right Away Sir...")

         elif 'play music' in query or 'play songs' in query or 'play a song' in query:
             speak("Which song do you want me to play?")
             song = takeCommand().lower()
             if song == None:
                 speak("I beg your pardon maa lick")
                 song = takeCommand().lower()
             if 'any' == song:
                 pywhatkit.playonyt()
             else:
                pywhatkit.playonyt(song)


         elif 'google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening google Right Away Sir...")

         elif 'amazon' in query:
            webbrowser.open("https://www.amazon.com")
            speak("Opening amazon Right Away Sir...")

         elif 'flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("Opening flipkart Right Away Sir...")

         elif 'mail' in query:
            webbrowser.open("https://www.gmail.com")
            speak("Opening mail Right Away Sir...")

         elif 'pinterest' in query:
            webbrowser.open("https://in.pinterest.com")
            speak("Opening pinterest Right Away Sir...")

         elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

         elif 'stop' in query or 'exit' in query or 'ruk ja' in query or 'bye' in query or 'bas' in query:
            speak("Goodbye!")
            break