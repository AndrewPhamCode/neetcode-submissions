class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            grid[row][col] = '0'
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if grid[new_row][new_col] == '0':
                    continue
                if grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)
            
        
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    # for i in range(len(grid)):
                    #     print(grid[i])
                    # print('nriuh')
                    island_count += 1
        return island_count