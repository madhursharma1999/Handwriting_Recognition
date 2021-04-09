import math
import numpy as np
import matplotlib as mpl
import scipy.interpolate as interpolate
import cv2
    
def fun(img1_path,img2_path):
    
    def savefig(data,name,no,s):
        mpl.rcParams['savefig.pad_inches'] = 0
        ax = plt.axes([0,0,.5,.5], frameon=False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.autoscale(tight=True)
        y = np.array(data)
        x = np.array(range(0,len(y)))
        
        if(len(data)<=4):
            t, c, k = interpolate.splrep(x, y, s=0, k=len(data))
        else:
            t, c, k = interpolate.splrep(x, y, s=0, k=4)
        N = 1000
        xmin, xmax = x.min(), x.max()
        xx = np.linspace(xmin, xmax, N)
        spline = interpolate.BSpline(t, c, k, extrapolate=False)
        #plt.subplot( no)
        plt.plot(xx, spline(xx))
        plt.title(s)
        #plt.savefig(name,transparent=True)
        #plt.show()
    
    
    from matplotlib import pyplot as plt
    sx1=0;
    sy1=0
    chk=True

    img1 = cv2.imread(img1_path,0)
    (thresh, blackAndWhiteImage) = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

    list1=[]
    
    for i in range(0,len(blackAndWhiteImage),5):
        for j in range(0,len(blackAndWhiteImage[0]),5):
            if blackAndWhiteImage[i][j]==0:
                list1.append([i,j])
                if chk==True:
                    chk=False
                    sx1=j
                    sy1=i
    xl2=[]
    yl2=[]
    chk1=False
    
    for x in list1:
        xl2.append(math.sqrt(((sx1-x[1])**2)+((sy1-x[0])**2)))
         
        
    img1 = cv2.imread(img2_path,0)
    (thresh, blackAndWhiteImage) = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
    list2=[]
    i=0
    j=0

    sx2=0
    sy2=0
    chk2=True
    for i in range(0,len(blackAndWhiteImage),5):
        for j in range(0,len(blackAndWhiteImage[0]),5):
            if blackAndWhiteImage[i][j]==0:
                list2.append([i,j])
                if chk2==True:
                    chk2=False
                    sx2=j
                    sy2=i
    xl=[]
    yl=[]

    chk2=False
    for x in list2:
     
        xl.append(math.sqrt(((sx2-x[1])**2)+((sy2-x[0])**2)))
    
    
    
    import numpy as np
    from scipy.signal import argrelextrema

    #normalizing
    xl = xl/np.linalg.norm(xl)
    xl2 = xl2/np.linalg.norm(xl2)

    
    x = np.array(xl)
    y = np.array(range(0,len(xl)))
    maxm=(argrelextrema(x, np.greater,order=1))
    minm = (argrelextrema(x, np.less,order=1))
    
    

    x2 = np.array(xl2)
    y2 = np.array(range(0,len(xl2)))
    

    maxm2=(argrelextrema(x2, np.greater,order=1))
    minm2 = (argrelextrema(x2, np.less,order=1))
  
    maxm=maxm[0] #/ np.linalg.norm(maxm[0])
    maxm2=maxm2[0]# / np.linalg.norm(maxm2[0])
   # minm=minm[0] #/ np.linalg.norm(minm[0])
   # minm2=minm2[0]
    maym=(x[maxm])
   # miym=(x[minm])
    maym2=(x2[maxm2])
   # miym2=(x2[minm2])
    #print(np.max(maxm),np.min(maxm))
    #print(np.max(maym),np.min(maym))
    #print(np.max(maxm2),np.min(maxm2))
    #print(np.max(maym2),np.min(maym2))
    score=(np.var(maxm)+np.var(maym))-(np.var(maxm2)+np.var(maym2))
    print(score)

    if score>=-25 and score <= 25:
        print(" same ")
    else:
        print(" different ")
    print()

    
    savefig(xl,"z1.jpg",321,"image1")
    savefig(xl2,"f.jpg",325,"image2")
    #plt.text(0,60, sm)
    plt.show()
    

if __name__ == '__main__':


    fun(img1_path="w21.png", img2_path="w23.png")
    
