class Solution:
    def compress(self, chars: List[str]) -> int:
        k = 0 # write pointer
        r = 0 # read pointer
        n = len(chars)

        while r < n:
            chars[k] = chars[r]
            k += 1
            j = r + 1
            
            while j < n and chars[j] == chars[r]:
                j += 1
            count = j - r
            
            if count > 1:
                for number in str(count):
                    chars[k] = number
                    k += 1

            r = j
        
        return k
        
        