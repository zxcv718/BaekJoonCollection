import sys
from collections import deque

input = sys.stdin.readline
k = int(input())

for _ in range(k):
    v, e = map(int, input().split()) 
    graph = [[] for _ in range(v + 1)] # 평소 문제보다 한단계 더 필요
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (v + 1)
    is_binary = True

    for start in range(1, v + 1):
        if color[start] != 0: # 이미 방문함
            continue

        queue = deque()
        queue.append(start)
        color[start] = 1
        #bfs
        while queue and is_binary:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if color[nxt] == 0:
                    color[nxt] = -color[cur] # 핵심로직1
                    queue.append(nxt)
                elif color[nxt] == color[cur]: #핵심로직2
                    is_binary = False
                    break

        if not is_binary:
            break

    print("YES" if is_binary else "NO")