def solve():
    N, K, *p = map(int, open(0).read().split())
    
    idx = 0
    tmp, p_sum = sum(p[:K]), sum(p[:K])
    for i in range(N - K):
        tmp -= p[i]
        tmp += p[i + K]
        if p_sum < tmp:
            p_sum = tmp
            idx = i + 1
    
    cumsum = [i for i in range(1, 200001)]
    for i in range(1, 200000):
        cumsum[i] += cumsum[i - 1]
    
    ans = 0
    for i in range(idx, idx + K):
        ans += cumsum[p[i] - 1] / p[i]
    print(ans)


if __name__ == '__main__':
    solve()
