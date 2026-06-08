class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        map_s={}
        map_t={}

        for char in s:
            map_s[char]=map_s.get(char,0)+1

        for char in t:
            map_t[char]=map_t.get(char,0)+1

        return map_s == map_t    
           
        