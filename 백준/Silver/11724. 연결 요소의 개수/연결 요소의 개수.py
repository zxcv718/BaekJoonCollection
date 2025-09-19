import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
adj = [[] for _ in range(n + 1)] # 0번 인덱스는 사용안함 vertex는 1번부터 시작

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
components = 0
#DFS
for node in range(1, n + 1):
    if visited[node]: # 방문한 노드면 다음 노드로
        continue
    components += 1 # 반복문이 새로 시작한다는 것은 새로운 연결요소 라는 뜻
    stack = [node] # vertex 번호
    visited[node] = True # 방문했으니 true로 변경
    while stack:
        cur = stack.pop() # 마지막으로 추가된 vertex pop
        for nxt in adj[cur]:
            if not visited[nxt]: # 만약 모두 방문했다면 더이상 append가 안되어서 empty stack이라 while 탈출
                visited[nxt] = True
                stack.append(nxt)

print(components)
# 스택 동작(예시)
# 문제에서 사용한 테스트 입력(간선 순서):
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# edges: (1-2), (2-5), (5-1), (3-4), (4-6)
# 이때 생성된 인접리스트(입력 순서 유지):

# adj[1] = [2, 5]
# adj[2] = [1, 5]
# adj[5] = [2, 1]
# adj[3] = [4]
# adj[4] = [3, 6]
# adj[6] = [4]
# 시작: node=1 (첫 루프에서)

# 초기: stack = [1], visited[1]=True
# 반복1: pop -> cur=1, process neighbors 2,5
# nxt=2 : visited[2]=False → visited[2]=True, push 2 → stack becomes [2]
# nxt=5 : visited[5]=False → visited[5]=True, push 5 → stack becomes [2, 5]
# 반복2: pop -> cur=5 (LIFO이므로 5가 먼저 나옴), adj[5]=[2,1]
# nxt=2 visited True → skip
# nxt=1 visited True → skip → stack becomes [2]
# 반복3: pop -> cur=2, adj[2]=[1,5] 모두 visited → skip → stack 비어있음 → 첫 연결요소의 탐색 종료
