class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        
        return count
    
    def dfs(self, grid: List[List[str]], row: int, col: int) -> None:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
