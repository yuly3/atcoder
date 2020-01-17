from itertools import product


def solve():
    N = int(input())
    x, y, h = [0] * N, [0] * N, [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())

    xt, yt, ht = -1, -1, -1
    for i in range(N):
        if h[i] != 0:
            xt, yt, ht = x[i], y[i], h[i]
            break
    
    for cx, cy in product(range(101), repeat=2):
        ans_h = ht + abs(cx - xt) + abs(cy - yt)
        flg = True
        for i in range(N):
            if h[i] != max(ans_h - abs(x[i] - cx) - abs(y[i] - cy), 0):
                flg = False
                break
        if flg:
            print(cx, cy, ans_h)
            exit()


if __name__ == '__main__':
    solve()
