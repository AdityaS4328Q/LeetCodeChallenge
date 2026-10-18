import math
def helper(arr):
    if len(arr)<=1:
        return 1
    f=arr[0]
    left_arr=[]
    right_arr=[]
    for i in arr[1:]:
        if i<f:
            left_arr.append(i)
        else:
            right_arr.append(i)
    l=helper(left_arr)
    r= helper(right_arr)
    interleavings = math.comb(len(left_arr)+len(right_arr),len(left_arr))
    return (interleavings*r*l)%(10**9+7)


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        ans = helper(nums)
        return (ans -1)%(10**9+7)