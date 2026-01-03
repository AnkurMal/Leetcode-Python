from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for key, val in Counter(nums).items():
            if val * 2 == len(nums):
                return key
        return 0
