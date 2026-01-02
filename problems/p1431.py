from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        biggest = max(candies)
        for ind, i in enumerate(candies):
            if i + extraCandies >= biggest:
                res[ind] = True

        return res
