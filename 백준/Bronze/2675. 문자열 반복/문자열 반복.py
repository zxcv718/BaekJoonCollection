num = int(input())
arr = [list(input().split()) for _ in range(num)]

#숫자, 문자열 따로 빼서 배열 2개 만들기

count = []
strs = []

for i in arr:
    count.append(i[0])
    strs.append(i[1])

for i in range(0, num):
    a = count[i]
    b = strs[i]
    for j in b:
        for _ in range(0, int(a)):
            print(j, end = "")
    print()
