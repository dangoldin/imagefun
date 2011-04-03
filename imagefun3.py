from PIL import Image, ImageFilter
import random, math

def get_neighbors(x,y):
    #yield (x,y) # Center
    yield (x+1,y) # Left
    yield (x-1,y) # Right
    yield (x,y+1) # Above
    yield (x,y-1) # Below
    yield (x+1,y+1) # Above and to the right
    yield (x+1,y-1) # Below and to the right
    yield (x-1,y+1) # Above and to the left
    yield (x-1,y-1) # Below and to the left

ifilename = 'picasso_bull.jpg'
#ifilename = 'very-cute-puppy.jpg'
ofilename = 'pb2.jpg'
ofilename2 = 'pb3.jpg'

img = Image.open(ifilename)
img = img.convert("RGBA")

img2 = img.filter(ImageFilter.CONTOUR)

pixdata = img2.load()

def distance_from_middle(x,y,z):
    return math.sqrt( math.pow(255/2.0 - x,2) + math.pow(255/2.0 - y,2) + math.pow(255/2.0 - z,2) )

def flatten(pixdata):
    for x in xrange(1,img.size[0]-1):
        for y in xrange(1,img.size[1]-1):
            p = pixdata[x,y]
            cnt = 0
            for i,j in get_neighbors(x,y):
                if distance_from_middle(pixdata[i,j][0],pixdata[i,j][1],pixdata[i,j][2]) < 255/2.0:
                    cnt += 1
            if cnt > 2:
                pixdata[x,y] = (100,0,0,255)

    for x in xrange(1,img.size[0]-1):
        for y in xrange(1,img.size[1]-1):
            p = pixdata[x,y]
            if p[0] == 100:
                pixdata[x,y] = (0,0,0,255)

for i in range(3):
    flatten(pixdata)

img2.save(ofilename2)

datas = img.getdata()
newData = list()

pixdata = img.load()
pixdata2 = img.load()

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        p = pixdata[x,y]
        if p[0] > 200 and p[1] > 200 and p[2] > 200:
            pixdata[x,y] = (255,255,255,255)
        else:
            pixdata[x,y] = (0,0,0,255)


for y in xrange(2,img.size[1]-2):
    for x in xrange(2,img.size[0]-2):
        p = pixdata[x,y]
        tp = pixdata[x,y-1]
        tp2 = pixdata[x,y-2]
        dp = pixdata[x,y+1]
        dp2 = pixdata[x,y+1]
        if p[0] == 0:
            if tp[0] == 0 and tp[2] == 0:
                pixdata[x,y] = (100,0,0,255)
            if (tp[0] == 0 or tp[0] == 100) and tp[2] == 0:
                pixdata[x,y] = (100,0,0,255)
            if tp[0] == 100 and dp[0] == 255:
                pixdata[x,y] = (100,0,0,255)

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        p = pixdata[x,y]
        if p[0] == 100:
            pixdata[x,y] = (255,255,255,255)

img.save(ofilename)
