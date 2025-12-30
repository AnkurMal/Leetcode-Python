from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        
        index = 0
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                index = i
                break

        return index
