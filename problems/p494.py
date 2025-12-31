from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def target_sum(nums, target, index=0, curr=0, dp={}):
            if (index, curr) in dp:
                return dp[(index, curr)]
            if index == len(nums):
                return 1 if curr == target else 0

            count = target_sum(
                nums, target, index + 1, curr - nums[index], dp
            ) + target_sum(nums, target, index + 1, curr + nums[index], dp)
            dp[(index, curr)] = count

            return count

        return target_sum(nums, target)
