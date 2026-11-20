# 1. Two Sum

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Map lookup |
| **LeetCode** | [Open problem](https://leetcode.com/problems/two-sum/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

 

**Example 1:**

**Input:** `nums = [2,7,11,15], target = 9`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `2 + 7 = 9`, which equals the target. Therefore, the indices `[0, 1]` are returned.

**Example 2:**

**Input:** `nums = [3,2,4], target = 6`

**Output:** `[1,2]`

**Explanation:**

The sum of `nums[1]` and `nums[2]` is `2 + 4 = 6`, which equals the target. Therefore, the indices `[1, 2]` are returned.

**Example 3:**

**Input:** `nums = [3,3], target = 6`

**Output:** `[0,1]`

**Explanation:**

The sum of `nums[0]` and `nums[1]` is `3 + 3 = 6`, which equals the target. Therefore, the indices `[0, 1]` are returned.

 

**Constraints:**

	- `2 <= nums.length <= 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- `-10^9 <= target <= 10^9`

	- **Only one valid answer exists.**

 

**Follow-up: **Can you come up with an algorithm that is less than `O(n^2)` time complexity?

---

## Brute Force

Check every pair of indices with two nested loops, which costs O(n^2) time.

## Intuition

By storing each number's index as we iterate, we can ask **in O(1) time** whether the complement (target‑num) has been seen before. Since exactly one solution exists, the first match is the answer.

## Optimal Approach

Use a **hash map** (dictionary) to map numbers to their indices while scanning the array once.

## Step-by-Step Algorithm

1. Initialize an empty dictionary `seen`.
2. Iterate over `nums` with index `i` and value `num`.
3. Compute `complement = target - num`.
4. If `complement` is in `seen`, return `[seen[complement], i]`.
5. Otherwise store `num` with its index `i` in `seen`.
6. If loop ends, raise an error (should not happen).

## Dry Run

- nums=[2,7,11,15], target=9
- i=0, num=2, complement=7 not in seen → seen={2:0}
- i=1, num=7, complement=2 in seen → return [0,1]

---

## Code

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # dictionary to store number -> its index
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # According to problem constraints this line is never reached
        raise ValueError("No two sum solution found")
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is processed once and dictionary look‑ups are O(1) on average. |
| **Space** | `O(n)` | In the worst case we store all n elements in the hash map. |

## Edge Cases

- Array with negative numbers
- Array containing duplicate values
- Minimum length array of size 2

---

## Interview Tips

- Clarify that exactly one solution exists and elements cannot be reused.
- Mention handling of duplicates by storing the first index and checking complement before insertion.
- Discuss time vs. space trade‑off and why O(n) is optimal for this problem.

## Follow-up Questions

- Can you solve it without extra space using sorting and two‑pointers?
- What if there were multiple valid pairs?
- How would you adapt the solution for a stream of numbers?

## Key Takeaways

- **Hash map** enables constant‑time complement look‑up.
- Store **index** while iterating to avoid a second pass.
- Always consider **complement** when dealing with sum problems.

## Related Problems

- Two Sum II - Input array is sorted
- 3Sum
- 4Sum

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
