# 448. Find All Numbers Disappeared in an Array

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | In-place marking using index as hash |
| **LeetCode** | [Open problem](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

 

**Example 1:**

```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```
**Example 2:**

```
Input: nums = [1,1]
Output: [2]
```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 10^5`

	- `1 <= nums[i] <= n`

 

**Follow up:** Could you do it without extra space and in `O(n)` runtime? You may assume the returned list does not count as extra space.

---

## Brute Force

Use a hash set to record seen numbers and then iterate 1..n to collect missing ones; O(n) time and O(n) extra space.

## Intuition

Because each value is in [1,n], we can use the array itself as a presence map by marking the index corresponding to each value. **Negating** or **adding n** to the element at that index records that the number exists without extra storage.

## Optimal Approach

Traverse the array and for each number x, mark the element at index |x|-1 (e.g., make it negative). After marking, any index whose value remains positive indicates its (index+1) is missing. This uses **in‑place modification** and **constant extra space**.

## Step-by-Step Algorithm

1. Iterate over each element num in nums.
2. Compute idx = abs(num) - 1, the target index for marking.
3. If nums[idx] > 0, set nums[idx] = -nums[idx] to mark presence.
4. After the first pass, iterate i from 0 to n-1; if nums[i] > 0, add i+1 to the result list.
5. Return the result list.

## Dry Run

- Input: [4,3,2,7,8,2,3,1]
- Marking pass:
- num=4 -> idx=3 -> nums[3] becomes -7
- num=3 -> idx=2 -> nums[2] becomes -2
- num=2 -> idx=1 -> nums[1] becomes -3
- num=-7 -> idx=6 -> nums[6] becomes -3
- num=8 -> idx=7 -> nums[7] becomes -1
- num=2 -> idx=1 (already negative) -> no change
- num=3 -> idx=2 (already negative) -> no change
- num=-1 -> idx=0 -> nums[0] becomes -4
- Second pass, positive entries at indices 4 and 5 => missing numbers 5 and 6.
- Output: [5,6]

---

## Code

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # First pass: mark presence by negating the value at the corresponding index
        for num in nums:
            idx = abs(num) - 1  # target index for the value num
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        # Second pass: collect indices that remain positive
        result = []
        for i, val in enumerate(nums):
            if val > 0:
                result.append(i + 1)
        return result
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is visited a constant number of times. |
| **Space** | `O(1)` | Only the output list is extra; the algorithm modifies the input in place. |

## Edge Cases

- All numbers appear exactly once (output empty).
- All numbers are the same (e.g., [1,1,1]) -> missing 2..n.
- Single element array.

---

## Interview Tips

- Clarify that modifying the input array is allowed.
- Explain why using abs(num) is needed when the value may already be negative.
- Mention that the output list does not count toward extra space.

## Follow-up Questions

- How would you solve it if you cannot modify the input array?
- Can you extend the idea to find numbers that appear twice?

## Key Takeaways

- **In‑place indexing** can replace auxiliary hash structures when values are bounded.
- Marking with **sign change** is a common trick for presence detection.
- Always consider the constraints (value range) to design O(1) space solutions.

## Related Problems

- Find All Duplicates in an Array
- First Missing Positive
- Missing Number

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
