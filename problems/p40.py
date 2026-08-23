from collections import Counter


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[] for _ in range(target + 1)]
        count = Counter(candidates)
        dp[0] = [[]]

        for i in range(target + 1):
            for k in candidates:
                n = i + k
                if n <= target:
                    for combo in dp[i]:
                        if combo.count(k) < count[k]:
                            new_combo = sorted(combo + [k])

                            if new_combo not in dp[n]:
                                dp[n].append(new_combo)

        return dp[target]
