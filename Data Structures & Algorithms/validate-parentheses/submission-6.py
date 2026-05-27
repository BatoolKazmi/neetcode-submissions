class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedtoOpen = {"]" : "[", ")" : "(", "}" : "{" }

        for c in s:
            if c in closedtoOpen:
                if stack and stack[-1] == closedtoOpen[c]:
                    stack.pop()
                    print(stack)
                else:
                    return False
            else:
                stack.append(c)
                print(stack)
        
        return True if not stack else False