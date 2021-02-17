import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W = map(int, rl().split())
    S = [rl().rstrip() for _ in range(H)]
    T = [list(rl().rstrip()) for _ in range(H)]
    
    pos_in_S = set()
    pos_in_T = [[] for _ in range(4)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                pos_in_S.add((i, j))
            if T[i][j] == '#':
                pos_in_T[0].append((i, j))
    
    for i in range(1, 4):
        for cy, cx in pos_in_T[i - 1]:
            pos_in_T[i].append((-cx, cy))
    
    for i in range(4):
        for dy in range(-20, 21):
            for dx in range(-20, 21):
                flg = True
                for py, px in pos_in_T[i]:
                    cy, cx = py + dy, px + dx
                    if not (0 <= cy < H and 0 <= cx < W):
                        flg = False
                        break
                    if (cy, cx) in pos_in_S:
                        flg = False
                        break
                if flg:
                    print('Yes')
                    return
    print('No')


if __name__ == '__main__':
    solve()
