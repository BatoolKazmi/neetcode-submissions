class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hashmap = {}
        horizontal, vertical = 0, 0
        hashmap[(horizontal, vertical)] = (horizontal, vertical)

        for i in range(len(path)):
            if path[i] == "N":
                horizontal += 1
            elif path[i] == "S":
                horizontal -= 1
            elif path[i] == "E":
                vertical += 1
            elif path[i] == "W":
                vertical -= 1
            
            if (horizontal, vertical) in hashmap:
                return True
            hashmap[(horizontal, vertical)] = (horizontal, vertical)
            
        return False