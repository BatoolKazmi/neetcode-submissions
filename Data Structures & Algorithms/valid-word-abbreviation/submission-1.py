class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        first, second = 0, 0

        while second < len(abbr) and first < len(word):
            
            if word[first] == abbr[second]:
                first += 1
                second += 1
            elif abbr[second].isdigit():
                if abbr[second] == '0':
                    return False
                num = 0
                while second < len(abbr) and abbr[second].isdigit():
                    num = num * 10 + int(abbr[second])
                    second += 1
                first += num 
            else:
                return False

        return first == len(word) and second == len(abbr)