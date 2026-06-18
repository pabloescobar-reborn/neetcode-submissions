class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for word in strs:
            alpha = [0]* 26
            for char in word:
                alpha[ord(char) - ord('a')] += 1
            
            key = tuple(alpha)
            
            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(word)
        return list(hashmap.values())

        

        
        