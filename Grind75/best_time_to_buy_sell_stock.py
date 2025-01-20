from typing import List


class DayPrice:
    def __init__(self, day, price):
        self.day = day
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def __sub__(self, other):
        return self.price - other.price


def maxProfit(prices: List[int]) -> int:

    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit,current_profit)
        else:
            left = right

        right += 1
    return max_profit

print(maxProfit([2,4,1,3,3,0,5,6,4]))

