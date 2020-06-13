import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    
    counter = defaultdict(int)
    for _ in range(M):
        a, b = map(int, rl().split())
        counter[a] += 1
        counter[b] += 1
    
    for i in range(1, N + 1):
        if counter[i] % 2:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    solve()
