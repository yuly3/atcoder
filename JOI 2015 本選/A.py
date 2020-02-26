def solve():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    A, B, C = [0] * N, [0] * N, [0] * N
    for i in range(1, N):
        A[i], B[i], C[i] = map(int, input().split())
    
    imos = [0] * (N + 1)
    pp = P[0]
    for pi in P[1:]:
        s, e = min(pp, pi), max(pp, pi)
        imos[s] += 1
        imos[e] -= 1
        pp = pi
    for i in range(1, N + 1):
        imos[i] += imos[i - 1]
    
    ans = 0
    for i in range(1, max(P)):
        ans += min(A[i] * imos[i], B[i] * imos[i] + C[i])
    print(ans)


if __name__ == '__main__':
    solve()
