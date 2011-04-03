from PIL import Image

ifilename = 'very-cute-puppy.jpg'
ofilename = 'very-cute-puppy2.jpg'

img = Image.open(ifilename)
img = img.convert("RGBA")
datas = img.getdata()
newData = list()

for item in datas:
    newData.append((255 - item[0], 255 - item[1], 255 - item[2], 0))

#for item in datas:
#  if item[0] >= 200 and item[1] >= 200 and item[2] <= 200:
#    newData.append((0, 0, 0, 0))
#  else:
#    newData.append(item)

img.putdata(newData)
img.save(ofilename)
