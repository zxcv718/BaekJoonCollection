n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = sorted(arr, reverse=True)

def tree(a: list):
    if len(a) == 1:
        return a[0] - m
    else:       
        diff = a[0] - a[1]
        if diff >= m:
            if diff > m:
                return a[0] - m
            else:
                return a[1]
        else:
            lo, hi = 0, a[0]
            s = 0
            ans = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                l = [x for x in a if x > mid]
                s = sum(l) - (len(l) * mid)
                if s >= m:
                    lo = mid + 1
                    ans = mid
                else:
                    hi = mid - 1
            return ans

print(tree(arr1))