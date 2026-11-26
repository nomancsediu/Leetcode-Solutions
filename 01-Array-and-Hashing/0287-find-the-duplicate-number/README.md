# 287. Find the Duplicate Number

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Floyd's Tortoise and Hare (Cycle Detection) |
| **LeetCode** | [Open problem](https://leetcode.com/problems/find-the-duplicate-number/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only **one repeated number** in `nums`, return this repeated number.

You must solve the problem **without** modifying the array `nums` and using only constant extra space.

 

**Example 1:**

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:**

```
Input: nums = [3,3,3,3,3]
Output: 3
```

 

**Constraints:**

	- `1 <= n <= 10^5`

	- `nums.length == n + 1`

	- `1 <= nums[i] <= n`

	- All the integers in `nums` appear only **once** except for **precisely one integer** which appears **two or more** times.

 

**Follow up:**

	- How can we prove that at least one duplicate number must exist in `nums`?

	- Can you solve the problem in linear runtime complexity?

---

## Brute Force

Check each pair of elements using a hash set or nested loops; O(n^2) time or O(n) extra space.

## Intuition

Treat the array values as pointers to the next index, forming a linked list that must contain a cycle because there are n+1 nodes pointing into n positions. **Floyd's cycle detection** will meet inside the cycle, and a second phase finds the entry, which is the duplicate.

## Optimal Approach

Use **Floyd's Tortoise and Hare** algorithm to detect the cycle without modifying the array and with O(1) extra space.

## Step-by-Step Algorithm

1. Initialize two pointers: **slow** at nums[0] and **fast** at nums[nums[0]]; move **slow** one step and **fast** two steps until they meet.
2. Reset **slow** to nums[0] while keeping **fast** at the meeting point; move both one step at a time until they meet again.
3. The index where they meet is the duplicate value; return it.
4. (Optional) No need for extra passes; the algorithm finishes in linear time.

## Dry Run

- nums = [1,3,4,2,2]
- slow=1, fast=4 → move: slow=3, fast=2
- slow=4, fast=4 → meet
- reset slow=1, fast=4
- slow=1→3, fast=4→2
- slow=3→4, fast=2→2 → meet at 2, return 2

---

## Code

```python
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find intersection point of two runners.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Phase 2: Find entrance to the cycle.
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each pointer traverses at most O(n) steps before meeting. |
| **Space** | `O(1)` | Only a few integer variables are used regardless of input size. |

## Edge Cases

- All elements are the same (e.g., [3,3,3,3,3])
- Duplicate appears at the first position
- Very large n near 10^5

---

## Interview Tips

- Explain why a cycle must exist using the pigeonhole principle.
- State that we cannot modify the array nor use extra storage, which rules out sorting or hash sets.
- Walk through the two‑phase Floyd algorithm clearly, emphasizing O(1) space.
- Mention that the algorithm works for any duplicate count ≥2, not just exactly two occurrences.

## Follow-up Questions

- Can you adapt the solution to return all duplicate numbers if more than one exists?
- What if the numbers are not limited to 1..n?
- How would you handle the case where you are allowed to modify the array?

## Key Takeaways

- **Floyd's Tortoise and Hare** can detect cycles in structures represented by arrays.
- The **pigeonhole principle** guarantees a duplicate when length > range.
- Constant‑space pointer techniques are useful when modification is prohibited.

## Related Problems

- Find the Duplicate Number (LeetCode 287)
- Find the Missing Number
- Find All Duplicates in an Array

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
