class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        inx = 0

        for i in nums:
            if i > 0:
                break
            inx += 1

        nums = nums[inx:]

        if len(nums) == 0 or nums[0] > 1:
            return 1

        for i in range(len(nums) - 1):
            a, b = nums[i], nums[i + 1]
            if b - a > 1:
                return a + 1

        return nums[-1] + 1
