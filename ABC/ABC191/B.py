import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, X = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    ans = [ai for ai in A if ai != X]
    print(*ans)


if __name__ == '__main__':
    solve()
