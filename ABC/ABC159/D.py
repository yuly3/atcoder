import sys
from collections import defaultdict

rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    counter = defaultdict(int)
    for ai in A:
        counter[ai] += 1
    
    B = defaultdict(int)
    for ai in A:
        B[ai] = counter[ai] * (counter[ai] - 1) // 2
    
    tmp = sum(B.values())
    for ai in A:
        print(tmp - B[ai] + (counter[ai] - 1) * (counter[ai] - 2) // 2)


if __name__ == '__main__':
    solve()
