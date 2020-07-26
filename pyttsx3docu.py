import pyttsx3

#LISTENING FOR EVENTS
'''
import pyttsx3
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
# INTERRUPTING AN UTTERANCE
'''
import pyttsx3
def onWord(name, location, length):
   print ('word', name, 11, length)
   if location > 10:
      engine.stop()
engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
#CHANGING VOICES
'''
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
# Changing speech rate
'''
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
# Changing volume
'''
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''

# Running a driver event loop
'''
engine = pyttsx3.init()
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
   if name == 'man':
      engine.say('What a lazy woman!', 'woman')
   elif name == 'woman':
      engine.endLoop()
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown man jumped over the lazy woman.', 'woman')
engine.startLoop()
'''

#Using an external event loop
'''
engine = pyttsx3.init()
engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
engine.startLoop(False)
# engine.iterate() must be called inside externalLoop()
engine.iterate()
# externalLoop()
engine.endLoop()
'''
