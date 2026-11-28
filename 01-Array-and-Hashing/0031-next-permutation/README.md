# 31. Next Permutation

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Two Pointers (reverse scan) |
| **LeetCode** | [Open problem](https://leetcode.com/problems/next-permutation/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

	- For example, for `arr = [1, 2, 3]`, the following are all the permutations of `arr`: `[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

Examples:

	- The next permutation of `arr = [1, 2, 3]` is `[1, 3, 2]`.

	- The next permutation of `arr = [2, 3, 1]` is `[3, 1, 2]`.

	- The next permutation of `arr = [3, 2, 1]` is `[1, 2, 3]` because `[3, 2, 1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be **in place** and use only constant extra memory.

 

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

---

## Brute Force

Generate all permutations, sort them and pick the next one; O(n!·n) time and O(n!·n) space

## Intuition

The next lexicographic permutation can be built by **finding the first decreasing pair from the right**, swapping the smaller element with the just‑larger element to its right, and then **reversing the suffix** to obtain the smallest possible order. This works because the suffix is originally in non‑increasing order, so reversing yields the minimal arrangement greater than the original.

## Optimal Approach

Use **two‑pointer scanning from the end** to locate the pivot, then another pointer to find the rightmost successor, swap, and finally **reverse** the tail in‑place. All operations are O(n) with O(1) extra space.

## Step-by-Step Algorithm

1. Scan from the end to find the first index i such that nums[i] < nums[i+1]; if none exists, the whole array is non‑increasing.
2. If such i exists, scan again from the end to find the smallest index j > i with nums[j] > nums[i].
3. Swap nums[i] and nums[j].
4. Reverse the sub‑array nums[i+1:] to get the next smallest ordering.

## Dry Run

- Input [1,2,3]: find i=1 (2<3); find j=2 (3>2); swap → [1,3,2]; reverse suffix after i → suffix length 0, final [1,3,2].
- Input [3,2,1]: no i found; reverse whole array → [1,2,3].
- Input [1,1,5]: i=1 (1<5); j=2 (5>1); swap → [1,5,1]; reverse suffix after i (index2) → stays [1]; final [1,5,1].

---

## Code

```python
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """Modify nums in‑place to the next lexicographic permutation."""
        n = len(nums)
        # 1. find pivot i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            # 2. find rightmost successor j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. swap pivot and successor
            nums[i], nums[j] = nums[j], nums[i]
        # 4. reverse suffix i+1 .. end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each step scans the array at most twice and a reversal is linear. |
| **Space** | `O(1)` | All modifications are done in‑place with a few index variables. |

## Edge Cases

- Array length 1 (no change)
- All elements equal (remains same)
- Already highest permutation (reverse whole array)

---

## Interview Tips

- Explain the lexicographic ordering intuition before coding
- State that the suffix after the pivot is guaranteed to be non‑increasing
- Mention that reversing the suffix is equivalent to sorting it ascending because it was descending
- Clarify that only constant extra variables are used

## Follow-up Questions

- Can you modify the algorithm to return the k‑th next permutation?
- How would you handle very large arrays where in‑place reversal might be costly?
- What if the numbers can be negative or larger than 100?

## Key Takeaways

- **Pivot detection** from the right identifies where change is needed
- **Successor swap** ensures the next larger value
- **Reverse suffix** yields the minimal arrangement after the pivot

## Related Problems

- Permutations II
- Maximum Swap
- Find the Smallest K-Length Subarray With a Given Sum

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
