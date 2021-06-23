# Max Product Subarr
# we take max as well as the min product similar toh kadanes algo

nums=[6, -3, -10, 0, 2]
prevMin = prevMax = 1
maxProduct = nums[0]
for num in nums:
    temp=prevMin
    prevMin= min(num,num*prevMin,num*prevMax)
    prevMax=max(num,num*temp,num*prevMax)
    maxProduct = max(maxProduct,prevMax)
print(maxProduct)
