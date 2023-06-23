import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import ssl
import pywhatkit
import smtplib
from email.message import EmailMessage
email_sender = 'youremail@website.com'
email_password = 'youremailkey'

r = sr.Recognizer()
engine = pyttsx3.init()
emailreceiver = "someone@example.com"
subject = None
body = None
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        process_command(command)

    except sr.UnknownValueError:
        speak("i beg your pardon maa lick")
        listen()


def get_recipient():
    pass


def get_subject():
    pass


def get_body():
    pass


def process_command(command):
    command = command.lower()

    if "hello" in command:
        speak("Hello, I am  Mangal  AI built by ABHYUDH, How can I assist you?")


    elif 'stop' in command or 'exit' in command or 'ruk ja' in command or 'bye' in command or 'bas' in command:
        speak("Goodbye! Have a great day.")
        exit()

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")

    elif "search" in command:
        search_query = command.split("search", 1)[1].strip()
        search_wikipedia(search_query)

    elif "send a mail" in command:

        recipient = get_recipient()

        subject = get_subject()

        body = get_body()

        em = EmailMessage()

        em['From'] = email_sender

        em['To'] = recipient

        em['Subject'] = subject

        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)

            smtp.sendmail(email_sender, recipient, em.as_string())

        speak("Mail sent.")

        speak("Any other task?")
    elif "open website" in command:
        website = command.split("open website", 1)[1].strip()
        open_website(website)

    elif "open application" in command:
        application = command.split("open application", 1)[1].strip()
        open_application(application)

    elif 'play music' in command or 'play songs' in command or 'play a song' in command:
        speak("Which song do you want me to play?")
        song = command.lower()
        if song == None:
            speak("I beg your pardon maa lick")
            song = command.lower()
        if 'any' == song:
            pywhatkit.playonyt("SHAPE OF YOU")
        else:
            pywhatkit.playonyt(song)



    else:
        speak("Sorry, I didn't understand that.")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:3]  # Get the top 3 options
        speak(f"There are multiple options. Here are the first three: {', '.join(options)}.")

    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any relevant information.")

# Define a function to open a website
def open_website(website):
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "pinterest": "https://in.pinterest.com",
        "flipkart": "https://www.flipkart.com",
        "amazon": "https://www.amazon.com",
        "ajio":"https://www.ajio.com",
        "shopify":"www.shopify.com"

    }

    if website in urls:
        webbrowser.open(urls[website])
    else:
        speak("Sorry, Please provide me the link for the website")
        webby = str(input("link: "))
        webbrowser.open(webby)

def open_application(application):
    app_paths = {
        "notepad": "C:\\Windows\\system32\\notepad.exe",
        "calculator": "C:\\Windows\\system32\\calc.exe",
    }

    if application in app_paths:
        os.startfile(app_paths[application])
    else:
        speak("Sorry, I don't know how to open that application.")

speak("Hello, I am  Mangal  AI built by ABHYUDH , How can I assist you?")
while True:
    listen()
