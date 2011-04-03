import sys
import Image

im = Image.open('very-cute-puppy.jpg')
print im.format, im.size, im.mode

# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
out.save('tmp.jpg', 'JPEG')

# split the image into individual bands
source = im.split()
R, G, B = 0, 1, 2
# select regions where red is less than 100
mask = source[R].point(lambda i: i < 150 and 255)
# process the green band
out = source[G].point(lambda i: i * 0.2)
# paste the processed band back, but only where red was 100
source[G].paste(out, None, mask)
# build a new multiband image
im = Image.merge(im.mode, source)
im.save('tmp2.jpg', 'JPEG')
