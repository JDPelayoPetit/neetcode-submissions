from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        if len(count_s) != len(count_t):
            return False

        for char in count_s.keys():
            if char not in count_t or count_t[char] != count_s[char]:
                return False
        
        return True
        
            