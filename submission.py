import pyautogui
import os
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C'
myScreenshot = pyautogui.screenshot()
myScreenshot.save('image1.png')

img = Image.open("image1.png")
text = tess.image_to_string(img)
print(text)
