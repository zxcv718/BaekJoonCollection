import sys
from itertools import combinations

arr = list(map(int, sys.stdin.read().split()))

def find_sum(arr, k, target):
    for comb in combinations(arr, k):
        if sum(comb) == target:
            ans = sorted(comb)
            print(*ans, sep="\n")
            return


find_sum(arr, 7, 100)
