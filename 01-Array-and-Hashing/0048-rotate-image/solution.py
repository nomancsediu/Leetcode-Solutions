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
