# 36. Valid Sudoku

| | |
|---|---|
| **Difficulty** | Medium |
| **Topic** | Array and Hashing |
| **Pattern** | Hash Set for rows, columns, and sub-boxes |
| **LeetCode** | [Open problem](https://leetcode.com/problems/valid-sudoku/) |
| **Solution** | [solution.py](./solution.py) |

---

## Problem

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

	- Each row must contain the digits `1-9` without repetition.

	- Each column must contain the digits `1-9` without repetition.

	- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

	- A Sudoku board (partially filled) could be valid but is not necessarily solvable.

	- Only the filled cells need to be validated according to the mentioned rules.

 

**Example 1:**

```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2:**

```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

 

**Constraints:**

	- `board.length == 9`

	- `board[i].length == 9`

	- `board[i][j]` is a digit `1-9` or `'.'`.

---

## Brute Force

Check each row, column, and sub-box separately by scanning and using a list to detect duplicates, leading to O(9*9*3)=O(1) but with higher constant factors and repeated scans

## Intuition

By storing the **seen digits** for each row, column, and 3×3 block in hash sets we can detect a repetition the moment it occurs, avoiding multiple passes over the same cells.

## Optimal Approach

Use three arrays of hash sets: one for rows, one for columns, and one for the 3×3 sub‑boxes. While iterating the board once, insert each digit into the corresponding sets and return false on a conflict.

## Step-by-Step Algorithm

1. Initialize three lists of 9 empty **sets**: rows, cols, and boxes.
2. Iterate over each cell (i from 0 to 8, j from 0 to 8).
3. If the cell contains '.', skip it.
4. Compute box_index = (i//3)*3 + j//3 and check if the digit is already in rows[i], cols[j] or boxes[box_index]; if so, return false; otherwise add it to the three sets.
5. If the loop finishes without conflicts, return true.

## Dry Run

- Board start: all sets empty.
- Cell (0,0)='5' → box 0; not in any set → add to rows[0], cols[0], boxes[0].
- Cell (0,1)='3' → box 0; add to rows[0], cols[1], boxes[0].
- Cell (1,0)='6' → box 0; add to rows[1], cols[0], boxes[0].
- Cell (0,4)='7' → box 1; add to rows[0], cols[4], boxes[1].
- Continue; when reaching a duplicate like another '5' in the same row, the check fails and returns false.

---

## Code

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 9 sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                # compute index of the 3x3 sub‑box
                box_index = (i // 3) * 3 + (j // 3)
                # check for duplicates
                if (val in rows[i]) or (val in cols[j]) or (val in boxes[box_index]):
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        return True
```

## Complexity

| | Complexity | Why |
|---|---|---|
| **Time** | `O(81) ≈ O(1)` | We visit each of the 81 cells once and each operation on a set is O(1). |
| **Space** | `O(27) ≈ O(1)` | We store at most 9 sets for rows, 9 for columns, and 9 for boxes, each holding at most 9 elements. |

## Edge Cases

- All cells are '.' (empty board)
- A board with a single duplicate in a row, column, or sub‑box
- Invalid characters (not needed per constraints)

---

## Interview Tips

- Clarify that we only need to validate the current board, not solve it.
- Mention using a single pass with three hash‑set collections to achieve O(1) space.
- Explain how to compute the 3×3 box index using integer division.
- If asked, discuss trade‑offs of using a fixed‑size boolean array instead of sets.

## Follow-up Questions

- Can you solve it using only O(1) extra space without hash sets?
- How would you adapt the solution for an N×N Sudoku where N is a perfect square?
- What changes if the board size is larger and you need to support streaming input?

## Key Takeaways

- **Hash Set** lookup gives O(1) duplicate detection
- **Single pass** over the grid is sufficient when maintaining auxiliary state
- Mapping a cell to its **sub‑box index** via (i//3)*3 + j//3 is a handy trick

## Related Problems

- LeetCode 36: Valid Sudoku
- LeetCode 37: Sudoku Solver
- LeetCode 423: Reconstruct Original Digits from English
- LeetCode 128: Longest Consecutive Sequence

---

> Draft generated with Groq (`openai/gpt-oss-120b`). Review before relying on it.
