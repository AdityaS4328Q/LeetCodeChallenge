class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = arr1[:]
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count.remove(i)
                    break
                
        return len(count)