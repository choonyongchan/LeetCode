from math import floor, sqrt 

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [None for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, floor(sqrt(i+1))):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[n]