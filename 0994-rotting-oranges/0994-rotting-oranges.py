class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        time = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while fresh > 0 and q:
            time += 1
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (
                        row in range(ROWS)
                        and col in range(COLS)
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
        return time if fresh == 0 else -1
