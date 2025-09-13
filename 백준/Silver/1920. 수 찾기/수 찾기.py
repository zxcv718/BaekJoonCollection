import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

for i in arr2:
    if binary_search(arr1, i) == -1:
        print(0)
    else:
        print(1)
