'''
import pyaudio
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    
    for age in range(1,6):
        age=int(input("Enter your age:\n"))
        if(age>18 and age<70):
            print("You can drive a car")
            speak("You can drive a car")
        elif(age<18 and age>6):
            print("You cannot drive a car")
            speak("You cannot drive a car")
        elif(age==18):
            print("You need to do physical test")
            speak("You need to do physical test")
        elif(age<=6):
            print("You have to wait for it ,Kid")
            speak("You have to wait for it ,Kid")
        elif(age>=70 and age<=289):
            print("Sorry Sir! You are a senior citizen")
            speak("Sorry Sir! You are a senior citizen")
        else:
            speak("Guruji give me some blessings")    
'''


