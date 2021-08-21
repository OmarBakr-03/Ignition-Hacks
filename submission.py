#Please read the README file before assessing

import pyautogui
import os
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C'
myScreenshot = pyautogui.screenshot()
myScreenshot.save('image1.png')


class classyClass:
  def __init__(self, name, width, length):
    self.name = name
    self.width = width
    self.length = length
  
  def getName(self):
    return self.name
  def getWidth(self):
    return self.width
  def getLength(self):
    return self.length

thing = classyClass('jason', 144, 144)

def welcomeMessage():
    #Will give options and use try and catch in the process as well as variables
    print("Welcome, what would you like to do?")
    print("Option 1: Name Alert")
    print("Option 2: Record Meet Audio")
    print("Option 3: Save Meet Transcript")
    getResponse()
    
def getResponse():
    while(True):
        try:
            welcomeResponse = int(input("Print Please enter a number: "))
        except ValueError:
            print("Please enter an Integer from 1-3")
        else:
          if welcomeResponse in [1,2,3]:
            break
          else:
              print("Please enter an Integer from 1 to 3")
    if welcomeResponse == 1:
        nameAlert()
    elif welcomeResponse == 2:
        recordMeetAudio()
    elif welcomeResponse == 3:
        saveMeetTranscript()

def nameAlert():
    while True:
        img = Image.open("image1.png")
        text = tess.image_to_string(img)
        print(text)
        file = open("test.txt","w")
        file.write(text)
        file.close()

        if thing.getName() in text:
            break

def recordMeetAudio():
    print("Hi")
    
def saveMeetTranscript():
    print("Hi")

