import sys
a = int(input())
arr = list(map(int, sys.stdin.read().split()))
arr.sort()

print(*arr, sep='\n')