import sys

a = int(input())
ans = [0] * 10001

for i in range(0, a):
    read = sys.stdin.readline
    ans[int(read())] += 1

for i in range(1, len(ans)):
    if ans[i] == 0:
        continue
    for _ in range(0, ans[i]):
        print(i)

