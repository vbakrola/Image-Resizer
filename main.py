import PIL
from PIL import Image
import os

path = '.'
if not os.path.exists('resize'):
    os.mkdir('resize')
for file in os.listdir(path):
    current = os.path.join(path, file)
    #os.remove(current + '\\Thumbs.db')
    if os.path.isdir(current):
        #print file
        for images in os.listdir(current):
            img = Image.open(current + '\\' + images).convert('1',dither=Image.NONE)
            img = img.resize((28, 28), PIL.Image.ANTIALIAS)
            if not os.path.exists('.\\resize\\' + file):
                os.makedirs('.\\resize\\' + file)
            img.save('.\\resize\\' + file + '\\' + images)