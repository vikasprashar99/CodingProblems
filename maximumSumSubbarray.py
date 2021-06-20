# find maximum contiguous subarray
# Kadane's Algo

def maximumSumSubbarray(a):   
    maxTillnow=0
    maxSum=0
    
    for i in range(len(a)):
        maxTillnow = max(a[i], maxTillnow + a[i])
        maxSum = max(maxSum,maxTillnow)
         
    return maxSum    


a=[-1,1,0,-2,4,6]
maximumSumSubbarray(a)
