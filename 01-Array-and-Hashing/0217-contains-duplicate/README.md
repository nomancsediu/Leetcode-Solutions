# 217. Contains Duplicate

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Set lookup |
| **LeetCode** | [Open problem](https://leetcode.com/problems/contains-duplicate/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

---

## Brute Force

Check each pair of elements with two nested loops; O(n^2) time and O(1) extra space.

## Intuition

If any number appears twice, inserting elements into a **hash set** will reveal a duplicate the moment we try to add an already‑present value. The set gives constant‑time membership checks.

## Optimal Approach

Iterate through the array while maintaining a **hash set** of seen values; if a value is already in the set, return true, otherwise add it.

## Step-by-Step Algorithm

1. Create an empty **set** called seen.
2. For each number num in nums:
3.  If num is in seen, return true (duplicate found).
4.  Otherwise, add num to seen.
5. If the loop finishes, return false (all elements distinct).

## Dry Run

- nums = [1,2,3,1]
- seen = {}
- num=1 → not in seen → seen={1}
- num=2 → not in seen → seen={1,2}
- num=3 → not in seen → seen={1,2,3}
- num=1 → in seen → return true

---

## Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is processed once with O(1) average set operations. |
| **Space** | `O(n)` | In the worst case all n distinct elements are stored in the set. |

## Edge Cases

- Array of length 1 – always false.
- All elements identical – duplicate found at second element.
- Negative numbers and large values – hash set handles any hashable integer.

---

## Interview Tips

- Mention the trade‑off between time and extra space before coding.
- Clarify that Python's set provides average O(1) lookup/insertion.
- If asked for O(1) extra space, discuss sorting the array in‑place as an alternative.

## Follow-up Questions

- How would you solve it if you could not use extra space?
- Can you modify the solution to return the duplicate value(s) instead of a boolean?
- What if the array is read‑only and you can only use O(1) extra space?

## Key Takeaways

- **Hash set** is ideal for detecting duplicates in linear time.
- **Early exit** on first duplicate saves work.
- Understanding **space‑time trade‑offs** helps choose between hashing and sorting.

## Related Problems

- LeetCode 217: Contains Duplicate II
- LeetCode 442: Find All Duplicates in an Array
- LeetCode 287: Find the Duplicate Number

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
