def check(s):
    return s==s[::-1]
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                if check(s[l+1:r+1]):
                    return True
                elif check(s[l:r]):
                    return True
                else:
                    return False

            l+=1
            r-=1
        return True