  # creating a min heap for largest element and max heap to find the smallest element
  
import heapq

def KthLargestElement(arr,k):
    heap=[]
    for i in range(len(arr)):
        heapq.heappush(heap,arr[i])
        if len(heap)>k:
            heapq.heappop(heap)
            
    return heapq.heappop(heap)

arr=[7,10,4,3,20,15]
k=1
KthLargestElement(arr,k) 


