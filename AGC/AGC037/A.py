import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = input()
    
    ans = 0
    ps, cs = '', ''
    for si in S:
        cs += si
        if cs != ps:
            ps = cs
            cs = ''
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
