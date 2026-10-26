class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            if grid[r][c]==0:
                return 0
            curr=grid[r][c]
            grid[r][c]=0

            up = dfs(r-1, c)
            down= dfs(r+1,c)
            right= dfs(r,c+1)
            left=dfs(r,c-1)

            return up + down + right + left + curr
        
        m=len(grid)
        n= len(grid[0])
        count=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]>0:
                    co = dfs(r,c)
                    if co%k==0:
                        count+=1
        return count