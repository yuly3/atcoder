def solve():
    N = int(input())
    F = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    
    ans = -10 ** 9
    for s in range(1, 1 << 10):
        benefit = 0
        for i in range(N):
            cnt = 0
            for j in range(10):
                if s >> j & 1 and F[i][j] == 1:
                    cnt += 1
            benefit += P[i][cnt]
        ans = max(ans, benefit)
    print(ans)


if __name__ == '__main__':
    solve()
