class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def unique(x=0, y=0, dp={}):
            if (x, y) in dp:
                return dp[(x, y)]
            if x == m or y == n:
                return 0
            if x == m - 1 and y == n - 1:
                return 1

            dp[(x, y)] = unique(x + 1, y, dp) + unique(x, y + 1, dp)
            return dp[(x, y)]

        return unique()
