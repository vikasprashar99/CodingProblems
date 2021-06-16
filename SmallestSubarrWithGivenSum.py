# Smallest Subarray with given sum
import math
a=[2, 1, 5, 2, 3, 2]
s=7
window_start=0
temp=0
ans=math.inf

for window_end in range(len(a)):
    temp+=a[window_end]

    while temp>=s:
        ans=min(ans,window_end-window_start+1)
        x=a[window_start]
        temp-=x
        window_start+=1
    