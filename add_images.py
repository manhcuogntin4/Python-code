import sys
from PIL import Image
import random
import glob

IMAGES_FOLDER="test/"
images_folder=IMAGES_FOLDER

def readFileImages(strFolderName):
    image_list=[]
    st=strFolderName+"*.png"
    for f in glob.glob(st):
    	image_list.append(f)
    return image_list
image_list=readFileImages(images_folder)
#print image_list
images = map(Image.open, [i for i in image_list])
widths, heights = zip(*(i.size for i in images))

max_width = max(widths)
sum_height = sum(heights)

new_im = Image.new('RGB', (max_width, sum_height), color=(255,255,255,0))

y_offset = 0
y=0
x=0
f=open("coordinate.txt", "w")
images_coordinate=[]
for im in images:
	image_coordinate=[]
	x=random.randint(0,max_width-im.size[0])
	image_coordinate.append(x)
	image_coordinate.append(y)
	image_coordinate.append(im.size[0])
	image_coordinate.append(im.size[1])
	new_im.paste(im, (x,y_offset))
	y_offset += im.size[1]
	y=y+y_offset
	images_coordinate.append(image_coordinate)
	f.write(str(image_coordinate)+"\n")
new_im.save('test.png')
