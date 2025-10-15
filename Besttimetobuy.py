def maxProfit(prices):
    n = len(prices)
    min_price = float('inf')
    max_profit = 0
    
    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
            
        else:
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
                
    return max_profit

if __name__ == "__main__":
    n1 = list(map(int, input().split()))
    print(maxProfit(n1))
