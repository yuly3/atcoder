import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = 0
    for i in range(1, 10 ** 6 + 1):
        if N < int(str(i) + str(i)):
            break
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
