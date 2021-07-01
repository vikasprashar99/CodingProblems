# Count of Plaindromic Substring
# Dynamic Programming Pepcoding
# first check first and last and then check 
#  whether inner one is true before

s = "aba"

dp =[[False for x in range(len(s))]for y in range(len(s))]

count=0
for gp in range(len(s)):
    for i, j in zip(range(len(s)), range(gp,len(s))):
        if gp==0:
            dp[i][j]=True
            count+=1
        elif gp==1:
            if s[i]==s[j]:
                dp[i][j]=True
                count+=1
        else:
            if s[i]==s[j] and dp[i+1][j-1]==True:
                dp[i][j]=True
                count+=1
        
        
