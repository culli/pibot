import time
from datetime import datetime
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8()
display.begin()
 
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 9)
 
im = Image.new("1", (8, 8), "black")
draw = ImageDraw.Draw(im)
width, ignore = font.getsize("88 : 88 : 88")

def format_time():
    d = datetime.now()
    return "{:%H : %M : %S}".format(d)

message = format_time()
x = 8
while True:
    x = x - 1
    if x < -(width + 20):
        x = 8
        message = format_time()
    draw.rectangle((0, 0, 7, 7), outline=0, fill=0)
    draw.text((x, -1), message, 1, font=font)
    display.set_image(im)
    display.write_display()
    time.sleep(0.1)
