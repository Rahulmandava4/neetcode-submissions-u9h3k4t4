class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}
        for i,k in enumerate(nums):
            complement = target - k
            if complement in hash1:
                return [hash1[complement],i]
            hash1[k] = i
        return []
        