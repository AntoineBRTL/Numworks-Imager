from PIL import Image

PIXEL_SHIFT = 9

image = Image.open('image.jpg')
new_image = image.resize((int(320 / PIXEL_SHIFT), int(240 / PIXEL_SHIFT)))

lst = list(new_image.getdata())

program = """import kandinsky
SCREEN_WIDTH = 320
SCREEN_HIEGHT = 240

PIXEL_SHIFT = """ + str(PIXEL_SHIFT) + """

colors = """ + str(lst) + """

i = 0
for y in range(int(SCREEN_HIEGHT / PIXEL_SHIFT)):
    for x in range(int(SCREEN_WIDTH / PIXEL_SHIFT)):
        i += 1
        kandinsky.fill_rect(int(x * PIXEL_SHIFT), int(y * PIXEL_SHIFT), PIXEL_SHIFT, PIXEL_SHIFT, kandinsky.color(colors[i % len(colors)][0], colors[i % len(colors)][1], colors[i % len(colors)][2]))"""

f = open("imager.py", "a")
f.write(program)
f.close()