import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    
    ans = 10 ** 10
    for y1 in range(1, H):
        s1 = y1 * W
        y2 = (H - y1) // 2
        y3 = H - y1 - y2
        s2 = y2 * W
        s3 = y3 * W
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
        x2 = W // 2
        x3 = W - x2
        s2 = (H - y1) * x2
        s3 = (H - y1) * x3
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    
    for x1 in range(1, W):
        s1 = x1 * H
        x2 = (W - x1) // 2
        x3 = W - x1 - x2
        s2 = x2 * H
        s3 = x3 * H
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
        y2 = H // 2
        y3 = H - y2
        s2 = (W - x1) * y2
        s3 = (W - x1) * y3
        ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    print(ans)


if __name__ == '__main__':
    solve()
