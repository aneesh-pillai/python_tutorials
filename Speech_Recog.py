import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia

print(datetime.now().strftime("%I:%M:%S %p"))
listener = sr.Recognizer()
engine = pyttsx3.init()
on = True

def process_voice(voice):
    voice = voice.lower()
    stop_words = ['who', 'what', 'is', 'are', 'the']
    temp_voice = voice.split()
    temp_result = [word for word in temp_voice if word not in stop_words]
    result = ' '.join(temp_result)
    return result


def talk(text):
    if text == '':
        engine.say("Hello Am your assistant,what can I do for you?")
    elif "time" in text:
        engine.say("Current time is " + datetime.now().strftime("%I:%M %p"))
    elif "than you" in text:
        engine.say("No problem")
    elif "who is" in text:
        my_object = process_voice(text)
        info = wikipedia.summary(my_object, 1)
        engine.say(info)
    elif "what is" in text:
        my_object = process_voice(text)
        info = wikipedia.summary(my_object, 1)
        engine.say(info)

    elif "bye bye" in text:
        engine.say("Bye bye for now")
        quit()
    else:
        engine.say(text)
    engine.runAndWait()

talk("Welcome, What can I do for you?")


def listen():
    try:

        with sr.Microphone() as source:
            print("I am listening....")
            voice = listener.listen(source)
            comment = listener.recognize_google(voice).lower()
            print(comment)
            talk(comment)
            # print(result)

    except:
        msg = "Sorry something went wrong!"
        talk(msg)
        quit()
        pass

