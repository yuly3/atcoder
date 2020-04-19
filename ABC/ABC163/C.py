import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    counter = defaultdict(int)
    for ai in A:
        counter[ai] += 1
    for i in range(1, N + 1):
        print(counter[i])


if __name__ == '__main__':
    solve()
