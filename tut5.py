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
# print((2+3)*5/2%6)  #precedence in python

# s = "Rooose"
# v = {i for i in s}
# print(len(v)) # ans = 4, cuz it counts different characters in the word

# t = [0]
# s1 = s2 = t
# s1 = s1 + [1]
# s2 += [1]
# print(t)
#Ans [0, 1]

# s = [100, 84, 63, 97]
# s_sort = s.sort()
# print(s[::-1][0])  #Ans  It's 100, because when you sort it, this is s = [63, 84, 97, 100] then you reverse it with [start from 0:until the end of it: and substract 1 then the list would be [100, 97, 84, 63] and your are asking the value in index 0 so the value 100 is the right answer.

# s = "apple"
# x = s.find('p')
# y = s.find('m')
# z = s.find('')
# print(x+y+z)  #0 since value of X is 1...value of Y is -1.....value of z is 0..


