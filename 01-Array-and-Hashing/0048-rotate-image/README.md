# 48. Rotate Image

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | In-place matrix transformation |
| **LeetCode** | [Open problem](https://leetcode.com/problems/rotate-image/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

 

**Example 1:**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

 

**Constraints:**

	- `n == matrix.length == matrix[i].length`

	- `1 <= n <= 20`

	- `-1000 <= matrix[i][j] <= 1000`

---

## Brute Force

Create a new matrix and copy rotated values, then assign back; O(n^2) time and O(n^2) extra space

## Intuition

The rotation can be achieved by first **transposing** the matrix (swap rows with columns) and then **reversing each row**. Transpose turns columns into rows, and the subsequent row reversal flips the order to achieve a 90° clockwise rotation.

## Optimal Approach

Use **in-place transpose** followed by **in-place row reversal**; both operations only need constant extra space.

## Step-by-Step Algorithm

1. **Transpose** the matrix: for each i from 0 to n-1, for each j from i+1 to n-1, swap matrix[i][j] with matrix[j][i].
2. **Reverse** each row: for each row, swap elements symmetrically from the ends moving towards the center.
3. Return (the matrix is modified in place).

## Dry Run

- Start with [[1,2,3],[4,5,6],[7,8,9]].
- After transpose: [[1,4,7],[2,5,8],[3,6,9]].
- Reverse each row: row0 -> [7,4,1], row1 -> [8,5,2], row2 -> [9,6,3].
- Result matches expected output.

---

## Code

```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """Rotate the n x n matrix 90 degrees clockwise in place.
        The function modifies matrix directly and returns None.
        """
        n = len(matrix)
        # Step 1: transpose the matrix (swap across the main diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: reverse each row to get the final rotated matrix
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(n^2)` | Every element is visited a constant number of times during transpose and reversal. |
| **Space** | `O(1)` | All swaps are done in place without extra data structures. |

## Edge Cases

- n=1 matrix (no change)
- Matrix with negative numbers
- Maximum size n=20 (still fits constraints)

---

## Interview Tips

- Clarify that the rotation must be in‑place and that using a second matrix is not allowed.
- Explain the two‑step process (transpose + reverse) before coding.
- Mention that swapping indices i<j avoids undoing previous swaps.
- Check boundary indices carefully to prevent out‑of‑range errors.

## Follow-up Questions

- Can you rotate the matrix counter‑clockwise in place?
- How would you rotate the matrix by 180° using similar ideas?
- What if the matrix is not square?

## Key Takeaways

- **Transpose** converts rows to columns in place.
- **Row reversal** after transpose yields a 90° clockwise rotation.
- Both steps together give an **O(1) extra space** solution for square matrices.

## Related Problems

- Spiral Matrix
- Set Matrix Zeroes
- Transpose Matrix
- Flip Equivalent Binary Trees

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
