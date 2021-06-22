# Find the triplet that sum to a given value
# Two pointers sorted array

a=[1,2,4,3,6]
k=10
a.sort()

def tripletSum(nums,targetsum):
    for x in range(len(nums)-1):
        i=x
        j=x+1
        k=len(nums)-1
        while j<k:
            s=nums[i]+nums[j]+nums[k]
            if s>targetsum:
                k-=1
            elif s<targetsum:
                j+=1
            else:
                return True
                j+=1
                k-=1
                
                
    return False
    
tripletSum(a,k)
