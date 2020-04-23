import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, N = map(int, rl().split())
    sr, sc = map(lambda x: int(x) - 1, rl().split())
    S = input()
    T = input()
    
    cy = sr
    for i in range(N):
        if S[i] == 'U':
            cy -= 1
            if cy < 0:
                print('NO')
                exit()
        if T[i] == 'D' and cy < H - 1:
            cy += 1
    
    cy = sr
    for i in range(N):
        if S[i] == 'D':
            cy += 1
            if H <= cy:
                print('NO')
                exit()
        if T[i] == 'U' and 0 < cy:
            cy -= 1
    
    cx = sc
    for i in range(N):
        if S[i] == 'L':
            cx -= 1
            if cx < 0:
                print('NO')
                exit()
        if T[i] == 'R' and cx < W - 1:
            cx += 1
    
    cx = sc
    for i in range(N):
        if S[i] == 'R':
            cx += 1
            if W <= cx:
                print('NO')
                exit()
        if T[i] == 'L' and 0 < cx:
            cx -= 1
    
    print('YES')


if __name__ == '__main__':
    solve()
