# Longest Subarray/Substring with K distinct Characters
# sliding Window approach

s="araaci"
k=2

window_start=0
ans=0
hashMap={}

for window_end in range(len(s)):
    ch=s[window_end]
    if ch not in hashMap:
        hashMap[ch]=1
    else:
        hashMap[ch]+=1
    
    while len(hashMap)>k:
        temp=s[window_start]
        if hashMap[temp]>1:
            hashMap[temp]-=1
        else:
            del hashMap[temp]
        window_start+=1
    ans=max(ans,window_end-window_start+1)
    