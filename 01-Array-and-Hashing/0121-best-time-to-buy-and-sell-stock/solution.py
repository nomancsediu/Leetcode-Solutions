class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Edge case: empty or single element
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # update the lowest price seen so far
            if price < min_price:
                min_price = price
            else:
                # potential profit if we sell today
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
