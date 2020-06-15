import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    counter = Counter(A)
    A.sort()
    B = [True] * (10 ** 6 + 1)
    ans = 0
    for ai in A:
        if B[ai]:
            for i in range(ai, 10 ** 6 + 1, ai):
                B[i] = False
            if counter[ai] == 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
