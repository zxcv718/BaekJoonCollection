import sys
q = []

n = int(input())
arr = list(map(str, sys.stdin.read().splitlines()))

for s in arr:
    parts = s.split()
    cmd = parts[0]

    if cmd == 'push':
        x = int(parts[1])
        q.append(x)
    elif cmd == 'pop':
        print(q.pop() if q else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(0 if q else 1)
    elif cmd == 'top':
        print(q[len(q) - 1] if q else -1)