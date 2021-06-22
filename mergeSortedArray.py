# Merge Two Sorted Arrays
# Merge Sort Technique Used
# complexity(N)
a=[1, 3, 5, 7]
b=[0, 2, 6, 8, 9]
n=len(a)+len(b)

ans=[0]*n

i=0
j=0
k=0

while i<len(a) and j<len(b):
    if a[i]<b[j]:
        ans[k]=a[i]
        i+=1
        k+=1
    elif a[i]>b[j]:
        ans[k]=b[j]
        j+=1
        k+=1

while i<len(a):
    ans[k]=a[i]
    i+=1
    k+=1
while j<len(b):
    ans[k]=b[j]
    k+=1
    j+=1
    
