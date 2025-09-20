#  https://www.acmicpc.net/problem/2178
import sys
from collections import deque


N, M = map(int, input().split())
graph = []
visit = [[False] * M for _ in range(N)]
time_list = [[1] * M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
queue.append((0, 0))
visit[0][0] = True

while queue:
    node = queue.popleft()
    y, x = node[0], node[1]

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if (0 <= tx < M) and (0 <= ty < N):
            if graph[ty][tx]:
                if not visit[ty][tx]:
                    visit[ty][tx] = 1
                    time_list[ty][tx] = time_list[y][x] + 1
                    queue.append((ty, tx))


print(time_list[-1][-1])
