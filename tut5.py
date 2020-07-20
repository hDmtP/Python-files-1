'''
import winsound
fr = 2599        #frequency
d = 10000        #duration
winsound.Beep(fr,d)
'''

'''
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone as source:
    print("SPEAK....")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:{}".format(text))  
    except:
        print("Sorry, I cannot recognize you:(")
'''        

