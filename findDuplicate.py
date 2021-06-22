#  find duplicate in an array of N+1 Integers
# Time complexity n
  
  def findDuplicate(num):
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return nums[i]

findDuplicate([1,2,2,3,4])
