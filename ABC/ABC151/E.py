MOD = 10 ** 9 + 7
N, K, *A = map(int, open(0).read().split())
A.sort()

fact = [1, 1]
fact_inv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)


def cmb(n, r):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % MOD


def solve():
    ans = 0
    for j in range(N):
        num = cmb(j, K - 1) % MOD
        ans += num * A[j] % MOD
        ans -= num * A[N - j - 1] % MOD
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
