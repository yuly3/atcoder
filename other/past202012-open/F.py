import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    ABC = [set(map(lambda n: int(n) - 1, rl().split())) for _ in range(M)]
    
    ans = 0
    for s in range(1, 1 << N):
        se = set()
        others = set()
        for i in range(N):
            if s >> i & 1:
                se.add(i)
            else:
                others.add(i)
        if any(len(se | abc) == len(se) for abc in ABC):
            continue
        cnt = 0
        for x in others:
            cse = se | {x}
            cnt += any(len(cse | abc) == len(cse) for abc in ABC)
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
