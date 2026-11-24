# 53. Maximum Subarray

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Kadane's Algorithm |
| **LeetCode** | [Open problem](https://leetcode.com/problems/maximum-subarray/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

 

**Example 1:**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

**Example 2:**

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

**Example 3:**

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-10^4 <= nums[i] <= 10^4`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

---

## Brute Force

Check every possible subarray and compute its sum, which takes O(n^2) time because there are n*(n+1)/2 subarrays.

## Intuition

The optimal subarray either extends the previous subarray or starts fresh at the current element; **keeping a running best sum ending at each position** lets us decide greedily. If the running sum becomes negative, it cannot contribute to a future maximum, so we reset it.

## Optimal Approach

Use **Kadane's Algorithm**, a dynamic programming technique that maintains the maximum subarray sum ending at the current index and the global maximum seen so far, both in O(1) extra space.

## Step-by-Step Algorithm

1. Initialize two variables: **current_sum** = nums[0] and **max_sum** = nums[0].
2. Iterate i from 1 to len(nums)-1:
3. Update **current_sum** = max(nums[i], current_sum + nums[i]) – either extend the previous subarray or start a new one at i.
4. Update **max_sum** = max(max_sum, current_sum) to record the best overall sum.
5. After the loop, return **max_sum** as the answer.

## Dry Run

- nums = [-2,1,-3,4,-1,2,1,-5,4]
- Start: current_sum = -2, max_sum = -2
- i=1, val=1 → current_sum = max(1, -2+1)=1, max_sum = max(-2,1)=1
- i=2, val=-3 → current_sum = max(-3,1-3)=-2, max_sum stays 1
- i=3, val=4 → current_sum = max(4,-2+4)=4, max_sum = 4
- i=4, val=-1 → current_sum = max(-1,4-1)=3, max_sum stays 4
- i=5, val=2 → current_sum = max(2,3+2)=5, max_sum = 5
- i=6, val=1 → current_sum = max(1,5+1)=6, max_sum = 6
- i=7, val=-5 → current_sum = max(-5,6-5)=1, max_sum stays 6
- i=8, val=4 → current_sum = max(4,1+4)=5, max_sum stays 6
- Return 6

---

## Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current and global maximum with the first element
        current_sum = max_sum = nums[0]
        # Iterate over the rest of the array
        for num in nums[1:]:
            # Either extend the previous subarray or start a new one at current index
            current_sum = max(num, current_sum + num)
            # Update global maximum if needed
            max_sum = max(max_sum, current_sum)
        return max_sum
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n)` | Each element is processed once in a single pass. |
| **Space** | `O(1)` | Only a few scalar variables are used regardless of input size. |

## Edge Cases

- All numbers negative – the algorithm returns the largest (least negative) element.
- Single element array – returns that element.
- Array with zeros and positives – zeros are handled naturally by max operation.

---

## Interview Tips

- Clarify that the problem asks for a contiguous subarray, not any subset.
- Explain why a negative running sum can be discarded – it would only reduce future sums.
- Mention that Kadane's algorithm is essentially a DP with O(1) state, which is why it’s optimal.

## Follow-up Questions

- Can you adapt the solution to also return the start and end indices of the maximum subarray?
- How would you solve the problem using a divide‑and‑conquer approach and what would its complexity be?
- What changes are needed if the subarray length must be at least k?

## Key Takeaways

- **Kadane's Algorithm** provides an O(n) greedy DP for maximum subarray problems.
- Maintaining **current best ending here** vs **global best** is a common DP pattern.
- When a running aggregate becomes detrimental (e.g., negative sum), **reset it**.

## Related Problems

- Maximum Subarray Sum with One Deletion
- Maximum Product Subarray
- Best Time to Buy and Sell Stock
- Longest Subarray with Sum at Most K

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
