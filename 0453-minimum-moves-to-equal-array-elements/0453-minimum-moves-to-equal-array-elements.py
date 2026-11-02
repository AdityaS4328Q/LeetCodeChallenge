class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves=0
        m=min(nums)
        for i in nums:
            moves+= i - m
        return moves