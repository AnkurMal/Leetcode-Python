class Solution:
    def trap(self, height: list[int]) -> int:
        st, en, mark, sum, lsum, lst = 0, len(height) - 1, 0, 0, 0, 0

        while (st + 1) <= en and height[st] <= height[st + 1]:
            st += 1

        while st <= en:
            mark = st + 1
            sum += lsum
            lsum = 0
            while mark <= en and height[mark] <= height[st]:
                lsum += height[st] - height[mark]
                mark += 1

            lst = st
            st = mark

        if lsum != 0:
            ma = list(reversed(height[lst + 1 :]))
            en, st, mark = len(ma) - 1, 0, 1
            while (st + 1) <= en and ma[st] <= ma[st + 1]:
                st += 1

            while st <= en:
                mark = st + 1

                while mark <= en and ma[mark] <= ma[st]:
                    sum += ma[st] - ma[mark]
                    mark += 1

                st = mark

        return sum
