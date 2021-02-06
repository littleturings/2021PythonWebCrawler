import pytesseract
from PIL import Image
img = Image.open("yzm.jpg")
str = pytesseract.image_to_string(img)
print(str)