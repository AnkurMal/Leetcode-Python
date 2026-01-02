from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)

        for i in range(n):
            done = False
            for j in range(m):
                if flowerbed[j] != 1:
                    left = right = False
                    if j > 0 and flowerbed[j - 1] == 1:
                        left = True
                    if j < m - 1 and flowerbed[j + 1] == 1:
                        right = True

                    if not left and not right:
                        flowerbed[j] = 1
                        done = True
                        break

            if not done:
                return False

        return True
