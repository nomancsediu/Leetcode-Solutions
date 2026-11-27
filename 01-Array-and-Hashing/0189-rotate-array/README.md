# 189. Rotate Array

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Reverse (In‑place rotation) |
| **LeetCode** | [Open problem](https://leetcode.com/problems/rotate-array/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

 

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-2^31 <= nums[i] <= 2^31 - 1`

	- `0 <= k <= 10^5`

 

**Follow up:**

	- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.

	- Could you do it in-place with `O(1)` extra space?

---

## Brute Force

Create a new array of the same size and copy each element to its target index; O(n) time and O(n) extra space.

## Intuition

By **reversing** parts of the array we can reposition elements without extra storage: first reverse the whole array, then reverse the first k elements and finally reverse the rest, which restores the original order within each segment.

## Optimal Approach

Use the **array reversal** technique to achieve an in‑place rotation with **O(1)** extra space.

## Step-by-Step Algorithm

1. Compute k = k % n to handle k >= n.
2. Reverse the entire array in place.
3. Reverse the first k elements (indices 0 to k‑1).
4. Reverse the remaining n‑k elements (indices k to n‑1).

## Dry Run

- nums=[1,2,3,4,5,6,7], k=3 → k=3
- After full reverse: [7,6,5,4,3,2,1]
- Reverse first 3: [5,6,7,4,3,2,1]
- Reverse last 4: [5,6,7,1,2,3,4]

---

## Code

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """Rotate nums to the right by k steps in‑place.
        Modifies nums directly and returns None.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n  # effective rotations
        if k == 0:
            return
        # helper to reverse a sub‑array [l, r]
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        # step 1: reverse whole array
        reverse(0, n - 1)
        # step 2: reverse first k elements
        reverse(0, k - 1)
        # step 3: reverse remaining n‑k elements
        reverse(k, n - 1)
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is visited a constant number of times during the three reversals. |
| **Space** | `O(1)` | Reversal is done by swapping elements in place, using only a few temporary variables. |

## Edge Cases

- k = 0 (no rotation)
- k equal to array length (array unchanged)
- Array of length 1
- k larger than n (use modulo)

---

## Interview Tips

- Clarify constraints and ask if rotating in‑place is required.
- Explain why k may be reduced modulo n.
- Mention alternative solutions (extra array, cyclic replacements) and their trade‑offs.
- Walk through a small example to prove correctness.

## Follow-up Questions

- Can you implement the rotation using cyclic replacements?
- How would you rotate to the left instead of the right?
- What if the array is stored in a read‑only memory region?

## Key Takeaways

- **Reverse** trick converts rotation into simple sub‑array reversals.
- Modulo operation handles **large k** efficiently.
- In‑place algorithms often rely on **swap‑based** transformations.

## Related Problems

- LeetCode 189: Rotate Array
- LeetCode 31: Next Permutation
- LeetCode 215: Kth Largest Element in an Array
- LeetCode 283: Move Zeroes

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
