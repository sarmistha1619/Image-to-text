import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\Other\sarmistha pal\BN\projects\pytesseract\tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe'
from PIL import image

img = image.open('imgtotxt.jpg')

text = tess.image_to_string(img)

print(text)