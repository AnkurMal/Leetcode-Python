import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def recurse(nums):
            if len(nums) == 0:
                yield []
                return

            for i in nums:
                n = copy.deepcopy(nums)
                n.remove(i)

                for li in recurse(n):
                    li.append(i)
                    yield li

        return list(recurse(nums))
