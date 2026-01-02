class Solution:
    def reverseVowels(self, s: str) -> str:
        res, last, n = list(s), len(s) - 1, len(s)
        vowel = set("AEIOUaeiou")

        for i in range(n):
            if i >= last:
                break
            if res[i] in vowel:
                for j in range(last, -1, -1):
                    if res[j] in vowel:
                        res[i], res[j] = res[j], res[i]
                        last = j - 1
                        break

        return "".join(res)
