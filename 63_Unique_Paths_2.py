class sol:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R = len(obstacleGrid)
        C =len(obstacleGrid[0])

        #dp = [[0 for col in range(C+1)] for row in range(R+1)]
        dp = [0]*C
        #dp[R-1][C-1] = 1
        dp[C-1]=1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c]:
                    #dp[r][c]=0
                    dp[c]=0
                #else:
                    #dp[r][c] += (dp[r][c+1]+dp[r+1][c])
                elif c+1 < C:
                    dp[c] += dp[c+1] 

        return dp[0]
