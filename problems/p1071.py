class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        cop = str1

        while True:
            l1, l2 = len(str1), len(str2)
            if l1 < l2:
                str1, str2 = str2, str1
                l1, l2 = l2, l1
                cop = str1

            if str1.find(str2) != 0 or not str2:
                break
            str1 = str1[l2:]

        if not str2:
            return str1
        else:
            if cop.find(str2) == 0 and str1.find(str2) == 0:
                return str1
            else:
                return ""
