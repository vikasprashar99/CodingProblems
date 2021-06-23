# Longest Consecutive Sequence
# used hash with num boolean pairs

nums=[0,3,7,2,5,8,4,6,0,1]

def longestconsecutive(nums):
    d=dict()    
    mcount=0
    for i in nums:
        d[i]=True
    for i in nums:
        if i-1 in d:
            d[i]=False
    
    for i in nums:
        if d[i]==True:
            t=1
            val=i
            count=0
            while val+t in d:
                count+=1
                t+=1
            mcount=max(mcount,count)
        
    return(mcount+1)
longestconsecutive(nums)
