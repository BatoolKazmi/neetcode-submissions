class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [] * len(temperature)
        stack = []

        for i, t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop() 
                # When you pop that means we found how many more days it will take
                # for that value to be bigger than it was on that day 
                res[stackInd] = i - stackInd
            stack.append((t , i))
        return res
        