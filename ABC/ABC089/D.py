def solve():
    H, W, D = map(int, input().split())
    posX, posY = [0] * (H * W + 1), [0] * (H * W + 1)
    for i in range(H):
        Ai = list(map(int, input().split()))
        for j in range(W):
            posX[Ai[j]] = i
            posY[Ai[j]] = j
    
    d_cum = [0] * (H * W + 1)
    for i in range(D + 1, H * W + 1):
        d_cum[i] = d_cum[i - D] + abs(posX[i] - posX[i - D]) + abs(posY[i] - posY[i - D])
    
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        print(d_cum[R] - d_cum[L])


if __name__ == '__main__':
    solve()
