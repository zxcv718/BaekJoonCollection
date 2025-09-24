import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[[0] * m for _ in range(n)] for _ in range(h)]

for layer in range(h):
    for row in range(n):
        values = list(map(int, input().split()))
        for col in range(m):
            box[layer][row][col] = values[col]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
q = deque()
day = 0

zero_exists = False
for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                dist[z][y][x] = 0
                q.append((z, y, x))
            elif box[z][y][x] == 0:
                zero_exists = True
            elif box[z][y][x] == -1:
                dist[z][y][x] = -2

if not zero_exists:
    print(0)
    sys.exit(0)

while q:
    z, y, x = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if dist[nz][ny][nx] == -1 and box[nz][ny][nx] == 0:
                dist[nz][ny][nx] = dist[z][y][x] + 1
                day = max(day, dist[nz][ny][nx])
                q.append((nz, ny, nx))

target = -1
exists = any(cell == target for layer in dist for row in layer for cell in row)

print(target if exists else day)