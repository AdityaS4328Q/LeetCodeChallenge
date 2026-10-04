class Solution:
    def checkValidString(self, s: str) -> bool:
        high=0
        low = 0 
        for i in s:
            if i==')':
                low-=1
                high-=1
            elif i=='(':
                low +=1
                high+=1
            else:
                low-=1
                high+=1
            low=max(0,low)
            if high<0:
                return False
        return low==0