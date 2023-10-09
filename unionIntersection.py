

def unionOfArrays(a,b):
    s=set()
    for i in range(len(a)):
        s.add(a[i])
    
    for j in range(len(b)):
        s.add(b[j])
    
    print(len(s))
def intersectionArrays(a,b):
    s=set()
    for i in range(len(a)):
        s.add(a[i])
        
    for i in range(len(b)):
        if b[i] in s:
            print(b[i])
        
a=[1,2,3,4,5]
b=[1,2,3]
unionOfArrays(a,b)  
intersectionArrays(a,b)
# end
