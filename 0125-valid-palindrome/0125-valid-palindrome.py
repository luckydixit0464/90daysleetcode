class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl=''.join(char for char in s if char.isalnum()).lower()
        k=0
        for j in range(len(cl)-1,-1,-1):
            if cl[j]!=cl[k]:
                return False
            k+=1
        return True

