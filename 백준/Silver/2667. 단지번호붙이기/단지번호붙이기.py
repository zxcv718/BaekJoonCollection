import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
grid = [[int(ch) for ch in input().strip()] for _ in range(n)]
sizes: list[int] = []

def bfs(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for row in range(n):
        for col in range(n):
            if grid[row][col] != 1 or visited[row][col]:
                continue

            queue = deque([(row, col)])
            visited[row][col] = True
            count = 0

            while queue:
                r, c = queue.popleft()
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if visited[nr][nc] or grid[nr][nc] != 1:
                        continue
                    visited[nr][nc] = True
                    queue.append((nr, nc))

            sizes.append(count)
bfs(grid)
sizes = sorted(sizes)
print(len(sizes))

for size in sizes:
    print(size)