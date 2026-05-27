class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(list)

        for i, n in enumerate(nums):
            res = target - n
            print(res)
            print(hash(res))
            if res in hash:
                return [hash(res), i]
            hash[n] = i