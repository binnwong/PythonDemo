# coding=utf-8
# from PIL import Image


# class MyThread(threading.Thread):
#     def __init__(self, target, *args):
#         threading.Thread.__init__(self)
#         self.target = target
#         self.is_stop = False
#         self.args = args
#
#     def start(self):
#         while not self.is_stop:
#             self.target(self.args)
#
#     def stop(self):
#         self.is_stop = True


# coding=utf-8
# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# image.show()


# from PIL import Image
#
#
# image = Image.new('RGB', (160, 90), (0, 0, 255))
# image.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# print('width: ', image.width)
# print('height: ', image.height)
# print('size: ', image.size)
# print('mode: ', image.mode)
# print('format: ', image.format)
# print('category: ', image.category)
# print('readonly: ', image.readonly)
# print('info: ', image.info)


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# print(image.mode)
# image1 = image.convert('1')
# print(image1.mode)
# # image1.show()
# image_l = image.convert('L')
# print(image_l.mode)
# # image_l.show()
# image_p = image.convert('P')
# print(image_p.mode)
# # image_p.show()
# image_rgb = image.convert('RGB')
# print(image_rgb.mode)
# # image_rgb.show()
# image_cmyk = image.convert('CMYK')
# print(image_cmyk.mode)
# # image_cmyk.show()
# image_ycbcr = image.convert('YCbCr')
# print(image_ycbcr.mode)
# # image_ycbcr.show()
# # image_lab = image_ycbcr.convert('LAB')
# # print(image_lab.mode)
# # image_lab.show()
# image_hsv = image.convert('HSV')
# print(image_hsv.mode)
# # image_hsv.show()
# image_i = image.convert('I')
# print(image_i.mode)
# # image_i.show()
# image_f = image.convert('F')
# print(image_f.mode)
# # image_f.show()
# image2 = image_f.convert()
# print(image2.mode)
# # image2.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# image_rgb = image.convert('RGB')
# print(image_rgb.mode)
# image_l = image_rgb.convert('L')
# # image_l.show()
# matrix = (0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6)
# image_l2 = image_rgb.convert('L', matrix=matrix)
# image_l2.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# image_p = image.convert('P')
# # image_l.show()
# image_p2 = image.convert('P', palette='ADAPTIVE', colors=256)
# image_p2.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# image_copy = image.copy()
# # image_copy.show()
# image_new = Image.new('RGB', (160, 90), (0, 0, 255))
# image_new2 = Image.new('L', (160, 90), '#646464')
# image_copy.paste(image_new, (100, 100, 260, 190), mask=image_new2)
# image_copy.save('duck.png')
# image_save = Image.open('duck.png')
# print(image_save.format, image_save.mode)
# image_copy.show()


from PIL import Image


image = Image.open("yazi.jpg")
image_crop = image.crop(box=(300, 300, 800, 700))
# image_crop.show()
print('before resize: ', image.size)
image_resize = image.resize((500, 400), resample=Image.LANCZOS, box=(100, 100, 1200, 800), reducing_gap=5.0)
print('after resize: ', image_resize.size)
image_resize.show()
