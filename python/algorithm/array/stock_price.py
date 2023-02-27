def max_price(prices):
    max_profit = 0.0
    min_profit = float('inf')
    for price in prices:
        min_profit = min(min_profit, price)
        compare_profit = price - min_profit
        max_profit = max(max_profit, compare_profit)
    return max_profit

A = [ 100, 110, 100, 90, 85, 100]
print(max_price(A))
        