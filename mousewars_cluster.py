import os
from pprint import pprint

file1 = os.path.join("/Users", "sophiewang", "data sets", "Mousewars", "au_above1.txt")

player_ids = [16, 18, 22, 27, 31, 36, 56, 60, 61, 64, 73, 77, 84, 85, 89, 92, 93, 97, 101, 105, 
              108, 109, 112, 117, 128, 132, 133, 137, 140, 141, 145, 148, 153, 156, 157, 160, 
              161, 164, 165, 172, 176, 181, 185, 189, 192, 193, 196, 197, 201, 204]



aus = {}

with open(file1, 'rU') as f1:
    lines = f1.readlines()
    for line in lines:
        line = line.strip('\n')
        items = line.split(':')

        if not items[2]:
            continue
        subjects = items[2].split(',')

        for subject in subjects:
            
            subject = str(player_ids[int(subject)-1])
            if not subject:
                continue
            if subject in aus:
                aus[subject].append(items[0])
            else:
                aus[subject] = []
                aus[subject].append(items[0])
                



pprint(aus) 

s = ''
for i in range(50):
    id = i+1
    if not str(id) in aus.keys():
        s = s + str(id) + ', '
print s
# 
# print '------'
# 
# print str(len(aus.keys())) + ' subjects'   
# 
#              
# for k in sorted(aus, key=lambda k:len(aus[k])):
#     print '%2s' % k + ' ' + str(aus[k])

results = {}
for k in aus:
    h = str(aus[k])
    if h in results:
        results[h].append(int(k))
    else:
        results[h] = []
        results[h].append(int(k))
        
#pprint(results)
for k in sorted(results, key=lambda k:len(k)):
    print  k + ': ' + str(results[k])[1:-1]
    
# test = []
# test.append({'name':'Hui', 'age':8})
# test.append({'name':'Sophie', 'age':18})
# test.append({'name':'Lucy', 'age':4})
# print sorted(test, key=lambda k:k['age'])
    
