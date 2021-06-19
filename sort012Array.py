# Sort an array of 0s, 1s and 2s
# used 3 pointer where low=0 mid=1 and high=2

def sort012Array(a):
    low=0
    mid=0
    high=len(a)-1
    
    while mid<=high:
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]
            mid+=1
            high-=1

a=[0,2,1,2,0]
sort012Array(a)
