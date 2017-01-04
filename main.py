from __future__ import print_function
import sys
from PIL import Image

im = Image.open("ikisugi.png")
im_w, im_h = im.size
background = Image.new("RGBA", (11 * im_w, 11 * im_h), (255, 255, 255, 0))

def sierpinski(im, background, level, factor, metric):
    #metric determines the size of the whole image
    #factor determines the size of each mini-senpai
    bg_w, bg_h = background.size
    im = im.resize((int(im.size[0] * factor), int(im.size[1] * factor)))
    im_w, im_h = im.size
    wCenter, hCenter = bg_w // 2, bg_h // 2
    def sierpinski_iter(currentLevel, coordinate):
        wc, hc = coordinate
        if currentLevel == 1:
            i = background.copy()
            i.paste(im, (wc - im_w // 2, hc - im_h // 2, wc - im_w // 2 + im_w, hc - im_h // 2 + im_h))
            return i
        else:
            def findCoordinate(x):
                offset = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1 ,1), (-1, 0)]
                return (wc + offset[x][0] * metric[0] * (3 ** (currentLevel - 2)), hc + offset[x][1] * metric[1] * (3 ** (currentLevel - 2)))
            l = [sierpinski_iter(currentLevel - 1, findCoordinate(x)) for x in range(0,8)]
            #map(lambda x: x.show(), l)
            return reduce(Image.alpha_composite, l)
    return sierpinski_iter(level, (wCenter, hCenter))

img = sierpinski(im, background, 1, 1.3, im.size)
img.show()
img.save("output1.png")
img = sierpinski(im, background, 2, 1.3, im.size)
img.show()
img.save("output2.png")
img = sierpinski(im, background, 3, 1.3, im.size)
img.show()
img.save("output3.png")
img = sierpinski(im, background, 4, 1.3 / 3, (im.size[0] / 3, im.size[1] / 3))
img.show()
img.save("output4.png")
