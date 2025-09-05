import sys
arr = list(map(int, sys.stdin.read().split()))

print(max(arr))
print(arr.index(max(arr)) + 1)