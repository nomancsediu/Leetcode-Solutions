# 136. Single Number

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Bitwise XOR |
| **LeetCode** | [Open problem](https://leetcode.com/problems/single-number/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given a **non-empty** array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

**Example 1:**

**Input:** nums = [2,2,1]

**Output:** 1

**Example 2:**

**Input:** nums = [4,1,2,1,2]

**Output:** 4

**Example 3:**

**Input:** nums = [1]

**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 3 * 10^4`

	- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

	- Each element in the array appears twice except for one element which appears only once.

---

## Brute Force

Use a hash map to count frequencies and return the element with count 1; O(n) time and O(n) space.

## Intuition

XOR has the property that a ^ a = 0 and a ^ 0 = a; therefore pairing identical numbers cancels them out, leaving only the unique number.

## Optimal Approach

Iterate once while maintaining a running **XOR** accumulator; the final accumulator holds the **single number**.

## Step-by-Step Algorithm

1. Initialize a variable result = 0.
2. For each num in nums, set result = result ^ num.
3. After the loop, result holds the element that appears once.
4. Return result.

## Dry Run

- nums = [4,1,2,1,2]
- result = 0 ^ 4 = 4
- result = 4 ^ 1 = 5
- result = 5 ^ 2 = 7
- result = 7 ^ 1 = 6
- result = 6 ^ 2 = 4
- Return 4

---

## Code

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR accumulator; cancels out numbers appearing twice
        result = 0
        for num in nums:
            result ^= num
        return result
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is processed exactly once. |
| **Space** | `O(1)` | Only a single integer variable is used regardless of input size. |

## Edge Cases

- Array length is 1.
- All numbers are negative.
- Large input size up to 3*10^4.

---

## Interview Tips

- Mention the XOR properties before coding.
- Explain why using a hash map violates the O(1) extra space requirement.
- Confirm that the input is non‑empty as per the problem statement.

## Follow-up Questions

- What if every element appears three times except one?
- Can you extend the solution to handle two unique numbers?

## Key Takeaways

- **XOR** cancels paired values.
- **Bitwise** operations can give O(1) space solutions.
- Use **accumulator pattern** for linear scans.

## Related Problems

- Single Number II
- Single Number III
- Missing Number
- Find the Duplicate Number

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
