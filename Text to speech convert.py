!pip install gTTS
from gtts import gTTS  #we have import this module for text to speech conversion 
text="hello guys how are you ,I am fine .what about u" #  text that u want to convert

language ='en'#en is for english

obj=gTTS(text=text,lang=language,slow =False) #we have used slow=false beacuse our video will have high speed 
obj.save("sample.mp3")

# to open the video file automaticlly we have to import os
os.system("sample.mp3")
