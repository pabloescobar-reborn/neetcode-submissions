class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,num in enumerate(nums):
            req = target - num

            if req in hashmap:
                return [hashmap[req],i]

            hashmap[num] = i      