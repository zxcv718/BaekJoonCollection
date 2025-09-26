import sys

MOD = 15746
TRANSFORMATION = (
    (1, 1),
    (1, 0),
)


def mat_mul(a, b):
    return (
        (
            (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD,
            (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD,
        ),
        (
            (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD,
            (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD,
        ),
    )


def mat_pow(k):
    # 행렬 거듭 제곱 (O(log k))
    result = ((1, 0), (0, 1))
    base = TRANSFORMATION
    while k:
        if k & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        k >>= 1
    return result


def apply(mat, vec):
    return (
        (mat[0][0] * vec[0] + mat[0][1] * vec[1]) % MOD,
        (mat[1][0] * vec[0] + mat[1][1] * vec[1]) % MOD,
    )


def main():
    n = int(sys.stdin.readline().strip())
    if n == 1:
        print(1)
        return

    base_vec = (1, 1)  # (dp[1], dp[0]) — dp[0]은 빈 문자열 한 가지
    answer = 0
    for length in range(2, n + 1):
        mat = mat_pow(length - 1)
        value, _ = apply(mat, base_vec)
        answer = value
    print(answer)


if __name__ == "__main__":
    main()
