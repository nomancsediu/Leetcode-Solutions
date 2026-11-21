# 169. Majority Element

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Boyer-Moore Voting Algorithm |
| **LeetCode** | [Open problem](https://leetcode.com/problems/majority-element/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times. You may assume that the majority element always exists in the array.

 

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```
**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5 * 10^4`

	- `-10^9 <= nums[i] <= 10^9`

	- The input is generated such that a majority element will exist in the array.

 

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

---

## Brute Force

Count each element using a hash map and return the one with count > n/2; O(n) time and O(n) space.

## Intuition

If we pair each occurrence of the majority element with a different element, the majority still remains because it appears more than half the time; thus we can cancel out non‑majority values while tracking a candidate.

## Optimal Approach

Use the **Boyer-Moore Voting Algorithm** which maintains a **candidate** and a **counter** while scanning the array once.

## Step-by-Step Algorithm

1. Initialize candidate = None and count = 0.
2. Iterate through each num in nums:
3. If count is 0, set candidate = num and count = 1.
4. Else if num == candidate, increment count; otherwise decrement count.
5. After the loop, candidate holds the majority element; return it.

## Dry Run

- nums = [2,2,1,1,1,2,2]
- Start: candidate=None, count=0
- num=2 -> count=0 so candidate=2, count=1
- num=2 -> same as candidate, count=2
- num=1 -> different, count=1
- num=1 -> different, count=0
- num=1 -> count=0 so candidate=1, count=1
- num=2 -> different, count=0
- num=2 -> count=0 so candidate=2, count=1
- End: candidate=2, which is the majority.

---

## Code

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        # Since the problem guarantees a majority, candidate is the answer
        return candidate
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | We scan the array only once. |
| **Space** | `O(1)` | Only two integer variables are used regardless of input size. |

## Edge Cases

- Array of length 1
- All elements are the same
- Majority element appears exactly floor(n/2)+1 times

---

## Interview Tips

- Explain why the majority element must survive the cancelation process.
- Mention that a second pass to verify the candidate can be added if the guarantee is removed.
- Compare with hash‑map solution and discuss trade‑offs in space.

## Follow-up Questions

- How would you modify the algorithm if the majority element might not exist?
- Can you find all elements appearing more than n/3 times?

## Key Takeaways

- **Boyer-Moore Voting** works when a single element exceeds half the array.
- Cancelation technique is useful for majority‑type problems.
- Maintain only constant extra state to achieve O(1) space.

## Related Problems

- Find Majority Element II
- Top K Frequent Elements
- Kth Largest Element in an Array

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
