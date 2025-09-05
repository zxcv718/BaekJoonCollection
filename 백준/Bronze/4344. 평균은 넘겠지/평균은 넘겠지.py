a = int(input())
arr = [list(map(int, input().split())) for _ in range(a)]

for num in arr: # 여러개의 항목이 필요하므로 별도의 변수 선언이 가독성 좋음
    n = num[0]
    scores = num[1:]#1번 인덱스부터 끝까지 배열 추출
    avg = sum(scores) / n
    count = 0
    for i in scores:
        if i > avg:
            count += 1
    #count = sum(1 for x in scores if x > avg)#조건을 만족하면 1씩 더한다
    # for i in scores:
    #   if i > avg: count += 1
    print(f"{(count / n * 100):.3f}%")