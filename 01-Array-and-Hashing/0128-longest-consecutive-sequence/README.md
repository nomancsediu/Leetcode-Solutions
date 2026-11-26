# 128. Longest Consecutive Sequence

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Set lookup |
| **LeetCode** | [Open problem](https://leetcode.com/problems/longest-consecutive-sequence/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

 

**Example 1:**

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

**Example 2:**

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Example 3:**

```
Input: nums = [1,0,1,2]
Output: 3
```

 

**Constraints:**

	- `0 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

---

## Brute Force

Sort the array and scan for consecutive runs, which costs O(n log n) time and O(1) extra space.

## Intuition

By putting every number in a **hash set** we can check existence of neighbours in O(1). We only start counting from numbers that are the **beginnings** of a sequence (i.e., num-1 is not in the set), which guarantees each element is visited at most once.

## Optimal Approach

Use a **hash set** to achieve O(1) look‑ups and iterate only from sequence starts, expanding forward to count the length.

## Step-by-Step Algorithm

1. Insert all elements of **nums** into a **set** for O(1) membership checks.
2. Initialize **max_len** to 0.
3. For each **num** in the set, if **num-1** is not in the set, treat **num** as the start of a sequence.
4. From this start, increment a counter while **num+1**, **num+2**, … are present in the set, updating **max_len** accordingly.

## Dry Run

- Input: [100,4,200,1,3,2] → set = {100,4,200,1,3,2}
- Iterate: 100 (99 not in set) → count 1, max=1
- 4 (3 in set) → skip
- 200 (199 not in set) → count 1, max stays 1
- 1 (0 not in set) → count 1,2,3,4 (2,3,4 present) → max=4
- 3,2 skipped because their predecessors exist

---

## Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty list
        if not nums:
            return 0
        num_set = set(nums)  # O(n) space for hash set
        max_len = 0
        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                cur_len = 1
                # Expand forward while consecutive numbers exist
                while current + 1 in num_set:
                    current += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each number is processed at most twice: once to find a start, once while expanding the sequence. |
| **Space** | `O(n)` | We store all numbers in a hash set. |

## Edge Cases

- Empty array → return 0
- Array with one element → return 1
- All duplicates → treat as single element
- Large negative and positive values – hash set handles them

---

## Interview Tips

- Clarify that the required complexity is O(n) and that sorting is not acceptable.
- Mention using a hash set for constant‑time look‑ups and why we only start from sequence beginnings.
- Discuss handling duplicates by using a set, which automatically removes them.
- Explain the worst‑case linear time proof.
- 

## Follow-up Questions

- Can you solve it with O(1) extra space if the array can be modified?
- How would you adapt the solution for a streaming input where numbers arrive one by one?
- What if you need to return the actual longest consecutive sequence, not just its length?

## Key Takeaways

- **Hash set** enables O(1) existence checks.
- Start counting only from **sequence beginnings** to avoid repeated work.
- Each element is visited a constant number of times, giving linear overall time.

## Related Problems

- Longest Increasing Subsequence
- Maximum Length of Pair Chain
- Find the Duplicate Number

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
