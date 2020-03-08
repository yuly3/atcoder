def solve():
    N, *A = map(int, open(0).read().split())
    
    cumsum = [0] * (N + 1)
    for i in range(1, N + 1):
        cumsum[i] = cumsum[i - 1] + A[i - 1]
    
    ans = [0] * (N + 1)
    for i in range(N):
        for j in range(i + 1, N + 1):
            ans[j - i] = max(ans[j - i], cumsum[j] - cumsum[i])
    print('\n'.join(map(str, ans[1:])))


if __name__ == '__main__':
    solve()
