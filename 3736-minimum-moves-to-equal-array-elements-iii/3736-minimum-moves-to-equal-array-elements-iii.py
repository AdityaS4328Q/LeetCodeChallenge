class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        n= len(nums)
        res=0
        for i in range(n):
            res+= m-nums[i]
        return res