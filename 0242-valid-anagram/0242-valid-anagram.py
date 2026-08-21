class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            fre[s[i]]=fre.get(s[i],0)+1
            fre[t[i]]=fre.get(t[i],0)-1
        for ch in fre:
            if fre[ch]!=0:
                return False
        return True

            