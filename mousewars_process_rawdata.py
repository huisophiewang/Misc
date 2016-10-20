import os
import xlrd
import shutil
from pprint import pprint
import csv



CSV_PATH = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "Facet Winning Winners Frames Cleanup RW")
GAMEPRE_PATH = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "raw data", "GamePre_V2.xlsx")
QUALTRICS_PATH = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "raw data", "Qualtrics-2-3.csv")

output_file = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "winning_winners_RW.csv")
output_labels = []
output_dict = {}

au_labels = ['AU1', 'AU2', 'AU4', 'AU5', 'AU6', 'AU7', 'AU9', 'AU10', 'AU12', 'AU14', 
             'AU15', 'AU17', 'AU18', 'AU20', 'AU23', 'AU24', 'AU25', 'AU26', 'AU28', 'AU43']

player_ids = []
game_ids = []

au6_max = {}
au12_max = {}

all_au_max = {}
for au_label in au_labels:
    all_au_max[au_label] = {}

#################################################################################
# read AU max from facet data

files = os.listdir(CSV_PATH)
for file in files:

    if file == '.DS_Store':
        continue
    
    game_id = file[:3]
    game_ids.append(game_id)
    
    player_id = file[5:-26]
    player_ids.append(player_id)
    
    
    columns = {}
    
    fp_read = os.path.join(CSV_PATH, file)
    with open(fp_read, 'rU') as fr:
        reader = csv.reader(fr)
        reader.next()
        for row in reader:
            for j in range(26, 46):
                if not au_labels[j-26] in columns:
                    columns[au_labels[j-26]] = []
                    columns[au_labels[j-26]].append(float(row[j]))
                else: 
                    columns[au_labels[j-26]].append(float(row[j]))
                

    for au_label in au_labels:
        max_au = max(columns[au_label])
        if max_au > 0:
            all_au_max[au_label][player_id] = max_au
        else:
            all_au_max[au_label][player_id] = 0
        
#pprint(all_au_max)

#################################################################################
# read game data from GamePre_V2.xlsx


book_gamepre = xlrd.open_workbook(GAMEPRE_PATH)
sh = book_gamepre.sheet_by_name('PreData')


column_labels =  sh.row_values(0)

pa_index = []
pb_index = []
subset_labels = []

for i in range(len(column_labels)):
    if 'P_A' in column_labels[i]:
        pa_index.append(i)
        label = column_labels[i] 
        if label.startswith('P_A'):
            subset_labels.append(label[4:])
        elif label.endswith('P_A'):
            subset_labels.append(label[:-4])
        else:
            subset_labels.append(label.replace('_P_A_', '_'))
            
            
            
    if 'P_B' in column_labels[i]:
        pb_index.append(i)
        
    

output_labels.extend(['PlayerID', 'GameID', 'Friends'])     
output_labels.extend(subset_labels)  


for rx in range(1, sh.nrows):
    row = sh.row_values(rx)

      
    game_id = str(int(row[0]))

    
    if game_id in game_ids:

        
        pa = row[1]
        pb = row[2]
        winner = row[6]
        script_a = row[3]
        script_b = row[4]
        
#         if str(script_a).startswith('CC') or str(script_b).startswith('CC'):
#             print game_id + ' ' + str(script_a) + ' ' + str(script_b)
#         else:
#             print game_id + ' ' + str(script_a) + ' ' + str(script_b)
   
        ################################################
        # change switch pa and pb for loser
        if winner == 'P_A':
            player_id = pa.split('-')[0][11:]
        elif winner == 'P_B':
            player_id = pb.split('-')[0][11:]


        if pa[-1]=='F' and pb[-1]=='F':
            friends = 'Friends'
        else:
            friends = 'Strangers'
            
        
            
        output_dict[player_id] = [player_id, game_id, friends]

        ################################################
        # change switch pa_index and pb_index for loser
        if winner == 'P_A':
            for index in pa_index:
                output_dict[player_id].append(row[index])
        elif winner == 'P_B':
            for index in pb_index:
                output_dict[player_id].append(row[index])
        

 
#pprint(output_dict)

#################################################################################
# read player data from Qualtrics-2-3.csv

with open(QUALTRICS_PATH, 'rU') as fr:
    reader = csv.reader(fr)
        
    labels = reader.next()
       
    output_labels.extend(labels[1:35])
    output_labels.extend(labels[81:])
        
    for row in reader:
        if row[0] in player_ids:
            #print row
            output_dict[row[0]].extend(row[1:35])
            output_dict[row[0]].extend(row[81:])
  
  
  
  
  
for player_id in player_ids:
       
    for au_label in sorted(all_au_max, key=lambda k:int(k[2:])):        
        output_dict[player_id].append(all_au_max[au_label][player_id])
           
output_labels.extend(au + '_max' for au in au_labels)
#################################################################################
# output to csv file 
   
  
with open(output_file, 'wb') as fw:
    writer = csv.writer(fw, delimiter=',')
    writer.writerow(output_labels)
         
    for player_id in sorted(output_dict, key=lambda k:int(k)):
        #print output_dict[player_id]
        writer.writerow(output_dict[player_id])
