class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        li = []

        def recurse(perm, rem):
            if not rem:
                li.append(perm.copy())
                return

            for i in range(len(rem)):
                if i > 0 and rem[i] == rem[i - 1]:
                    continue
                recurse(perm + [rem[i]], rem[:i] + rem[i + 1 :])

        nums.sort()
        recurse([], nums)
        return li
