# 560. Subarray Sum Equals K

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Prefix Sum with Hash Map |
| **LeetCode** | [Open problem](https://leetcode.com/problems/subarray-sum-equals-k/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

 

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
```
**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
```

 

**Constraints:**

	- `1 <= nums.length <= 2 * 10^4`

	- `-1000 <= nums[i] <= 1000`

	- `-10^7 <= k <= 10^7`

---

## Brute Force

Check every possible subarray by nested loops and compute its sum, which takes O(n^2) time.

## Intuition

The sum of a subarray [i..j] equals k iff prefixSum[j]‑prefixSum[i‑1]=k. By storing how many times each prefix sum has occurred, we can instantly know how many earlier positions give the needed complement **prefixSum - k**. This turns a quadratic scan into a linear pass.

## Optimal Approach

We maintain a **hash map** that maps each encountered prefix sum to its frequency while iterating once through the array, applying the **prefix‑sum** technique.

## Step-by-Step Algorithm

1. Initialize a hash map with {0:1} to represent an empty prefix and set prefix=0, count=0.
2. Iterate over each number in nums, adding it to prefix.
3. Compute needed = prefix - k and add the frequency of needed from the hash map to count (if present).
4. Increment the frequency of the current prefix in the hash map.
5. After the loop, return count.

## Dry Run

- nums=[1,1,1], k=2
- Start: map={0:1}, prefix=0, count=0
- i=0, num=1 → prefix=1, needed= -1 (not in map), count=0, map={0:1,1:1}
- i=1, num=1 → prefix=2, needed=0 found 1 time, count=1, map={0:1,1:1,2:1}
- i=2, num=1 → prefix=3, needed=1 found 1 time, count=2, map={0:1,1:1,2:1,3:1}
- Return 2

---

## Code

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap stores prefix sum -> frequency
        prefix_counts = {0: 1}
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            # needed prefix sum that would make current subarray sum to k
            need = prefix - k
            result += prefix_counts.get(need, 0)
            # record current prefix sum
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
        return result
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is processed once with O(1) hash operations. |
| **Space** | `O(n)` | In the worst case we store a distinct prefix sum for each index. |

## Edge Cases

- All zeros with k=0
- Negative numbers
- Single element array
- Large k outside possible sum range

---

## Interview Tips

- Clarify that subarrays are contiguous and non‑empty.
- Explain why we need the initial {0:1} entry.
- Mention handling of negative numbers makes sliding‑window unsuitable.
- Discuss integer overflow isn’t an issue in Python.

## Follow-up Questions

- Can you modify the solution to return the actual subarrays?
- What if the array is streamed and you cannot store all prefix sums?
- How would you adapt it for a fixed‑size sliding window sum?

## Key Takeaways

- **Prefix sum** reduces range queries to O(1) look‑ups.
- A **hash map** of prefix frequencies enables counting subarrays with a target sum in linear time.
- Initializing the map with 0 helps capture subarrays that start at index 0.

## Related Problems

- Subarray Sum Equals K II (LeetCode 974)
- Maximum Size Subarray Sum Equals K (LeetCode 325)
- Continuous Subarray Sum (LeetCode 523)

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
