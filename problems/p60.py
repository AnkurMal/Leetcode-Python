import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ran = list(range(1, n + 1))
        res = ""

        k -= 1
        for i in range(n - 1, -1, -1):
            fact = math.factorial(i)
            index = k // fact
            res = res + str(ran[index])
            ran.pop(index)
            k -= fact * index

        return res
