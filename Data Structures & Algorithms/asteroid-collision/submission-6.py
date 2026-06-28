class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[n] < 0:
                if abs(asteroids[n]) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroids[n]) == stack[-1]:
                    stack.pop()
                    asteroids[n] = 0
                    break
                else:
                    asteroids[n] = 0
                    break
            
                  
            if asteroids[n] != 0:
                stack.append(asteroids[n])

        return stack