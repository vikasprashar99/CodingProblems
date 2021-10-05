# Find if there is any subarray with sum equal to 0
# code
a=[4,2,1,6]

def zeroSumSubarr(a):
    s=set()
    temp=0
    for i in range(len(a)):
        temp+=a[i]
        if temp in s or temp==0:
            return True
        else:
            s.add(temp)
    return False
zeroSumSubarr(a)
