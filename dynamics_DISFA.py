import os
import matplotlib.pyplot as plt
import numpy as np

dir = "C:\Users\Sophie\DISFA\DISFA_Database\ActionUnit_Labels"

aus = ['au1', 'au2', 'au4', 'au5', 'au6', 'au9', 
       'au12', 'au15', 'au17', 'au20', 'au25', 'au26']

def plot_au(au_id, start, end):
    i = 1
    f, axarr = plt.subplots(27, sharex=True)
    
    for fd in os.listdir(dir):
        if fd.startswith("."):
            continue
        
        print '======='
        print fd
        
        fp = os.path.join(dir, fd, fd + '_au%s' % au_id + '.txt')

        lines = open(fp, 'rU').readlines()
        y = []
        for line in lines:
            y.append(float(line.split(',')[1]))
        
        x = range(1, end-start+1)
        #print len(y[start:cut])
        #x = range(1, cut+1)
#         plt.subplot(27, 1, i)
#         plt.plot(x, y[start:cut])
        axarr[i-1].plot(x, y[start:end])
        axarr[i-1].set_ylim([0,5])
        i += 1
    plt.show()
    
def generate_cmd(sub_id, start, end):
    for au in aus:
#         print '========'
#         print au
        
        n = (end - start)*20
        
        x = np.arange(0,end-start,0.05)
        y = []
        fp = os.path.join(dir, sub_id, "%s_%s.txt" % (sub_id, au))
        lines = open(fp, 'rU').readlines()
        for line in lines[20*start:20*end]:
            value = float(line.split(',')[1])/5.0
            y.append(value)
        
        points = []
        points.append(str(n))
        for i in range(n):
            points.append(str(x[i]))
            points.append(str(y[i]))
        
        cmd = 'scene.command(\"send sbm char ChrOlivia viseme au_%s curve %s\")' % (au[2:], ' '.join(points))
        print cmd
            
        
            
    
 
if __name__ == '__main__': 
    # happy
    #plot_au(12, 0, 760)
    
    # surprise
    #plot_au(1, 4000, 4845)
    #plot_au(2, 4000, 4845)
    
    # disgust
    #plot_au(9, 1420, 1880)
    
    #print ' '.join([1,2,3,4])
    
    # happy
    #generate_cmd('SN003', 3, 38)
    
    # disgust
    #generate_cmd('SN003', 71, 94)
    
    # surprise
    generate_cmd('SN003', 200, 242)
    
    
    
    
    