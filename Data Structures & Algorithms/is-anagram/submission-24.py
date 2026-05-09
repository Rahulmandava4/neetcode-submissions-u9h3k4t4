class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i,0)+ 1
        for i in t:
            if i in hashmap and hashmap[i] > 0:
                hashmap[i] -=1
            
            else:
                return False
        return True
