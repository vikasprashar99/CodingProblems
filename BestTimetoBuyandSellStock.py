import math
# code 

def BestTimetoBuyandSellStock():
    prices =[7,1,5,3,6,4]
    leastsofar=math.inf
    maxCurrentProfit=0
    maxProfit=0
    
    for i in range(len(prices)):
        if prices[i]<leastsofar:
            leastsofar=prices[i]
        
        maxCurrentProfit=prices[i]-leastsofar
        maxProfit=max(maxProfit,maxCurrentProfit)
