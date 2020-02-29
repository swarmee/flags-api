import json
import io
from PIL import Image, ImageDraw, ImageFont
import functools


def create_image(imageText):
    img = Image.new('RGB', (25, 20), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)
    imageText = imageText.upper()
    d.text((2, 0),
           imageText,
           fill=(10, 255, 0),
           align="center"
           #,
           #font=ImageFont.truetype("./apis/text2image/Verdana.ttf", 16)
           )
    img.save(imageText + '.png')
    return 'done'


for letter1 in 'abcdefghijklmnopqrstwxyz':
    result = create_image(letter1)
    print(letter1 + ' --- ' + result)
    for letter2 in 'abcdefghijklmnopqrstwxyz':
        result = create_image(letter1 + letter2)
        print(letter1 + letter2 + ' --- ' + result)
