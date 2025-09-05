a = int(input())
count = 0

def is_han(n: int) -> bool:
    chars = list(map(int, str(n)))
    diff = 10 #자리수 차이가 

    for i in range(0, len(chars) - 1):
        if diff == 10:
            diff = chars[i] - chars[i + 1]
        else:
            if diff != chars[i] - chars[i + 1]:
                return False  
    return True

if a < 100:
    print(a)

else:
    for i in range(100, a + 1):
        if is_han(i) == True:
            count += 1
    
    print(count + 99)
