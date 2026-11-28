# 54. Spiral Matrix

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Boundary Traversal |
| **LeetCode** | [Open problem](https://leetcode.com/problems/spiral-matrix/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

 

**Example 1:**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[i].length`

	- `1 <= m, n <= 10`

	- `-100 <= matrix[i][j] <= 100`

---

## Brute Force

Iterate layer by layer using extra visited matrix, O(m*n) time and O(m*n) space.

## Intuition

By keeping four moving **boundaries** (top, bottom, left, right) we can walk the outer ring in order, then shrink the rectangle and repeat; each element is visited exactly once.

## Optimal Approach

Use **four pointers** to represent current borders and a while‑loop that walks right, down, left, and up, adjusting the borders after each direction.

## Step-by-Step Algorithm

1. Initialize top=0, bottom=m-1, left=0, right=n-1 and an empty result list.
2. Traverse from left to right along the top row, then increment top.
3. Traverse from top to bottom along the right column, then decrement right.
4. If top <= bottom, traverse from right to left along the bottom row, then decrement bottom.
5. If left <= right, traverse from bottom to top along the left column, then increment left.
6. Repeat until the result contains m*n elements.

## Dry Run

- matrix=[[1,2,3],[4,5,6],[7,8,9]]; top=0,bottom=2,left=0,right=2
- Right: add 1,2,3 → top=1
- Down: add 6,9 → right=1
- Left: add 8,7 → bottom=1
- Up: add 4 → left=1
- Right: add 5 → top=2 (stop) → result=[1,2,3,6,9,8,7,4,5]

---

## Code

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []
        while len(res) < m * n:
            # move right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            # move down
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            # move left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            # move up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(m*n)` | Each cell is visited exactly once. |
| **Space** | `O(1)` | Only a few integer pointers and the output list are used. |

## Edge Cases

- Single row matrix
- Single column matrix
- Non‑square matrix (more rows than columns or vice‑versa)
- Matrix with one element

---

## Interview Tips

- Clarify constraints and ask if the matrix can be empty (LeetCode guarantees at least 1x1).
- Explain the four‑boundary idea before coding and show how it avoids revisiting cells.
- Mention that the algorithm works for any rectangular shape, not just squares.

## Follow-up Questions

- How would you modify the solution to return the elements in counter‑clockwise order?
- Can you do it in-place without extra output list (e.g., write to a pre‑allocated array)?

## Key Takeaways

- **Boundary pointers** are a clean way to traverse matrix layers.
- Shrink the problem space after each full perimeter walk.
- Always check the remaining dimensions before each direction to avoid duplicates.

## Related Problems

- 54. Spiral Matrix II
- 59. Spiral Matrix III
- 73. Set Matrix Zeroes
- 79. Word Search

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
