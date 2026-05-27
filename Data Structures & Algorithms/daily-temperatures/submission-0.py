class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [] * len(temperature)
        stack = []

        for i, t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                stackInd, stackTemp = stack.pop()
                diff = i - stackInd
        stack.append([t , i])
        