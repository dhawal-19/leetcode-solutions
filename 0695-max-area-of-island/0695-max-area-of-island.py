class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxarea = 0
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or c < 0 
                or r == ROWS
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                cnt = dfs(i, j)
                maxarea = max(maxarea, cnt)
        return maxarea
