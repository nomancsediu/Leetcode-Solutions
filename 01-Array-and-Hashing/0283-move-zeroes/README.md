# 283. Move Zeroes

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Two Pointers |
| **LeetCode** | [Open problem](https://leetcode.com/problems/move-zeroes/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

 

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
**Example 2:**

```
Input: nums = [0]
Output: [0]
```

 

**Constraints:**

	- `1 <= nums.length <= 10^4`

	- `-2^31 <= nums[i] <= 2^31 - 1`

 

**Follow up:** Could you minimize the total number of operations done?

---

## Brute Force

Iterate through the array and for each zero shift all following elements one step to the left, then place zero at the end; this costs O(n^2) time.

## Intuition

The optimal solution works by keeping a **write pointer** that tracks where the next non‑zero element should go. Every time we see a non‑zero we copy it to the write position and advance the pointer, leaving zeros behind to be overwritten later. After the pass, all positions from the write pointer to the end are set to zero.

## Optimal Approach

Use the **two‑pointer** technique: one pointer scans the array (read), the other marks the position to write the next non‑zero (write). This achieves in‑place rearrangement with linear time.

## Step-by-Step Algorithm

1. Initialize **write = 0**.
2. Loop **read** from 0 to len(nums)-1: if nums[read] != 0, assign nums[write] = nums[read] and increment **write**.
3. After the loop, fill the rest of the array from **write** to end with 0s.
4. Return (the array is modified in place).

## Dry Run

- Start nums=[0,1,0,3,12], write=0
- read=0, nums[0]=0 → skip
- read=1, nums[1]=1 → nums[write]=1 (nums[0]=1), write=1
- read=2, nums[2]=0 → skip
- read=3, nums[3]=3 → nums[write]=3 (nums[1]=3), write=2
- read=4, nums[4]=12 → nums[write]=12 (nums[2]=12), write=3
- End loop, fill indices 3,4 with 0 → final [1,3,12,0,0]

---

## Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place."""
        write = 0
        # First pass: bring all non‑zero elements forward
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        # Second pass: fill the rest with zeros
        for i in range(write, len(nums)):
            nums[i] = 0
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is visited at most twice (once during scan, once during zero‑fill). |
| **Space** | `O(1)` | Only a couple of integer variables are used regardless of input size. |

## Edge Cases

- Array of all zeros
- Array with no zeros
- Single element array
- Negative numbers are allowed but irrelevant to logic

---

## Interview Tips

- Clarify that the operation must be in‑place and that the relative order of non‑zeros must stay the same.
- Explain the two‑pointer idea before coding and discuss why it minimizes writes.
- Mention that the algorithm performs at most n writes, which is optimal for this problem.

## Follow-up Questions

- Can you solve it using only one pass without a second fill loop?
- How would you adapt the solution if you needed to move all instances of a given value, not just zero?
- What if the array is read‑only and you must return a new array?

## Key Takeaways

- **Two‑pointer** scanning is ideal for in‑place rearrangement problems.
- Maintain a **write index** to compact desired elements.
- A final pass to fill the remainder often simplifies the logic.

## Related Problems

- Remove Element
- Sort Colors
- Relative Sort Array
- Move Zeroes II

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
