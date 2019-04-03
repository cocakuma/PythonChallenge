from PIL import Image

img = Image.open('oxygen.png')
print(img.width, img.height)

for x in range(0, img.height):
    for y in range(0, img.width, 7):
        pix = img.getpixel((y, x))
        if pix[0] == pix[1] and pix[1] == pix[2]:
            print(chr(pix[0]), end="")
    print("")
