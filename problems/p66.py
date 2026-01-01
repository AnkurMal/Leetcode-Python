from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            ind = -1
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] != 9:
                    ind = i
                    break
                digits[i] = 0

            if ind != -1:
                digits[ind] += 1
            else:
                digits[0] = 1
                digits.append(0)

        return digits
