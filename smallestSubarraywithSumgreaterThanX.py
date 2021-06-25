import math
def smallestSubarraywithSumgreaterThanX(a,s):
    window_start=0
    temp=0
    ans=math.inf
    for window_end in range(len(a)):
        temp+=a[window_end]
    
        while temp>s:
            ans=min(ans,window_end-window_start+1)
            x=a[window_start]
            temp-=x
            window_start+=1
    return ans
smallestSubarraywithSumgreaterThanX([1, 10, 5, 2, 7],9)
