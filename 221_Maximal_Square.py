class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        # dp[i][j] stores the side length of the maximum square
        # whose bottom-right corner is (i, j)
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # The side length is 1 plus the minimum of the
                        # top, left, and top-left diagonal neighbors
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    # Update the overall maximum side length found so far
                    max_side = max(max_side, dp[i][j])

        # The result is the area of the largest square
        return max_side * max_side
