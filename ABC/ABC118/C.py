from fractions import gcd


def solve():
    N, *A = map(int, open(0).read().split())
    
    ans = A[0]
    for i in range(1, N):
        ans = gcd(ans, A[i])
    print(ans)


if __name__ == '__main__':
    solve()
