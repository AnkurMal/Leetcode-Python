from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 1 and nums[0] == target:
            return [0] * 2

        res = [-1, -1]
        left, right = 0, n - 1

        while left < right:
            if res[0] == -1:
                if nums[left] == target:
                    res[0] = left
                else:
                    left += 1
            if res[1] == -1:
                if nums[right] == target:
                    res[1] = right
                else:
                    right -= 1

            if res[0] >= 0 and res[1] >= 0:
                break

        if n % 2 != 0 and nums[(n - 1) // 2] == target and res[0] < 0 and res[1] < 0:
            return [(n - 1) // 2] * 2

        if res[0] >= 0 and res[1] < 0:
            res[1] = res[0]
        elif res[0] < 0 and res[1] >= 0:
            res[0] = res[1]

        return res
