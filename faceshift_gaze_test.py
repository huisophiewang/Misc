fp = '/Users/sophiewang/Documents/faceshift/performances/SophieGazeTest/gaze_test.txt'


print 'timestamp leftEyePitch leftEyeYaw rightEyePitch rightEyeYaw'
with open(fp, 'rU') as fr:
    for line in fr:
        #print '-------'
        item = line.split('M')[0]
        #print len(items)
        #print items[0]
        time = float(item.split()[3]) / 1000
        
        eye_info = item.split('E')[1].strip()
        print "%.3f " % time + eye_info
