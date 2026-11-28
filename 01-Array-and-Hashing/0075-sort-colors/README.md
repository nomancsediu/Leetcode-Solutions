# 75. Sort Colors

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Dutch National Flag (Three-way partition) |
| **LeetCode** | [Open problem](https://leetcode.com/problems/sort-colors/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

**Example 1:**

**Input:** nums = [2,0,2,1,1,0]

**Output:** [0,0,1,1,2,2]

**Explanation:**

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

**Example 2:**

**Input:** nums = [2,0,1]

**Output:** [0,1,2]

**Explanation:**

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 300`

	- `nums[i]` is either 0, 1, or 2.

 

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?

---

## Brute Force

Count occurrences of 0,1,2 then overwrite the array; O(n) time but requires two passes and extra counting variables.

## Intuition

By maintaining three regions—<0, ==1, >2—we can place each element in its correct region with a single scan, swapping misplaced elements directly.

## Optimal Approach

Use **three pointers** (low, mid, high) to partition the array into three sections in one pass.

## Step-by-Step Algorithm

1. Initialize low=0, mid=0, high=n-1.
2. While mid <= high:
3. **If nums[mid] == 0**: swap nums[low] and nums[mid]; low++; mid++.
4. **If nums[mid] == 1**: just mid++.
5. **If nums[mid] == 2**: swap nums[mid] and nums[high]; high--.

## Dry Run

- Input [2,0,2,1,1,0], low=0,mid=0,high=5.
- mid=0, nums[mid]=2 → swap with nums[high]=0 → [0,0,2,1,1,2], high=4.
- mid=0, nums[mid]=0 → swap with nums[low]=0 → low=1,mid=1.
- mid=1, nums[mid]=0 → swap with nums[low]=0 → low=2,mid=2.
- mid=2, nums[mid]=2 → swap with nums[high]=1 → [0,0,1,1,2,2], high=3.
- mid=2, nums[mid]=1 → mid=3.
- mid=3, nums[mid]=1 → mid=4 (loop ends). Result [0,0,1,1,2,2].

---

## Code

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sort nums in-place using Dutch National Flag algorithm."""
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is examined at most once. |
| **Space** | `O(1)` | Only a few integer pointers are used. |

## Edge Cases

- Array of length 1
- All elements the same
- Already sorted array
- Reverse sorted array

---

## Interview Tips

- Explain why a single pass is possible with three pointers.
- Mention that swapping with high does not increment mid because the swapped element needs re‑evaluation.
- Clarify invariants: [0..low-1]=0, [low..mid-1]=1, [mid..high]=unknown, [high+1..n-1]=2.

## Follow-up Questions

- Can you adapt the algorithm for k colors?
- What if the array is read‑only? How would you output a sorted copy?
- How would you handle streaming input?

## Key Takeaways

- **Three‑way partition** solves problems with three distinct values.
- Maintain clear **invariants** for pointer regions.
- In‑place swaps give **O(1)** extra space.

## Related Problems

- LeetCode 75 Sort Colors
- LeetCode 215 Kth Largest Element in an Array
- LeetCode 347 Top K Frequent Elements
- LeetCode 88 Merge Sorted Array

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
