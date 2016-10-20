fp = r'C:\Users\Sophie\workspace\DataMining\data\decision_tree\house-votes-84.data.txt'
with open(fp, 'rU') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        items = line.split(',')
        n = items[1:]
        n.append(items[0])
        new_line = ','.join(n)
        print new_line