from datetime import datetime
from datetime import timedelta
from time import gmtime, strftime, localtime
import time

# current = strftime("%H:%M:%S", localtime())
# print current
# 
# current = time.mktime(localtime())
# print current

#print localtime()

# test = time.strptime('2015-01-05 14:43:00', '%Y-%m-%d %H:%M:%S')
# test = time.strptime("30 Nov 00", "%d %b %y")
# test = time.strptime("27MAR2013:00:02:43", "%d%b%Y:%H:%M:%S")
# print type(test)
# print test

# dt1 = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# dt2 = datetime.strptime("27MAR2013:00:02:43", "%d%b%Y:%H:%M:%S")
# print dt1 > dt2

# d1 = datetime.strptime("27MAR2013", "%d%b%Y")
# d2 = datetime.strptime("29MAR2013", "%d%b%Y")
# #print type(d2 - d1)
# print (d2-d1).days

t1 = datetime.strptime("27MAR2013:07:42:20", "%d%b%Y:%H:%M:%S")
t2 = datetime.strptime("27MAR2013:07:44:19", "%d%b%Y:%H:%M:%S")
print t2-t1
print type(t2-t1)

result = (t2-t1).seconds
print type(result)

r = timedelta(seconds=result)
print r
print type(r)

# t = dt.strftime("%H:%M:%S")
# print type(t)
 
# scheduled = time.mktime(test)
# print scheduled


# scheduled = '14:10:00'
# print current - scheduled
#datetime.now().time()
 
# delta = scheduled - current
# print type(delta)

# 
# print strftime("%Y-%m-%d %H:%M:%S", localtime(1364356963))
# print strftime("%Y-%m-%d %H:%M:%S", localtime(1364358144))
# 
# 
# print strftime("%Y-%m-%d %H:%M:%S", localtime(1364384540))
# print strftime("%Y-%m-%d %H:%M:%S", localtime(1364384555))


#print datetime.now().time()