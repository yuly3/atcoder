from fractions import gcd


def solve():
    N, *A = map(int, open(0).read().split())
    
    ans = 0
    left = [0 for _ in range(N+1)]
    right = [0 for _ in range(N+1)]
    for i in range(N):
        left[i+1] = gcd(left[i], A[i])
    for i in range(N-1, -1, -1):
        right[i] = gcd(right[i+1], A[i])
    for i in range(N):
        ans = max(ans, gcd(left[i], right[i+1]))
    print(ans)


if __name__ == '__main__':
    solve()
