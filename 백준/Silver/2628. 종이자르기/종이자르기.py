x, y = map(int, input().split())
num = int(input())

if num == 0:
    print(x * y)
else:
    arr = [list(map(int, input().split())) for _ in range(num)]
    #값 없는 경우 대비
    v = [x[1] for x in arr if x[0] == 0]
    h = [x[1] for x in arr if x[0] == 1] 
    v.sort()
    h.sort()
    v.insert(0, 0)
    v.insert(len(v), y)
    h.insert(0, 0)
    h.insert(len(h), x)

def find_max(arr: list) -> int:
    tmp = 0
    for i in range(0, len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > tmp:
            tmp = abs(arr[i] - arr[i + 1])
    return tmp
# 그냥 각각 배열 만든 다음에 오름차순 정렬 하고 0번째 n-1 번째 인덱스에 각각 0과 x또는y넣고
# 반복문 돌려서 최댓값 뽑아내기

a = find_max(v)
b = find_max(h)
print(a * b)
    