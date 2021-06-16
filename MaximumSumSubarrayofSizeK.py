# Maximum Sum Subarray of Size K 

a=[2, 1, 5, 1, 3, 2]
k=3

window_start=0
temp=0
ans=0

for window_end in range(len(a)):
    temp+=a[window_end]
    
    if window_end>k:
        x=a[window_start]
        temp-=x
        window_start+=1
    if window_end==k:
        ans=max(ans,temp)
    