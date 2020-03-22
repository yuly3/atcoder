def solve():
    H, W = map(int, input().split())
    _ = int(input())
    a = list(map(int, input().split()))
    
    ans = [[0] * W for _ in range(H)]
    ans[0][0] = 1
    a[0] -= 1
    direction = 1
    i, j, k = 0, 0, 1
    cnt = 1
    while cnt != H * W:
        if j == W - 1 and direction == 1:
            i += 1
            direction = -1
        elif j == 0 and direction == -1:
            i += 1
            direction = 1
        else:
            j += direction
        
        if a[k - 1] == 0:
            k += 1
        a[k - 1] -= 1
        ans[i][j] = k
        cnt += 1
    
    for line in ans:
        print(' '.join(map(str, line)))


if __name__ == '__main__':
    solve()
