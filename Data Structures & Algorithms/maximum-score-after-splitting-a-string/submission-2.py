class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        one, zero = s.count("1"), 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                one -= 1
            elif s[i] == "0":
                zero += 1
            num = one + zero

            res = max(res, num)

        return res