import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dist = [[0] * m for _ in range(n)] # 0이면 미방문, 그리고 거기에 1씩 더해서 거리까지 한번에
dist[0][0] = 1 # 시작점은 1,1로 고정, 따라서 시작과 동시에 방문하기 때문에 1

queue = deque()
queue.append((0,0))
# 상, 하, 좌, 우 방향을 한 번에 처리하기 위한 델타 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()
    if x == n - 1 and y == m - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < m): # 범위 넘어서면 다음 조건식으로 이동
            continue
        if maze[nx][ny] == 0 or dist[nx][ny] != 0: # 갈수없는 칸이거나 방문했던 칸이면 다음 조건식으로 이동
            continue

        dist[nx][ny] = dist[x][y] + 1 # 거리 1씩 누적
        queue.append((nx, ny))

print(dist[-1][-1])