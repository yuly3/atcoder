from collections import defaultdict
import sys
rline = sys.stdin.readline


def solve():
    N = int(rline())
    counter = defaultdict(int)
    for _ in range(N):
        counter[int(rline())] += 1
    
    ans = 0
    for val in counter.values():
        if val % 2 == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
