import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 10 ** 5
    for i in range(10, 0, -1):
        a = 1000 * i
        if a < N:
            break
        ans = a - N
    print(ans)


if __name__ == '__main__':
    solve()
