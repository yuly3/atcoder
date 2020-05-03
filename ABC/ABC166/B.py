import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    
    su_set = set()
    for _ in range(K):
        _ = int(rl())
        ai = list(map(int, rl().split()))
        for aij in ai:
            su_set.add(aij)
    
    print(N - len(su_set))


if __name__ == '__main__':
    solve()
