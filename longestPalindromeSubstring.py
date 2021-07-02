def longestPalindrome(self, s: str) -> str:
        dp =[[False for x in range(len(s))]for y in range(len(s))]
        ans=""
        count=0
        for gp in range(len(s)):
            for i, j in zip(range(len(s)), range(gp,len(s))):
                
                if gp==0:
                    dp[i][j]=True
                elif gp==1:
                    if s[i]==s[j]:
                        dp[i][j]=True
                        count+=1
                else:
                    if s[i]==s[j] and dp[i+1][j-1]==True:
                        dp[i][j]=True
                        count+=1
                if(dp[i][j]):
                    count=gp+1
                    if len(ans) < len(s[i:j+1]):
                        ans = s[i:j+1]
        return ans
