import os
import xlrd
import shutil
from pprint import pprint
import csv






XLSX_PATH = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "raw data", "GamePre_V2.xlsx")

DST = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Winning W")

root = os.path.join("/Users", "sophiewang", "data sets", "Mousewars")
path1 = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Video Winning All")
path2 = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Video Winning Losers")


game_ids = []
for file in os.listdir(path1):
    if not '.avi' in file:
        continue
    game_id = file[:3]
    if not game_id in game_ids:
        game_ids.append(game_id)
    
#print game_ids

book = xlrd.open_workbook(XLSX_PATH)
sh = book.sheet_by_index(0)

results = {}
ids = []
i = 0
for rx in range(1, sh.nrows):
    row = sh.row_values(rx)
      
    game_id = str(int(row[0]))
    p1 = row[1]
    p2 = row[2]
    p1_joy = row[64]
    p2_joy = row[65]
    winner = row[6]
    
    
    #if game_id in game_ids and p1[-1]=='F' and p2[-1]=='F':
    if game_id in game_ids:
        pass
#         player_id = ''
#         joy = -1
#         if winner == 'P_A':
#             player_id = p1.split('-')[0][11:]
#             joy = p1_joy
#         elif winner == 'P_B':
#             player_id = p2.split('-')[0][11:]
#             joy = p2_joy
#         #print player_id
#         #print ','.join([game_id, player_id, str(joy)])
#         if p1[-1]=='F' and p2[-1]=='F':
#             pair = 'F'
#         else:
#             pair = 'S'
#         results[player_id] = [player_id, game_id, pair, str(joy)]
#         ids.append(player_id)
#         i += 1






        
#         if row[6] == 'P_A':
#             player_id = row[2].split('-')[0][11:]
#             if row[2][-1] == 'C':
# 
#                 print game_id + ' ' + player_id
#         elif row[6] == 'P_B':
#             player_id = row[1].split('-')[0][11:]
#             if row[1][-1] == 'C':
#                 print game_id + ' ' + player_id        

                
#         file_name = game_id + '_P' + player_id + 'Winning' + '.avi'
#         src_file = os.path.join(path1, file_name)
#         if os.path.isfile(src_file):
#             print src_file
            #shutil.copy2(src_file, path2)

# cleanup = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Frames Cleanup")
# files = os.listdir(cleanup)
# for file in files:
#     print file[:3]


# DIR = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Video Winning Losers Index")
#  
# i = 1
# for file in os.listdir(DIR):
#      
#     if not '.avi' in file:
#         continue
#     items = file.split('.')
#     new_name = items[0] + str(i).zfill(2) + '.avi'
#     i += 1
#     print new_name
#     os.rename(os.path.join(DIR, file), os.path.join(DIR, new_name))

# DIR = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Video Winning Losers")
# path = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Losers Frames Cleanup")
# csvs = []
# for file in os.listdir(path):
#     if not '.csv' in file:
#         continue
#     csvs.append(file[:3])
# print csvs
# 
# 
# for file in os.listdir(DIR):
#       
#     if not '.avi' in file:
#         continue
#     if not file[:3] in csvs:
#         print file
#         os.remove(os.path.join(DIR, file))


dir1 = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Winners Frames Cleanup CCW")
files1 = os.listdir(dir1)

dir2 = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Winners Frames Cleanup RW")
files2 = os.listdir(dir2)

for file in files1:
    if file in files2:
        print file


