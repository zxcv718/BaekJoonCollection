a = int(input())
arr = list(map(int, input().split()))
ans = []

for i, t in enumerate(arr):
    if len(ans) == 0:
        print(0, end=" ")
    else:
        while ans and (ans[-1][1] < t):
            ans.pop()
        if ans:
            print(ans[-1][0] + 1, end=" ")
        else:
            print(0, end=" ")
    ans.append((i, t))
