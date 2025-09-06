import sys

a = int(input())

arr = list(set(sys.stdin.read().split()))
arr = sorted(arr, key=lambda s: (len(s), s))

print(*arr, sep="\n")