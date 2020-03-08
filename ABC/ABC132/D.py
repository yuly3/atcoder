from scipy.misc import comb


def solve():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    for i in range(1, K+1):
        ans = comb(N-K+1, i, exact=True) * comb(K-1, i-1, exact=True)
        ans %= MOD
        print(ans)


if __name__ == '__main__':
    solve()
