import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    
    counter = Counter(S)
    ans = max(counter, key=counter.get)
    print(ans)


if __name__ == '__main__':
    solve()
