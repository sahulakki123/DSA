def maxProfit(prices):
    Profit=0
    buy=prices[0]
    for i in prices:
        if i<buy:
            buy=prices
        else:
            P=i-buy
            if P > Profit:
                Profit=P
    return Profit

print(maxProfit([1,2,6,4,8,9,]))
                

  