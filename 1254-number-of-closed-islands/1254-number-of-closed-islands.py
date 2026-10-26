
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            if grid[r][c]==1:
                return True
            grid[r][c]=1
            isClosed= True
            if r==0 or r==m-1 or c==0 or c==n-1:
                isClosed= False
            up = dfs(r+1,c)
            nex= dfs(r, c+1)
            prev = dfs(r, c-1)
            down = dfs(r-1,c)
            return isClosed and up and nex and prev and down
        
        m= len(grid)
        n= len(grid[0])
        
        count=0
        for c in range(n):
            for r in range(m):
                if grid[r][c]==0:
                    if dfs(r,c):
                        count+=1
        return count