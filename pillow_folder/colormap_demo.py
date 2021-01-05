# coding=utf-8
# from colormap import Color
#
#
# c = Color('blue')
# print(c.rgb)
# print(c.hex)
# print(c)


# from colormap import hex2rgb, rgb2hex
#
#
# print(rgb2hex(255, 0, 0))
# print(hex2rgb('#FF0000'))


# from colormap import hex2web, web2hex
#
#
# print(hex2web('#FFFFFF'))
# print(web2hex('#F10'))


# from colormap import Colormap
#
# c = Colormap()
# map = c.cmap_linear('blue', 'white', 'green')
# c.test_colormap(map)


# from colormap import Colormap
#
#
# c = Colormap()
# c.plot_colormap('sequentials')
# c.test_colormap(map)


# from colormap import cmap_builder, test_cmap
#
#
# mycm = cmap_builder('green', 'black', 'blue')
# test_cmap(mycm)


# from pylab import *
# from colormap.colors import Colormap
# c = Colormap()
# t = ['#FF0000FF', '#FF4D00FF', '#FF9900FF', '#FFE500FF',
#      '#CCFF00FF', '#80FF00FF', '#33FF00FF', '#00FF19FF',
#      '#00FF66FF', '#00FFB2FF', '#00FFFFFF', '#00B3FFFF',
#      '#0066FFFF', '#001AFFFF', '#3300FFFF', '#7F00FFFF',
#      '#CC00FFFF','#FF00E6FF','#FF0099FF', '#FF004DFF']
# c.plot_rgb_from_hex_list(t)


from colormap import Colormap


c = Colormap()
d = {'red':   [0, 1, 0, 0, 1, 1, 0, 1],
     'green': [0, 0, 1, 0, 1, 0, 1, 1],
     'blue':  [0, 0, 0, 1, 0, 1, 1, 1]}
map = c.cmap(d, reverse=True, N=100)
c.test_colormap(map)
