def solve():
    N = int(input())
    C, S, F = [0] * (N - 1), [0] * (N - 1), [0] * (N - 1)
    for i in range(N - 1):
        C[i], S[i], F[i] = map(int, input().split())
    
    ans = [0] * N
    for i in range(N - 1):
        t = C[i] + S[i]
        for j in range(i + 1, N - 1):
            if S[j] <= t and t % F[j] == 0:
                t += C[j]
            elif t < S[j]:
                t = C[j] + S[j]
            else:
                t += C[j] + F[j] - (t % F[j])
        ans[i] = t
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
