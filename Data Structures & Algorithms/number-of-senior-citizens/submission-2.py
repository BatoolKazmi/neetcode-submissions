class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        # 10 (phone number) + 1 (Gender) + 2 (age) + 2 (seat)

        for i in range(len(details)):
            print(int(details[i][11:13]))

            if int(details[i][11:13]) > 60:
                res += 1

        return res
            