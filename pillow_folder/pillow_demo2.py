# coding=utf-8
# from PIL import Image


# image = Image.open("yazi.jpg")
# data = (200, 300, 1100, 1200)
# image_trans = image.transform((500, 400), Image.NEAREST, data=data, resample=Image.NEAREST, fillcolor='blue')
# image_trans.show()
# data = (0, 1, 300, 1, 0, 400)
# image_trans = image.transform((500, 400), Image.AFFINE, data=data, resample=Image.NEAREST, fillcolor='blue')
# image_trans.show()
# data = (0, 1, 500, 1, 0, 400, 0, 0)
# image_trans = image.transform((500, 400), Image.PERSPECTIVE, data=data, resample=Image.NEAREST, fillcolor='blue')
# image_trans.show()
# data = (300, 200, 300, 500, 800, 800, 1100, 0)
# image_trans = image.transform((500, 400), Image.QUAD, data=data, resample=Image.NEAREST, fillcolor='blue')
# image_trans.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# print(image.mode)
# r, g, b, a = image.split()
# print(r.mode, r.size)
# print(g.mode, g.size)
# print(b.mode, b.size)
# print(a.mode, a.size)
# # r.show()
# # g.show()
# # b.show()
# # a.show()
#
# r = image.getchannel('R')
# print(r.mode, r.size)
# r.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# r, g, b, a = image.split()
# image_merge = Image.merge('RGB', (r, g, a))
# print(image_merge.mode, image_merge.size)
# image_merge.show()


# from PIL import Image, ImageFilter
#
#
# image = Image.open("yazi.jpg")
# # image_blur = image.filter(ImageFilter.BLUR)
# # image_blur.show()
# # image_contour = image.filter(ImageFilter.CONTOUR)
# # image_contour.show()
# # image_edge = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
# # image_edge.show()
# image_emboss = image.filter(ImageFilter.EMBOSS)
# image_emboss.show()


# from PIL import Image
#
#
# image = Image.open('yazi.jpg').crop((100, 100, 1300, 900))
# image2 = Image.open('yazi2.jpg').crop((100, 0, 1300, 800))
# image.save('duck1.png')
# image2.save('duck2.png')
# duck1 = Image.open('duck1.png')
# duck2 = Image.open('duck2.png')
# print(duck1.size, duck1.mode)
# print(duck2.size, duck2.mode)
# image_blend = Image.blend(duck1, duck2, 5)
# image_blend.show()


# from PIL import Image
#
#
# duck1 = Image.open('duck1.png')
# duck2 = Image.open('duck2.png')
# r, g, b, a = duck2.split()
# image_compo = Image.composite(duck1, duck2, r)
# image_compo.show()


# from PIL import Image
#
#
# duck1 = Image.open('duck1.png')
# print(duck1.size)
# image = duck1.rotate(15, center=(0, 0), expand=1, translate=(100, 100), fillcolor=(0, 0, 255))
# print(image.size)
# image.show()


# from PIL import Image
#
#
# image = Image.open("yazi.jpg")
# image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
# # image1.show()
# image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
# # image2.show()
# image3 = image.transpose(Image.ROTATE_180)
# # image3.show()
# image4 = image.transpose(Image.TRANSVERSE)
# image4.show()


from PIL import Image


image = Image.open("yazi.jpg")
image_effect = image.effect_spread(10)
image_effect.show()
