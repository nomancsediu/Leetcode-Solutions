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
