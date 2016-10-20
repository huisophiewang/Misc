
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}




# sort key into list by value
#print sorted(d, key=d.get)

#print d.sorted()

#return a list of tuples (key, value)
d = sorted(d.items(), key=lambda x: len(x[0]))
# 
# for i, pair in enumerate(d):
#     if i>0:
#         print d[i-1]

test = []
test[0] = 't'
print test