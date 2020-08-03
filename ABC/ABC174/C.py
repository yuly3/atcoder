import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    
    mods = [7 % K]
    for _ in range(10 ** 6):
        if mods[-1] == 0:
            print(len(mods))
            return
        mods.append((mods[-1] * 10 + 7) % K)
    print(-1)


if __name__ == '__main__':
    solve()
