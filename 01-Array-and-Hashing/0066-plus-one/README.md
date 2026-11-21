# 66. Plus One

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Simple iteration with carry |
| **LeetCode** | [Open problem](https://leetcode.com/problems/plus-one/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the resulting array of digits.

 

**Example 1:**

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

 

**Constraints:**

	- `1 <= digits.length <= 100`

	- `0 <= digits[i] <= 9`

	- `digits` does not contain any leading `0`'s.

---

## Brute Force

Convert the array to an integer, add one, then split back into digits; this uses O(n) extra space and may overflow for very large numbers.

## Intuition

We simulate the manual addition of one starting from the least‑significant digit. **If a digit becomes 10 we set it to 0 and carry 1** to the next position; otherwise we stop because no further changes are needed.

## Optimal Approach

Use **in‑place traversal from right to left** while handling the **carry**. No extra data structures are required beyond a few variables.

## Step-by-Step Algorithm

1. Initialize carry = 1 (the +1 we need to add).
2. Iterate i from the last index down to 0: compute sum = digits[i] + carry.
3. Set digits[i] = sum % 10 and update carry = sum // 10.
4. If after the loop carry is still 1, insert 1 at the front of the list.
5. Return the modified digits array.

## Dry Run

- Input [1,2,9]: start carry=1; i=2 -> sum=9+1=10 -> digits[2]=0, carry=1; i=1 -> sum=2+1=3 -> digits[1]=3, carry=0; stop loop; result [1,3,0].
- Input [9,9]: i=1 -> sum=9+1=10 -> digits[1]=0, carry=1; i=0 -> sum=9+1=10 -> digits[0]=0, carry=1; loop ends, carry=1 so prepend 1 -> [1,0,0].

---

## Code

```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # start with a carry of 1 because we need to add one
        carry = 1
        n = len(digits)
        # process digits from least significant to most significant
        for i in range(n - 1, -1, -1):
            if carry == 0:
                break
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
        # if we still have a carry, insert it at the front
        if carry:
            digits.insert(0, carry)
        return digits
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each digit is visited at most once. |
| **Space** | `O(1)` | We modify the input list in place and use only a constant number of extra variables. |

## Edge Cases

- All digits are 9 (e.g., [9,9,9])
- Single element array
- Number without trailing 9s (e.g., [1,2,3])

---

## Interview Tips

- Clarify that the input represents a non‑negative integer with no leading zeros.
- Mention overflow concerns if you tried to convert to an int, which is why you work digit‑by‑digit.
- Explain the carry concept and why you can stop early when carry becomes 0.

## Follow-up Questions

- Can you do it without modifying the input array?
- What if the digits are stored in a linked list?
- How would you handle a very large input where the array length is up to 10^5?

## Key Takeaways

- **Carry propagation** is a common technique for digit‑wise arithmetic.
- In‑place right‑to‑left traversal avoids extra space.
- Stopping early when carry is zero saves time.

## Related Problems

- Add Two Numbers
- Multiply Strings
- Reverse Integer

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
