# coding=utf-8
# import random
# from PIL import Image, ImageDraw, ImageFont


# width, height, font_size, font_num = 300, 100, 48, 5
# bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# image = Image.new(mode='RGB', size=(width, height), color=bg_color)
# draw = ImageDraw.Draw(image, mode='RGB')
# font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", font_size)
# verify = str()
# for i in range(font_num):
#     x = random.randint(i*(width/font_num), (i+1)*(width/font_num)-font_size)
#     y = random.randint(0, height-font_size)
#     char = random.choice([chr(alpha) for alpha in range(65, 91)] + [str(num) for num in range(10)])
#     verify += char
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     draw.text((x, y), char, fill=color, font=font)
# print(verify)
# image.show()


import random
from PIL import Image, ImageDraw, ImageFont


def gen_verified_image():
    width, height, font_size, font_num = 400, 150, 48, 4
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    image = Image.new(mode='RGB', size=(width, height), color=bg_color)
    draw = ImageDraw.Draw(image, mode='RGB')
    font = ImageFont.truetype("C:\Windows\Fonts\Gadugi.ttf", font_size)
    verify = str()
    for i in range(font_num):
        x = random.randint(i * (width / font_num) + 10, (i + 1) * (width / font_num) - font_size - 10)
        y = random.randint(20, height - font_size - 20)
        char = random.choice([chr(a) for a in range(65, 91)] + [chr(b) for b in range(97, 123)] +
                             [str(num) for num in range(10)])
        verify += char
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text((x, y), char, fill=color, font=font)
    return image, verify


if __name__ == '__main__':
    image, verify = gen_verified_image()
    print(verify)
    image.show()

