from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n + 1):
    q.append(i)

print('<', end="")
while True:
    q.rotate(-k)
    print(q.pop(), end="")
    if not q:
        break
    else:
        print(', ', end="")
print('>')