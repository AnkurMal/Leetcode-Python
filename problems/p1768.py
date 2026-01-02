class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        le = max(l1, l2)
        st = ""

        for i in range(le):
            if i < l1:
                st += word1[i]
            if i < l2:
                st += word2[i]

        return st
