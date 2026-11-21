# 121. Best Time to Buy and Sell Stock

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | One Pass Minimum Tracking |
| **LeetCode** | [Open problem](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

 

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

 

**Constraints:**

	- `1 <= prices.length <= 10^5`

	- `0 <= prices[i] <= 10^4`

---

## Brute Force

Check every pair of buy‑sell days with two nested loops, O(n^2) time, O(1) space.

## Intuition

The best profit comes from the **largest future price** minus the **smallest price seen so far**; as we scan left‑to‑right we can keep the minimum price and compute profit on the fly.

## Optimal Approach

Maintain a running **minimum price** and update **max profit** in a single pass, which is a classic **greedy**/**one‑pass** technique.

## Step-by-Step Algorithm

1. Initialize min_price to +∞ and max_profit to 0.
2. Iterate over each price in the array.
3. Update min_price = min(min_price, current price).
4. Compute potential profit = current price - min_price and update max_profit = max(max_profit, potential profit).
5. After the loop, return max_profit.

## Dry Run

- prices=[7,1,5,3,6,4]
- min_price=∞,max_profit=0
- price=7 → min_price=7, profit=0, max_profit=0
- price=1 → min_price=1, profit=0, max_profit=0
- price=5 → profit=4, max_profit=4
- price=3 → profit=2, max_profit=4
- price=6 → profit=5, max_profit=5
- price=4 → profit=3, max_profit=5 → return 5

---

## Code

```python
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
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is visited exactly once. |
| **Space** | `O(1)` | Only a few scalar variables are used regardless of input size. |

## Edge Cases

- Single element array → profit 0
- All decreasing prices → profit 0
- All equal prices → profit 0
- Large input size up to 10^5

---

## Interview Tips

- Clarify that only one transaction is allowed and you must buy before you sell.
- Explain why a naive O(n^2) solution is too slow for n=10^5 and motivate a linear scan.
- Mention that keeping the minimum so far is sufficient because any better buy price would have been seen earlier.
- State the final answer is max(0, best profit) which the algorithm naturally yields.

## Follow-up Questions

- How would you modify the solution for unlimited transactions?
- What if you were allowed at most two transactions?
- Can you solve it using Kadane's algorithm on price differences?

## Key Takeaways

- **One‑pass min tracking** solves many "max difference with order" problems.
- **Greedy** works when the decision depends only on past information.
- Maintain **O(1) state** to achieve linear time.

## Related Problems

- Best Time to Buy and Sell Stock II
- Best Time to Buy and Sell Stock III
- Maximum Subarray
- Maximum Profit in Job Scheduling

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
