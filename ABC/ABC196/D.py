import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline

ans = 0


def solve():
    H, W, A, B = map(int, rl().split())
    
    def f(room, cy, cx, da, db):
        if cy == H - 1 and cx == W - 1:
            global ans
            if room[cy][cx] and da == 0 and db == 0:
                ans += 1
            elif not room[cy][cx] and da == 0 and db == 1:
                ans += 1
            return
        if room[cy][cx]:
            if cx == W - 1:
                f(room, cy + 1, 0, da, db)
            else:
                f(room, cy, cx + 1, da, db)
        else:
            n_room = deepcopy(room)
            n_room[cy][cx] = True
            if 0 < db:
                if cx == W - 1:
                    f(n_room, cy + 1, 0, da, db - 1)
                else:
                    f(n_room, cy, cx + 1, da, db - 1)
            if 0 < da:
                if cx < W - 1:
                    nn_room = deepcopy(n_room)
                    nn_room[cy][cx + 1] = True
                    f(nn_room, cy, cx + 1, da - 1, db)
                if cy < H - 1:
                    n_room[cy + 1][cx] = True
                    if cx == W - 1:
                        f(n_room, cy + 1, 0, da - 1, db)
                    else:
                        f(n_room, cy, cx + 1, da - 1, db)
    
    s_room = [[False] * W for _ in range(H)]
    f(s_room, 0, 0, A, B)
    
    global ans
    print(ans)


if __name__ == '__main__':
    solve()
