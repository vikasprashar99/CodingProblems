# Problem Statement- Reverse An Array 
# Used Two pointers
# Complexity O(n/2)  n=len(arr)

def reverseAnArray(arr)
    i=0
    j=len(arr)-1
    
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

a=[4, 5, 1, 2]
reverseAnArray(a)
