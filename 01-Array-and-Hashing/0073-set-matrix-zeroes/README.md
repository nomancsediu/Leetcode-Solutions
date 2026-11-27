# 73. Set Matrix Zeroes

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | In‑place marking using first row & column |
| **LeetCode** | [Open problem](https://leetcode.com/problems/set-matrix-zeroes/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

 

**Example 1:**

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

 

**Constraints:**

	- `m == matrix.length`

	- `n == matrix[0].length`

	- `1 <= m, n <= 200`

	- `-2^31 <= matrix[i][j] <= 2^31 - 1`

 

**Follow up:**

	- A straightforward solution using `O(mn)` space is probably a bad idea.

	- A simple improvement uses `O(m + n)` space, but still not the best solution.

	- Could you devise a constant space solution?

---

## Brute Force

Use an auxiliary matrix of size m×n to record zeros and then overwrite, which costs O(mn) time and O(mn) space.

## Intuition

If a cell is zero, its whole row and column must become zero. By storing flags in the first row and first column we can remember which rows/columns need zeroing **without extra memory**; we just need two extra booleans to remember whether the first row or first column originally contained a zero.

## Optimal Approach

Use the **first row and first column as markers** for rows and columns that should be zeroed, plus two boolean variables to track if the first row/column themselves need zeroing.

## Step-by-Step Algorithm

1. Scan the matrix to determine if the first row has any zero (store in `first_row_zero`).
2. Scan the matrix to determine if the first column has any zero (store in `first_col_zero`).
3. Iterate over the rest of the matrix (i>0, j>0); when a zero is found, set `matrix[i][0]=0` and `matrix[0][j]=0` as markers.
4. Traverse the matrix again (i>0, j>0) and set `matrix[i][j]=0` if either its row marker `matrix[i][0]` or column marker `matrix[0][j]` is zero.
5. Finally, zero out the first row if `first_row_zero` is true and the first column if `first_col_zero` is true.

## Dry Run

- Matrix [[1,1,1],[1,0,1],[1,1,1]]: first row no zero → `first_row_zero=False`; first column no zero → `first_col_zero=False`.
- Marking phase: cell (1,1) is zero → set matrix[1][0]=0 and matrix[0][1]=0.
- Zeroing phase: cells in row 1 or column 1 become zero → result [[1,0,1],[0,0,0],[1,0,1]].

---

## Code

```python
class Solution:
    def setZeroes(self, matrix):
        """Modify matrix in‑place so that rows and columns containing a zero become all zeros."""
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        # Determine if first row/col need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Zero first row/col if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(m·n)` | Each element is visited a constant number of times. |
| **Space** | `O(1)` | Only the two boolean flags are extra; the matrix itself is used for storage. |

## Edge Cases

- Single row or single column matrices
- Matrix with no zeros
- Matrix where the first row or first column contains zeros

---

## Interview Tips

- Clarify that the operation must be in‑place and discuss trade‑offs of extra space.
- Explain the need for the two extra booleans to avoid overwriting marker information.
- Walk through a tiny example to show how markers work before coding.

## Follow-up Questions

- Can you modify the algorithm to work when the matrix is read‑only and you must return a new matrix?
- What if the matrix is extremely large and does not fit in memory—how would you handle it?
- Can you extend the idea to a 3‑D matrix?

## Key Takeaways

- Using **in‑place markers** (first row/column) converts O(m+n) extra space into O(1).
- Always preserve original marker rows/columns with separate flags when they themselves may need modification.
- Separate the **marking** and **zeroing** passes to avoid premature overwrites.

## Related Problems

- LeetCode 73. Set Matrix Zeroes (same problem)
- LeetCode 289. Game of Life
- LeetCode 566. Reshape the Matrix
- LeetCode 48. Rotate Image

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
