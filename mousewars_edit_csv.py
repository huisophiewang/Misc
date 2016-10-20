import os
import csv

DIR_READ = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Frames Cleanup")
DIR_WRITE = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Frames")
DIR = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Video Winning Cleanup Index")

files = os.listdir(DIR)
#for file in files:
    

s = ''
for file in files:
    if file == '.DS_Store':
        continue
    s = s +', ' + file[5:-13]
    
print s

#     fp_read = os.path.join(DIR_READ, file)
# 
# #     fp_write = os.path.join(DIR_WRITE, file)
#     
#     with open(fp_read, 'rU') as fr:
#         
#         
#         reader = csv.reader(fr)
#         
# #         with open(fp_write, 'wb') as fw:
# #             writer = csv.writer(fw, delimiter=',')
#     
#         for row in reader:
#             print type(row)
#             print row
#                 #writer.writerow(row[:])
            