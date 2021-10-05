# Max Consecutive Ones III
# code
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


j=0
count=0
ans=0
for i in range(len(nums)):
    if nums[i]==0:
        count+=1
        
    while count>k:
        if nums[j]==0:
            count-=1
        j+=1
    
    ans=max(ans,i-j+1)
