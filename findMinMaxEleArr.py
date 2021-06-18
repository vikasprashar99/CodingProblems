
def findMinMaxEleArr(arr):
    minVal=arr[0]
    maxVal=0
    
    for i in range(len(arr)):
        if arr[i]>maxVal:
            maxVal=arr[i]
        if arr[i]<minVal:
            minVal=arr[i]

arr = [1000, 11, 445, 1, 330, 3000]
findMinMaxEleArr(arr)
