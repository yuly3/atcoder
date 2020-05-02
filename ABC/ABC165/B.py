import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = int(rl())
    
    a = 100
    ans = 0
    while a < X:
        a = a + int(a * 0.01)
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
