class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(x=0, dp={}):
            if x in dp:
                return dp[x]
            if x > n:
                return 0
            if x == n:
                return 1

            dp[x] = climb(x + 1, dp) + climb(x + 2, dp)
            return dp[x]

        return climb()
