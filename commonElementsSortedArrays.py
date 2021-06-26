# find common elements In 3 sorted arrays
# Two Pointers Approach
def commonElementsSortedArrays(ar1,ar2,ar3):
    i=0
    j=0
    k=0
    while i<len(ar1) and j<len(ar2) and k<len(ar3):
        if ar1[i]==ar2[j] and ar2[j]==ar3[k]:
            print(ar1[i])
            i+=1
            j+=1
            k+=1
        elif ar1[i]<ar2[j]:
            i+=1
        elif ar2[j]<ar3[k]:
            j+=1
        else:
            k+=1
            
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
commonElementsSortedArrays(ar1,ar2,ar3)
