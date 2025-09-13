import sys

n = int(input())
nums = list(map(int, sys.stdin.read().split()))
count = 0
h = 0

for i in reversed(nums):
    if i > h:
        h = i
        count += 1

print(count)    