# Move all negative numbers to beginning and positive to end 
# Two pointers - basic
def moveallnegativenumbers(a):   
    j=0
    for i in range(0,len(a)):
        if a[i]<0:
            a[i],a[j]=a[j],a[i]
            j+=1
        


a=[-1,1,0,-2,4,6]
moveallnegativenumbers(a)
