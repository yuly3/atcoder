import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    T = rl().rstrip()
    
    ans = 0
    for si, ti in zip(S, T):
        if si != ti:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
