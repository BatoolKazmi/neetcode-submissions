class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        val = [1]
        i = 0
        while i != numRows:
            pascal.append(val)
            temp = []
            temp.append(1)
            for n in range(len(val)):
                if n + 1 > len(val) - 1:
                    temp.append(val[n])
                else:
                    temp.append(val[n + 1] + val[n])
                n += 1
            print(temp)
            val = temp
            i += 1
        return pascal
        

                     



