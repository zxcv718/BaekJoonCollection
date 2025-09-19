import sys

input = sys.stdin.readline

c = int(input())
n = int(input())
adj = [[] for _ in range(c + 1)] # 0번 인덱스는 사용안함 vertex는 1번부터 시작

count = 0
component = 0

for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (c + 1)

for node in range(1, c + 1):
    if visited[node]: # 방문한 노드면 다음 노드로
        continue
    component += 1
    if component > 1:
        break
    stack = [node] # vertex 번호
    visited[node] = True # 방문했으니 true로 변경
    while stack:
        cur = stack.pop() # 마지막으로 추가된 vertex pop
        for nxt in adj[cur]:
            if not visited[nxt]: # 만약 모두 방문했다면 더이상 append가 안되어서 empty stack이라 while 탈출
                visited[nxt] = True
                stack.append(nxt)

print(visited.count(True) - 1)