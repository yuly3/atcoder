import sys

rl = sys.stdin.readline


def solve():
    _ = int(rl())
    a = list(map(int, rl().split()))
    
    ans = 10 ** 10
    for i in range(-100, 101):
        tmp = 0
        for ai in a:
            tmp += (ai - i) ** 2
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solve()
