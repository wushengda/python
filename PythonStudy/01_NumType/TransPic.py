from PIL import Image

ascii_char = list("/\|()1{}$@B%8&WM#ZO0QLCJUYX*hkbdpqwmoahkbdpqwmzcvunxrjft[]?-_+~<>i!lI;:,\"^`'. ")
imgname = "./touxiang.png"
output = "./a.txt"
# width = 4000
# height = 2000
width = 400
height = 200

def get_char(r, g, b, alpha=256):
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unitcount = (256.0 + 1) / length
    return ascii_char[int(gray / unitcount)]


img = Image.open(imgname)
img = img.resize((width, height), Image.NEAREST)

txt = ""

for i in range(height):
    for j in range(width):
        txt += get_char(*img.getpixel((j, i)))
    txt += '\n'

with open(output, 'w') as f:
    f.write(txt)
