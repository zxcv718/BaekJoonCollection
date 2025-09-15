n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
# 구역을 나누었을때 내부의 구역을 새로운 2차원 배열로 만들고
# 0과 1 둘중 하나로 통일되어 있지 않으면 섞여 있다는 의미니까 분할진행
# 통일되어있으면 거기서 stop 하고 count += 1
def slicing_matrix(arr: list):
    global white, blue
    if len(arr) == 1 or all_same(arr):
        if arr[0][0] == 1:
            blue += 1
        else:
            white += 1
        return
    else:
        n = len(arr)
        mid = n // 2
        top_left  = [row[:mid] for row in arr[:mid]]
        top_right = [row[mid:] for row in arr[:mid]]
        bot_left  = [row[:mid] for row in arr[mid:]]
        bot_right = [row[mid:] for row in arr[mid:]]
        slicing_matrix(top_left)
        slicing_matrix(top_right)
        slicing_matrix(bot_left)
        slicing_matrix(bot_right)

def all_same(matrix: list):
    vals = {v for row in matrix for v in row}
    return len(vals) <= 1

slicing_matrix(matrix)
print(white)
print(blue)