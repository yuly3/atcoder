import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M, K = map(int, rl().split())
    s = [rl().rstrip() for _ in range(N)]
    
    limit = min(N, M)
    for n in range(limit, 0, -1):
        for sy in range(N - n + 1):
            for sx in range(M - n + 1):
                counter = Counter()
                for dy in range(n):
                    for dx in range(n):
                        counter[s[sy + dy][sx + dx]] += 1
                m = max(counter.values())
                if n * n - m <= K:
                    print(n)
                    return


if __name__ == '__main__':
    solve()
