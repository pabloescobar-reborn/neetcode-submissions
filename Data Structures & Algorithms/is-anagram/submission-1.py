class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hashmap = {}
        t_hashmap = {}

        for char in s:
            s_hashmap[char] = s_hashmap.get(char, 0) + 1
        
        for char in t:
            t_hashmap[char] = t_hashmap.get(char, 0) + 1
        
        for key in s_hashmap:
            if s_hashmap[key] != t_hashmap.get(key, 0):
                return False
        
        return True


        