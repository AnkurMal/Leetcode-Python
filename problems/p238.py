from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref, suff = [nums[0]], [nums[-1]]

        for i in range(1, n - 1):
            pref.append(pref[i - 1] * nums[i])
            suff.append(suff[i - 1] * nums[n - i - 1])

        ans = [suff[-1]]
        for i in range(1, n - 1):
            ans.append(pref[i - 1] * suff[-i - 1])

        return ans + [pref[-1]]
