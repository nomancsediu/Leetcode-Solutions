# 238. Product of Array Except Self

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Prefix and Suffix Products |
| **LeetCode** | [Open problem](https://leetcode.com/problems/product-of-array-except-self/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

 

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```
**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

 

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-30 <= nums[i] <= 30`

	- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

 

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

---

## Brute Force

For each index compute the product of all other elements by scanning the whole array, giving O(n^2) time.

## Intuition

The product for position *i* can be split into the product of all elements to its left and the product of all elements to its right. By pre‑computing these left‑hand and right‑hand products we can obtain each answer in O(1) time, yielding an overall O(n) solution.

## Optimal Approach

Use **two passes** with **prefix** and **suffix** product accumulation while storing the result directly in the output array, achieving O(1) extra space.

## Step-by-Step Algorithm

1. Initialize an output array of length n with all 1s.
2. First pass (left to right): keep a running **prefix** product; for each index i set output[i] = prefix and then multiply prefix by nums[i].
3. Second pass (right to left): keep a running **suffix** product; for each index i multiply output[i] by suffix and then multiply suffix by nums[i].
4. Return the output array.

## Dry Run

- nums = [1,2,3,4]
- Initialize output = [1,1,1,1]; prefix=1
- i=0 → output[0]=1, prefix=1*1=1
- i=1 → output[1]=1, prefix=1*2=2
- i=2 → output[2]=2, prefix=2*3=6
- i=3 → output[3]=6, prefix=6*4=24
- Now suffix=1
- i=3 → output[3]=6*1=6, suffix=1*4=4
- i=2 → output[2]=2*4=8, suffix=4*3=12
- i=1 → output[1]=1*12=12, suffix=12*2=24
- i=0 → output[0]=1*24=24, suffix=24*1=24
- Result = [24,12,8,6]

---

## Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # output will hold the final answer; start with 1s for multiplication
        answer = [1] * n
        # First pass: compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        # Second pass: compute suffix products and multiply into answer
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is visited a constant number of times. |
| **Space** | `O(1)` | Only a few scalar variables are used besides the output array, which does not count toward extra space. |

## Edge Cases

- Array contains a single zero
- Array contains multiple zeros
- All elements are 1 or -1
- Very large n up to 10^5

---

## Interview Tips

- Clarify that division is not allowed and ask if the output array can be used for in‑place computation.
- Mention handling of zeros explicitly before coding.
- Explain why two passes suffice and how prefix/suffix products avoid recomputation.
- State the space analysis clearly, noting the output array is excluded.

## Follow-up Questions

- Can you modify the solution to handle the case where division is allowed and achieve O(n) time with O(1) extra space?
- How would you extend the approach to a 2‑D matrix where each cell needs the product of its row and column excluding itself?
- What if the numbers were large and overflow could occur – how would you mitigate it?

## Key Takeaways

- **Prefix‑suffix accumulation** lets you combine left and right information in linear time.
- **Two‑pass scanning** is a common way to achieve O(1) extra space for problems that need both forward and backward context.
- When division is forbidden, pre‑computing cumulative products is the go‑to technique.

## Related Problems

- Maximum Product Subarray
- Subarray Product Less Than K
- Find the Duplicate Number
- Sliding Window Maximum

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
