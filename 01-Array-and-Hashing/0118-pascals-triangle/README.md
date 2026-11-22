# 118. Pascal's Triangle

| | |
|---|---|
| **Difficulty** | Easy |
| **Topic** | Array and Hashing |
| **Pattern** | Iterative construction |
| **LeetCode** | [Open problem](https://leetcode.com/problems/pascals-triangle/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given an integer `numRows`.

Return the first `numRows` of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it and the first and last number on each row must be equal to 1, as shown below:

 

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

 

**Constraints:**

	- `1 <= numRows <= 30`

---

## Brute Force

Generate each row by computing binomial coefficients from scratch using factorials, leading to O(numRows^2) time and O(1) extra space per row

## Intuition

The triangle can be built **row by row** because each element only depends on the two elements directly above it; by reusing the previous row we avoid recomputation

## Optimal Approach

Use **iterative building** with a list of lists, each new row is created from the last row by adding adjacent pairs and padding with 1s

## Step-by-Step Algorithm

1. Initialize result with the first row [[1]]
2. For each i from 2 to numRows, create a new row starting with 1
3. Iterate j from 1 to i-2 and set new_row[j]=prev_row[j-1]+prev_row[j]
4. Append 1 to the end of new_row and add it to result
5. Return result

## Dry Run

- numRows=4
- result=[[1]]
- i=2 -> prev=[1], new=[1,1], result=[[1],[1,1]]
- i=3 -> prev=[1,1], new starts [1], j=1 adds 1+1=2, new becomes [1,2], append 1 -> [1,2,1], result adds it
- i=4 -> prev=[1,2,1], new starts [1], j=1 adds 1+2=3, j=2 adds 2+1=3, new=[1,3,3], append 1 -> [1,3,3,1]

---

## Code

```python
class Solution:
    def generate(self, numRows: int):
        # result will hold all rows
        result = []
        for i in range(numRows):
            # start each row with 1s
            row = [1] * (i + 1)
            # compute inner elements using previous row
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(numRows^2)` | We compute each of the ~numRows*(numRows+1)/2 elements once |
| **Space** | `O(numRows^2)` | We store all rows in the output list |

## Edge Cases

- numRows=1 returns [[1]]
- numRows=2 returns [[1],[1,1]]

---

## Interview Tips

- Clarify that the output includes all rows up to numRows
- Mention that each row can be built from the previous one in O(i) time
- Discuss space trade‑off if only the last row is needed
- Explain handling of small inputs like 1

## Follow-up Questions

- How to generate a specific row without building the whole triangle?
- Can you compute the triangle using O(1) extra space besides the output?
- What if the numbers become large—how to handle overflow?

## Key Takeaways

- **Iterative row construction** avoids recomputing binomial coefficients
- **In‑place update** of a list can reduce space when only the last row is needed
- **Pascal's triangle** naturally exhibits overlapping subproblems

## Related Problems

- Pascal's Triangle II
- Triangle
- Unique Paths

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
