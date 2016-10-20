import os
import shutil

user = 'Margot'
date = '20150109'
fullname = '_'.join([user, date])
startframe = 506

desktop = r'/Users/sophiewang/Desktop'
f1 = open(os.path.join(desktop, 'images_tag.txt'), 'r')
f2 = open(os.path.join(desktop, fullname + '.txt'), 'r')

src = os.path.join(r'/Users/sophiewang/Documents/faceshift/performances', fullname)
dst = os.path.join(r'/Users/sophiewang/face', user)

tags = {}
for line in f1:
    items = line.split()
    tags[items[0]] = items[1]
 
count = 0
for line in f2:
    if 'display image' in line:
        
        items = line.split()
        image = items[2]
        tag = tags[image]
        print str(image) + ' ' + str(tag)
        
        number = image.split('.')[0]
        dstpath = os.path.join(dst, '_'.join([user, tag, number]))
        os.makedirs(dstpath)
        for j in range(144):
            number = startframe + 144*count + j
            filename = '.'.join([fullname, str(number).rjust(4, '0'), 'jpg'])
            #print filename
            filepath = os.path.join(src, filename)
            shutil.copy2(filepath, dstpath)
            
        count += 1

# print count
# from pprint import pprint
# pprint(sorted(save, key= lambda pair:pair[1], reverse=True))