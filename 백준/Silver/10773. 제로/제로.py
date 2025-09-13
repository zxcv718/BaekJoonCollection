import sys

a = input()
arr = list(map(int, sys.stdin.read().splitlines()))
ans = []

for i in arr:
    if i != 0:
        ans.append(i)
    else:
        ans.pop()

print(sum(ans))