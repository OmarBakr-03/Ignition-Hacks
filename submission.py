#Please read the README file before assessing

#Importing Libraries
import pyautogui
import os
import pytesseract as tess
from PIL import Image

#A line we need for the OCR code but im still figuring out how this works
tess.pytesseract.tesseract_cmd = r'C'



class specifications: #a class of the person who's using the program's specifications 
  def __init__(self, name, width, length):
    self.name = name #name
    self.width = width #width dimension of the tab of google meet
    self.length = length #height dimension of the tab of google meet
  
  #functions to retrieve the attributes
  def getName(self):
    return self.name
  def getWidth(self):
    return self.width
  def getLength(self):
    return self.length

    #user input for this part is in progress

thing = specifications('jason', 144, 144) #creates example object

def welcomeMessage():#displays the main menu message
    #Will give options and use try and catch in the process as well as variables
    print("Welcome, what would you like to do?")
    print("Option 1: Name Alert")
    print("Option 2: Record Meet Audio")
    print("Option 3: Save Meet Transcript")
    getResponse() 
    
def getResponse(): #gets the user's response and checks for error
    while(True):
        try:
            welcomeResponse = int(input("Print Please enter a number: "))
        except ValueError: #when the value isn't an integer
            print("Please enter an Integer from 1-3")
        else: 
          if welcomeResponse in [1,2,3]: #when the number is valid (between and including 1 and 3)
            break
          else: #when the number isn't 1,2 or 3
              print("Please enter an Integer from 1 to 3")
    #runs the corresponding functions
    if welcomeResponse == 1:
        nameAlert()
    elif welcomeResponse == 2:
        recordMeetAudio()
    elif welcomeResponse == 3:
        saveMeetTranscript()

def nameAlert(): #the function which alerts the person when their name is called
    while True:
        #Takes a screenshot and saves it
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('image1.png')
        #Use OCR to extract text from Image
        img = Image.open("image1.png")
        text = tess.image_to_string(img)
        #It puts this text in the text file called test
        file = open("test.txt","w")
        file.write(text)
        file.close()
        #It will exit when it gets the persons name (We're still deciding on this but just an idea)
        if thing.getName() in text:
            print('name is called')
            break

#Some empty functions which we still gotta work on
def recordMeetAudio():
    print("Hi")
    
def saveMeetTranscript():
    print("Hi")

