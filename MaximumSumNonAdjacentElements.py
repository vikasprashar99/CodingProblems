# Maximum Sum Non Adjacent Elements DP
a=[2,0,0,2]
inclu=a[0]
exclu=0
ans=0
for i in range(1,len(a)):
    ninclu=exclu+a[i]
    nexclu=max(exclu,inclu)
    
    inclu=ninclu
    exclu=nexclu
    
    ans=max(inclu,exclu)