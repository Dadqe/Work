import pytesseract
from PIL import Image

img = Image.open(r'E:\Work\testrus.jpg')

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)

# with open('testrus.txt', 'w') as file:
#     file.write(text)