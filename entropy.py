
import math


def entropy(a, b):
    p1 = a / float(a+b)
    p2 = b / float(a+b)   
    entropy = (-p1)*math.log(p1, 2) + (-p2)*math.log(p2, 2)
    return entropy

if __name__ == '__main__':
    print entropy(5, 9)
    #print math.log(4, 2)
    
    print entropy(3,4) * 1/2 + entropy(1,6) * 1/2
    
    print 6.0/14.0*math.log(4.0/3.0, 2) + 1.0/14.0*math.log(2.0/5.0, 2) + 3.0/14.0*math.log(2.0/3.0, 2) + 4.0/14.0*math.log(8.0/5.0, 2)