import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    red = []
    blue = []
    for _ in range(N):
        x, c = rl().split()
        if c == 'R':
            red.append(int(x))
        else:
            blue.append(int(x))
    red.sort()
    blue.sort()
    
    cnt_r, cnt_b = 0, 0
    for _ in range(N):
        if cnt_r == len(red):
            print(blue[cnt_b])
            cnt_b += 1
        else:
            print(red[cnt_r])
            cnt_r += 1


if __name__ == '__main__':
    solve()
