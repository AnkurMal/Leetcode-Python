class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for curr in range(len(nums)):
            for i in range(1, nums[curr] + 1):
                if curr + i < len(nums):
                    dp[curr + i] = min(
                        dp[curr + i],
                        dp[curr] + 1
                    )

        return dp[-1]