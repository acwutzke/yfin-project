#import datetime
#import numpy as np 


def line_func(a):
    #find position of maximum in list
    mpos=a.index(max(a))
    #if mpos is in the second half of the list:
    if mpos>len(a)/2:
        #loop from begining of list to max position
        for p in range(mpos):
            #calulate slope of line (Ymax - Yp)/(Xmax - Xp)
            m=(max(a)-a[p])/(mpos-p)
            #calculate b
            b=a[p]-p*m
            #check whether line runs under any values in the array
            #using m and b calculated above
            check=0
            for p in range(mpos):
                y=p*m+b
                #check whether line is below price, if so break
                if y<a[p]:
                    check=1
                    break
            #if the above loop runs to completion, solution found, break
            if check==0:
                break
        
    else:
        i=0
        for p in range(len(a)-mpos):
            i=i+1
            #calulate slope of line (Ymax - Yp)/(Xmax - Xp)
            m=(max(a)-a[-p-1])/(mpos-(len(a)-p-1))
            #calculate b
            b=a[-p-1]-(len(a)-p-1)*m
            #print(i,m,b,a[-i],mpos,(len(a)-p))
            #check whether line runs under any values in the array
            #using m and b calculated above
            check=0
            for p in range(len(a)-mpos):
                y=p*m+b
                #check whether line is below price, if so break
                if (y+0.01)<a[p]:
                    check=1
                    break
            #if the above loop runs to completion, solution found, break
            if check==0:
                break         
    
    #solution is found - export line to list and return line
    ln=[]
    for i in range(len(a)+5):
        y=i*m+b
        ln.append(y)
    return ln
    






		



