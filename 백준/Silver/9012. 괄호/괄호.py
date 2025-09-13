import sys

a = input()
arr = list(map(str, sys.stdin.read().splitlines()))

for s in arr:
    a = s
    while True:
        if a.count("()") != 0:
            a = a.replace("()", "", 1)
        else:
            break
    print("YES") if a == "" else print("NO")