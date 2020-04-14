import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, A, B = map(int, rl().split())
    s = [[0] * W for _ in range(H)]
    for i in range(B):
        for j in range(A, W):
            s[i][j] = 1
    for i in range(B, H):
        for j in range(A):
            s[i][j] = 1
    for si in s:
        print(''.join(map(str, si)))


if __name__ == '__main__':
    solve()
