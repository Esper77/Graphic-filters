from PIL import Image
from random import randint

img = Image.open(input())


def kek():
    j = 0
    while j < img.width//2:
        i = 0
        while i < img.height:
            img.putpixel((img.width-1-j, i), img.getpixel((j, i)))
            i += 1
        j += 1


def mono():
    j = 0
    while j < img.width:
        i = 0
        while i < img.height:
            col = sum(img.getpixel((j, i)))//3
            img.putpixel((j, i), (col, col, col))
            i += 1
        j += 1


def poly():
    j = 0
    while j < img.width:
        i = 0
        while i < img.height:
            if sum(img.getpixel((j, i)))//3 < 151:
                img.putpixel((j, i), (255, 0, 255))
            else:
                img.putpixel((j, i), (0, 255, 0))
            i += 1
        j += 1


def glitch():
    j = 0
    while j < img.width:
        i = 0
        while i < img.height:
            glitch_num = randint(-75, 75)
            r, g, b = img.getpixel((j, i))
            if r + glitch_num > 255:
                r = 255-glitch_num
            if g + glitch_num > 255:
                g = 255-glitch_num
            if b + glitch_num > 255:
                b = 255-glitch_num
            img.putpixel((j, i), (r+glitch_num, g+glitch_num, b+glitch_num))
            i += 1
        j += 1


def glitch_color():
    j = 0
    while j < img.width:
        i = 0
        while i < img.height:
            glitch_num = randint(-75, 75)
            r, g, b = img.getpixel((j, i))
            r += glitch_num
            if r > 255:
                r = 255
            glitch_num = randint(-75, 75)
            g += glitch_num
            if g > 255:
                g = 255
            glitch_num = randint(-75, 75)
            b += glitch_num
            if b > 255:
                b = 255
            img.putpixel((j, i), (r+glitch_num, g+glitch_num, b+glitch_num))
            i += 1
        j += 1


def slicy():
    global img
    j = 0
    while j < img.width//10:
        line = img.crop((j * 10, 0, j * 10 + 10, img.height))
        rotated_line = line.transpose(Image.ROTATE_180)
        img.paste(rotated_line, (j * 10, 0, j * 10 + 10, img.height))
        j += 1
    img = img.transpose(Image.ROTATE_180)


def cascade():
    k = int(input())
    global img
    j = 0
    while j < img.width//k:
        i = 0
        while i < img.height//k:
            line = img.crop((k*j, k*i, img.height-k*j, img.width-k*i))
            rotated_line = line.transpose(Image.ROTATE_180)
            img.paste(rotated_line, (k*j, k*i, img.height-k*j, img.width-k*i))
            i += 1
        j += 1
    img = img.transpose(Image.ROTATE_180)


cascade()
img.show()
