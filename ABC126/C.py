def solve():
    N, K = map(int, input().split())
    ans = 0

    for i in range(1, N+1):
        count = 0
        while i * 2 ** count < K:
            count += 1
        ans += (1 / N) * (1 / 2 ** count)

    print(ans)

if __name__ == '__main__':
    solve()