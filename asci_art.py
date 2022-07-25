import sys
import math
from PIL import Image, ImageDraw, ImageFont


fnt = ImageFont.truetype("Monaco.ttf", 15)
factor = 0.4
charwidth = 10
charheight = 12
im = Image.open("_K3A1531.JPG")
width, height = im.size
print(width, height, height/width)
colors = []
stuff = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
stuff2 = list(stuff)
stufflen = len(stuff2)
interval = stufflen/256
im = im.resize((int(factor*width), int(factor*height*(charwidth/charheight))))
width,height = im.size
two = im.load()
outputimg =  Image.new('RGB',(charwidth * width * 2, charheight * height), color = (0,0,0))
owidth,oheight = outputimg.size
print(owidth, oheight, height/width)
draw = ImageDraw.Draw(outputimg)

text_file = open("output.txt","w")


def getChar(value):
    return stuff2[math.floor(value*interval)]

print (im.format,im.mode,"width=",width,"height=",height)

for i in range(height):
    for j in range(width):
        r,g,b = two[j,i]
        avg =  int((r+g+b)/3)
        two[j,i] = (avg,avg,avg)
        text_file.write(getChar(avg))
        draw.text((j*charwidth, i*charheight), getChar(avg), font =fnt, fill = (r,g,b))
    
    text_file.write('\n')

        #thing = im.getpixel((col,row))
        #colors.append(thing)
        #print(colors)

outputimg.save("output.png")







# width = 1200
# height = 600
# colors = [[]*width]


# for col in range(width):
#     for row in range(height):
#         thing = (1,2,3)
#         colors[col][row].append(thing)


# print (colors)





