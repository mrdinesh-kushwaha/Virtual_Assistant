import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hello sir , i am your virtual assistant , how can i help you')
def take_command():
    command = ""  # Initialize with an empty string or some default value
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'g-star' in command:
                command = command.replace('G-Star', '')
                print(command)
            if 'stop' in command:  # Break the loop if the stop command is detected
                return command
    except sr.UnknownValueError:
        print("Sorry, I did not hear your request. Please repeat.")
        talk("Sorry, I did not hear your request. Please repeat.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")

    return command
def run_gstar():
    while True:
        command = take_command()
        print(command)
        sites =[["youtube","https://youtube.com"], ["wikipedia","https://www.wikipedia.com"], ["google","https://www.google.com"],
                ["my lead code profile", "https://leetcode.com/mrdineshkumar/"],
                ["my linkedin profile", "https://www.linkedin.com/in/mrdinesh-kumar/"], ["my college sim", "https://glbg.servergi.com:8072/ISIMGLB/Login"],
                ["geeksforgeeks", "https://www.geeksforgeeks.org/"], ["my gmail", "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],
                ["gl bajaj website","https://www.glbitm.org/"],["my github profile","https://github.com/imdinesh-kushwaha"],
                ["my hackerrank profile","https://www.hackerrank.com/profile/dineshk00"], ["chat gpt","https://chat.openai.com/"],
                ["google bard","https://bard.google.com/chat"],["google ward","https://bard.google.com/chat"],["google badh","https://bard.google.com/chat"],]
        for site in sites:
            if f"Open {site[0]}".lower() in command.lower():
                talk(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if 'quit' in command:
            print('Ok Sir ! Thank you ! Have a nice day! ')
            talk('Ok Sir ! Thank you for giving your precious Time ! Have a nice day! ')
            break
        if 'nothing' in command:
            print('Ok Sir ! Thank you ! Have a nice day! ')
            talk('Ok Sir ! Thank you for giving your precious Time ! Have a nice day! ')
            break
        if 'stop' in command:
            print('Ok Sir ! Thank you ! Have a nice day! ')
            talk('Ok Sir ! Thank you for giving your precious Time ! Have a nice day! ')
            break
        if 'no thanks' in command:
            print('Ok Sir ! Thank you ! Have a nice day! ')
            talk('Ok Sir ! Thank you for giving your precious Time ! Have a nice day! ')
            break
        if 'are you busy' in command:
            talk('Noo , I am always available for you...so tell me sir , what can i do for you..')
        if 'r u busy' in command:
            talk('Noo , I am always available for you...so tell me sir , what can i do for you..')
        if 'what can you do for me' in command:
            talk('I will try to fulfill what you want to ask...')
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%S %p')
            print('Current time is ' + time)
            talk('Current time is ' + time)
        elif 'date' in command:
            date = datetime.datetime.now().strftime('%d-%B-%Y')
            print('Today date is ' + date)
            talk('Today date is ' + date)
        elif 'open code editor' in command:
            path = "C:\\Users\\DINESH KUMAR\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(path)
        elif 'open vs code' in command:
            path = "C:\\Users\\DINESH KUMAR\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(path)
        elif 'open chrome browser' in command:
            pathe = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(pathe)
        elif 'wikipedia' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'are you single' in command:
            talk('The concept of being single doesnt really apply to me,.I dont have romantic relationships or experience emotions in the same way humans do.'
                 'However,'
                 'Is there anything else you d like to know about me or how I work? ..I am happy to share more!')
        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        elif 'how r u g-star' in command:
            talk('I am good. thank you for asking. and what about you ')
        elif 'how are you g-star' in command:
            talk('I am good. thank you for asking. what about you ')
        elif 'i am also good' in command:
            talk('Great, Have a good day')
        elif 'kaise ho' in command:
            talk(' bilkul badhiya')
        elif 'what r u doing' in command:
            talk('Nothing special. tell me how can i help you ')
        elif 'what are you doing' in command:
            talk('I am thinking about you. tell me how can i help you ')
        elif 'whats your name' in command:
            talk('my name is G-star  . how can i help you? ')
        elif 'what is your name' in command:
            talk('my name is G-star  . how can i help you?')
        elif 'how r u' in command:
            talk('I am good. thank you for asking. and what about you ')
        elif 'how are you' in command:
            talk('I am good. thank you for asking. what about you ')
        elif 'what ise your name' in command:
            talk('my name is G-star . how can i help you ?')
        elif 'hello' in command:
            talk('hii sir. I am your Virtual assistant. how can i help you')
        elif 'whats my name' in command:
            talk('your name is Dinesh Kushwaha. How can I help you Dinesh')
        elif 'what ise my name' in command:
            talk('your name is Dinesh Kushwaha. How can I help you Dinesh')
        elif 'tell me about yourself' in command:
            talk('sure sir , my name is G-star , and I am your Artificial virtual assistant . I am created by mister Dinesh Kushwaha.'
                 ' and I am always ready to help you. so tell me sir . how can i help you right now ')
        elif 'thanks' in command:
            talk('wellcome sir. i am always glad to help you. so tell me sir how can i help you ')

if __name__ == "__main__":
    run_gstar()
