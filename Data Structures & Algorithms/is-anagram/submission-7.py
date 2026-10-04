from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        # sorted_s = "".join(sorted(s, key=str.lower))
        # sorted_t = "".join(sorted(t, key=str.lower))
    

        # for i in range (len(s)):
        #     if sorted_s[i] != sorted_t[i]:
        #         return False
        
        # return True
        
        count_s = Counter(s)
        count_t = Counter(t)

        for char in count_s.keys():
            if char not in count_t or count_t[char] != count_s[char]:
                return False
        
        return True
        
            