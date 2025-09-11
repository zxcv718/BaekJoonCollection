from itertools import combinations

num, s = map(int, input().split())

arr = list(map(int, input().split()))

i = 1
count = 0

def find_sum(arr, k, target):
        global count
        for comb in combinations(arr, k):
            if sum(comb) == target:
                count += 1

while i <= num:
    find_sum(arr, i, s)
    i += 1           

print(count)