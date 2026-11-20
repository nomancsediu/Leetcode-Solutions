# 3041. Maximize Consecutive Elements in an Array After Modification

**Difficulty:** Hard
**Link:** https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

## Question
You are given a 0-indexed array nums consisting of positive integers.

Initially, you can increase the value of any element in the array by at most 1.

After that, you need to select one or more elements from the final array such that those elements are consecutive when sorted in increasing order. For example, the elements [3, 4, 5] are consecutive while [3, 4, 6] and [1, 1, 2, 3] are not.

Return the maximum number of elements that you can select.

 
Example 1:


Input: nums = [2,1,5,1,1]
Output: 3
Explanation: We can increase the elements at indices 0 and 3. The resulting array is nums = [3,1,5,2,1].
We select the elements [3,1,5,2,1] and we sort them to obtain [1,2,3], which are consecutive.
It can be shown that we cannot select more than 3 consecutive elements.

Example 2:


Input: nums = [1,4,7,10]
Output: 1
Explanation: The maximum consecutive elements that we can select is 1.


 
Constraints:


	1 <= nums.length <= 105
	1 <= nums[i] <= 106

## Approach
Each element v can become either v or v+1, i.e. it defines an interval [v, v+1]. We need the longest consecutive integer sequence that can be assigned to distinct intervals. Scanning the integer line from left to right we keep a min‑heap of intervals whose left endpoint is ≤ current integer and whose right endpoint is still ≥ current integer. At each integer we discard intervals that ended before it, then if the heap is non‑empty we assign the current integer to the interval with the smallest right endpoint (greedy choice). If the heap is empty we cannot extend the current consecutive block, so we start a new block at the next left endpoint. The longest block length seen during the scan is the answer.

## Steps
1. 1. For every number v in nums create an interval (v, v+1).
2. 2. Sort the intervals by their left endpoint v.
3. 3. Initialise pointers: i = 0 (next interval to insert), cur = smallest left endpoint, cur_len = 0, max_len = 0, and an empty min‑heap.
4. 4. While there are intervals left or the heap is non‑empty:
5.    a. Insert into the heap all intervals whose left ≤ cur (push their right = v+1).
6.    b. Remove from the heap any interval with right < cur (cannot cover cur).
7.    c. If the heap is non‑empty, pop the interval with the smallest right and assign cur to it; increment cur_len, advance cur by 1, and update max_len.
8.    d. Otherwise (heap empty): start a new block – set cur_len = 0, cur = next interval's left endpoint, clear the heap.
9. 5. Return max_len.
10. 6. The implementation follows the above logic inside the LeetCode class Solution.

## Complexity
- Time: O(n log n) – sorting plus each interval is pushed and popped at most once from the heap.
- Space: O(n) – the heap may hold up to all intervals in the worst case.

> Draft generated with Groq (openai/gpt-oss-120b). Review before relying on it.
