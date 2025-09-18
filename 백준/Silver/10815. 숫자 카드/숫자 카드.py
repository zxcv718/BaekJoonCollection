n = int(input())
cards1 = list(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

sorted_cards1 = sorted(cards1)

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] == target:
            return 1
        else:
            end = mid - 1
    return 0

for i in cards2:
    res = binary_search(sorted_cards1, i)
    print(res, end = " ")