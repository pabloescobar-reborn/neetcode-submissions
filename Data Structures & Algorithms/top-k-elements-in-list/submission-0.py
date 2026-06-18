class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        sorted_arr = sorted(hashmap.items(),key = lambda x: x[1], reverse = True)

        res = []
        for x in range(k):
            res.append(sorted_arr[x][0])
        
        return res