from scipy import interpolate
import numpy as np

aunames = ['AU1','AU1-2','AU2','AU2L','AU4','AU5','AU6',
           'AU6L','AU6R','AU7L','AU7R','AU9','AU10Open','AU10LOpen',
           'AU10ROpen','AU11L','AU11R','AU12','AU25-12','AU12L','AU12R',
           'AU13','AU14','AU14L','AU14R','AU15','AU16Open','AU17',
           'AU20','AU20L','AU20R','AU22','AU23','AU24','AU25',
           'AU26','AU27','AU38','AU39','AU43','AU7','AU12-6']

sb_aunames = ['au_1', 'au_102', 'au_2', 'au_2_left', 'au_4', 'au_5', 'au_6', 
              'au_6_left', 'au_6_right', 'au_7_left', 'au_7_right', 'au_9', 'au_10', 'au_10_left', 
              'au_10_right', 'au_11_left', 'au_11_right', 'au_12', 'au_100', 'au_12_left', 'au_12_right', 
              'au_13', 'au_14', 'au_14_left', 'au_14_right', 'au_15', 'au_16', 'au_17', 
              'au_20', 'au_20_left', 'au_20_right', 'au_22', 'au_23', 'au_24', 'au_25', 
              'au_26', 'au_27', 'au_38', 'au_39', 'au_43', 'au_7', 'au_101']

###################################
#
# model 
#
###################################

def transform(para):
    aup = [None]*6
    aup[0] = para[0]
    aup[1] = 0.2 + (0.67-0.2)*para[1]
    aup[2] = aup[1]*0.67*para[2]
    aup[3] = 0.33*aup[1] + 0.67 + (0.33-0.33*aup[1])*para[3]
    aup[4] = aup[2]*aup[0]*para[4]
    # in matlab code:
    aup[5] = 0.5*aup[0] - 0.5*aup[3]*aup[0] + (0.5*aup[0]-0.5*aup[3]*aup[0])*para[5] 
    # in email:
    #aup[5] = 0.5*aup[0] - 0.5*aup[3]*aup[0] + (0.25*aup[0]-0.25*aup[3]*aup[0])*para[5]
    
    return aup

def generate(aup):
    x = [0, aup[2], aup[1], aup[3], 1]
    y = [0, aup[4], aup[0], aup[5], 0]
    #print x
    #print y
    
    n = 11
    duration = 1.25
    out_x = np.linspace(0, duration, n)
    out_y = interpolate.pchip_interpolate(x, y, np.linspace(0, 1, n))
    
    out = [str(n)]
    for i in range(n):
        out.append(str(out_x[i]))
        out.append(str(round(out_y[i], 2)))
    
    return out
    

def model():
    emotions = ["Happy", "Surprise", "Fear", "Disgust", "Anger", "Sadness"]
    for emotion in emotions:

        print emotion
        fr = open(r'C:\Users\Sophie\Dynamics\model3\%s.csv' % emotion, 'rU')
        lines = fr.readlines()
        for i, line in enumerate(lines):
               
            if not line.endswith(',NaN\n'):
                au = sb_aunames[i]
                    
                para = line.split(',')
                for j, p in enumerate(para):
                    para[j] = float(para[j])
                    
                out = generate(transform(para))
                
                cmd = 'scene.command(\"send sbm char ChrOlivia viseme %s curve %s\")' % (au, ' '.join(out))
                print cmd



###################################
#
# model sustain
#
###################################

                
def transform_sustain(para):
    aup = [None]*7
    aup[0] = para[0]
    aup[6] = para[6] * 0.3
    aup[1] = 0.2 + (0.67-0.2)*para[1]
    
    tstart = aup[1] - aup[6] * 0.5
    tend = aup[1] + aup[6] * 0.5
    
    aup[2] = tstart*0.8*para[2]
    aup[3] = tend + (1-tend)*0.2 + (1-(tend + (1-tend)*0.2))*para[3]
    aup[4] = aup[2]*aup[0]*para[4]
    # in matlab code:
    aup[5] = 0.5*aup[0] - 0.5*aup[3]*aup[0] + (0.5*aup[0]-0.5*aup[3]*aup[0])*para[5] 
    # in email:
    #aup[5] = 0.5*aup[0] - 0.5*aup[3]*aup[0] + (0.25*aup[0]-0.25*aup[3]*aup[0])*para[5]
    
    return aup, tstart, tend



    
def generate_sustain((aup, tstart, tend)):
    x = [0, aup[2], tstart, tend, aup[3], 1]
    y = [0, aup[4], aup[0], aup[0], aup[5], 0]
    #print x
    #print y
    
    n = 21
    duration = 2
    out_x = np.linspace(0, duration, n)
    out_y = interpolate.pchip_interpolate(x, y, np.linspace(0, 1, n))
    
    out = [str(n)]
    for i in range(n):
        out.append(str(out_x[i]))
        out.append(str(round(out_y[i], 2)))
    
    return out
    
              
def model_sustain():
    emotions = ["exhausted", 'afraid', 'sympathetic', 'jealous', 'impatient', 'disinterested']
    for emotion in emotions:
        print '============================'
        print emotion
        fr = open(r'C:\Users\Sophie\Dynamics\model_sustain\%s.csv' % emotion, 'rU')
        lines = fr.readlines()
        for i, line in enumerate(lines):
    
            
            if not line.endswith(',NaN\n'):
                au = sb_aunames[i]
                #print au
    
                para = line.split(',')
                for j, p in enumerate(para):
                    para[j] = float(para[j])
                    
                #print transform_sustain(para)
                out = generate_sustain(transform_sustain(para))
                
                cmd = 'scene.command(\"send sbm char ChrOlivia viseme %s curve %s\")' % (au, ' '.join(out))
                print cmd
    
if __name__ == '__main__': 
    #transform(au13)
    #generate(transform(au12))

    # Happy, Surprise, Fear, Disgust, Anger, Sadness

    #model_sustain()
    
    model()
    
