class sol:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [False] * (n + 1)
        
        dp[0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue 
                elif i == 0:
                    
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                   
                    dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
                else:
                    
                    from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                    from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    dp[j] = from_s1 or from_s2
        
        return dp[n]
