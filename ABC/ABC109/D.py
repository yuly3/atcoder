def solve():
    H, W = map(int, input().split())
    grid = [[] for _ in range(H)]
    for i in range(H):
        grid[i] = list(map(int, input().split()))
    
    ans = []
    for i in range(H):
        for j in range(W - 1):
            if grid[i][j] % 2 == 1:
                grid[i][j + 1] += 1
                ans += [[i + 1, j + 1, i + 1, j + 2]]
    for i in range(H - 1):
        if grid[i][W - 1] % 2 == 1:
            grid[i + 1][W - 1] += 1
            ans += [[i + 1, W, i + 2, W]]
    
    N = len(ans)
    print(N)
    for ans_i in ans:
        print(' '.join(map(str, ans_i)))


if __name__ == '__main__':
    solve()
