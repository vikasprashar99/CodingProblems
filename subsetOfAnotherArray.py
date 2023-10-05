# Array is the subset of another array

# code
a1= [10, 5, 2, 23, 19]
a2 = [2,5]
# Sort and merge Technique
def subsetArraySortandMerge(a1,a2):
    a1.sort()
    a2.sort()
    i=j=0
    
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            i += 1
        elif a1[i] == a2[j]:
            j += 1
            i += 1
        elif a1[i] > a2[j]:
            break
    if j==len(a2):
        print("true")
    else:
        print("false")
        
# using set tehcnique
def subsetArrayusingSet(a1,a2):
    s1=set()
    for i in range(len(a1)):
        if a1[i] not in s1:
            s1.add(a1[i])
    
    for i in range(len(a2)):
        if a2[i] not in s1:
            return False
    return True
subsetArrayusingSet(a1,a2)
subsetArraySortandMerge(a1,a2)

# ///////////////////
