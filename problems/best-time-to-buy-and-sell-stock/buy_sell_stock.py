# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def buy_sell_stock(prices: list[int]) -> int:
    L = len(prices)
    min_price = prices[0]
    max_profit = 0

    for i in range(0, L):
        if prices[i] < min_price:
            min_price = prices[i]

        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit
