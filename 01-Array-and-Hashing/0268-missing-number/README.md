# 268. Missing Number

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Mathematical Sum (Gauss) / XOR |
| **LeetCode** | [Open problem](https://leetcode.com/problems/missing-number/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

 

**Example 1:**

**Input:** nums = [3,0,1]

**Output:** 2

**Explanation:**

`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

**Input:** nums = [9,6,4,2,3,5,7,0,1]

**Output:** 8

**Explanation:**

`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

 

 

 

 

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^4`

	- `0 <= nums[i] <= n`

	- All the numbers of `nums` are **unique**.

 

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

---

## Brute Force

Use a hash set to store all numbers and then scan 0..n to find the missing one; O(n) time and O(n) space.

## Intuition

The sum of the first n natural numbers is known (n·(n+1)/2). **Subtracting** the actual sum of the array leaves exactly the missing value, giving O(1) extra space.

## Optimal Approach

Compute the expected total with the **Gauss formula** and subtract the sum of the input; the difference is the missing number.

## Step-by-Step Algorithm

1. Let n be the length of nums.
2. Compute expected_sum = n * (n + 1) // 2.
3. Compute actual_sum = sum(nums).
4. Return expected_sum - actual_sum.

## Dry Run

- nums = [3,0,1]; n = 3
- expected_sum = 3*4/2 = 6
- actual_sum = 3+0+1 = 4
- missing = 6-4 = 2

---

## Code

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n is the length of the array; the full range is 0..n inclusive
        n = len(nums)
        # Expected sum of 0..n using Gauss formula
        expected_sum = n * (n + 1) // 2
        # Actual sum of the given numbers
        actual_sum = sum(nums)
        # The difference is the missing number
        return expected_sum - actual_sum
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | We traverse the array once to compute its sum. |
| **Space** | `O(1)` | Only a few integer variables are used regardless of input size. |

## Edge Cases

- Array missing the largest number n (e.g., [0,1,2])
- Array missing 0 (e.g., [1,2,3])
- Minimum length n=1 (e.g., [0] or [1])

---

## Interview Tips

- Mention the Gauss formula and why it works for a contiguous range.
- Explain that the numbers are distinct, so no double‑counting issues.
- If asked for O(1) space, show the sum method; alternatively, discuss the XOR method as another O(1) solution.

## Follow-up Questions

- Can you solve it using XOR instead of sum?
- What if the array could contain duplicates or be unsorted?
- How would you handle very large n where the sum might overflow?

## Key Takeaways

- **Gauss sum** is useful when the complete set is a consecutive range.
- **XOR** can also cancel out pairs to isolate a missing element.
- Always verify constraints (distinctness
- range) before choosing a technique.

## Related Problems

- LeetCode 268: Missing Number
- LeetCode 287: Find the Duplicate Number
- LeetCode 41: First Missing Positive
- LeetCode 645: Set Mismatch

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
