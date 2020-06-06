import sys
from collections import Counter
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = rl()
    A = tuple(map(int, rl().split()))
    
    acc = [0] + list(accumulate(A))
    counter = Counter(acc)
    ans = 0
    for key, val in counter.items():
        ans += val * (val - 1) // 2
    print(ans)


if __name__ == '__main__':
    solve()
