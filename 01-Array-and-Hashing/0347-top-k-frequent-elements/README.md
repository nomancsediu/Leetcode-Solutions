# 347. Top K Frequent Elements

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Bucket Sort / Frequency Hash Map |
| **LeetCode** | [Open problem](https://leetcode.com/problems/top-k-frequent-elements/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

 

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

	- `k` is in the range `[1, the number of unique elements in the array]`.

	- It is **guaranteed** that the answer is **unique**.

 

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

---

## Brute Force

Count frequencies with a hash map then sort the items by frequency, taking O(n log n) time for sorting.

## Intuition

The most frequent elements are those with the highest counts. By **bucket sorting** frequencies we can retrieve the top k without a full sort, achieving linear time.

## Optimal Approach

Use a **hash map** to count occurrences, then place each number into a **bucket array** indexed by its frequency; finally iterate buckets from high to low to collect k elements.

## Step-by-Step Algorithm

1. Count each number's frequency using a **hash map** (O(n)).
2. Create an array of buckets where index i holds all numbers appearing i times.
3. Populate the buckets by iterating over the hash map entries.
4. Traverse the bucket array from the highest frequency down, adding numbers to the result until k elements are collected.

## Dry Run

- nums=[1,1,2,2,2,3], k=2
- freq map → {1:2,2:3,3:1}
- buckets size=4 → [[],[3],[1],[2]]
- iterate from i=3 → add 2, result=[2]; i=2 → add 1, result=[2,1]; stop (k=2)

---

## Code

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # 2. Create buckets: index = frequency
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        # 3. Gather top k elements from high freq to low
        res = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Counting and bucket filling are linear, and scanning buckets touches at most n elements total. |
| **Space** | `O(n)` | Hash map stores up to n unique keys and buckets store n elements overall. |

## Edge Cases

- All elements are the same
- k equals number of unique elements
- Negative numbers in the array
- Very large n (up to 10^5)

---

## Interview Tips

- Clarify that the answer order does not matter, so any collection order is fine.
- Mention that bucket sort leverages the fact that frequency ≤ n, giving O(n) space.
- Explain why this meets the follow‑up requirement (better than O(n log n)).
- If asked, discuss alternative using a min‑heap of size k (O(n log k)).

## Follow-up Questions

- Can you solve it using a heap and what would the complexity be?
- How would you modify the solution if k is very large, close to the number of unique elements?
- What if the input range is huge and you cannot allocate O(n) buckets?

## Key Takeaways

- **Hash map** for counting frequencies
- **Bucket sort** to achieve linear time selection of top‑k
- Choosing between **heap** vs **bucket** based on k and value range

## Related Problems

- 347. Top K Frequent Elements
- 451. Sort Characters By Frequency
- 692. Top K Frequent Words
- 169. Majority Element

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
