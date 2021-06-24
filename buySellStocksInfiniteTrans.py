# Buy Sell stocks with infinite transactions
a=[1,2,3,0,10,5,15]

bd=0
sd=0
profit=0

for i in range(1,len(a)):
    if(a[i]>a[i-1]):
        sd+=1
    else:
        profit+=a[sd]-a[bd]
        sd=bd=i
            
profit+=a[sd]-a[bd]

