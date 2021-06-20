import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
  N = int(rl())
  A = list(map(int, rl().split()))
  
  counter = Counter(A)
  ans = 0
  for i, ai in enumerate(A):
    counter[ai] -= 1
    ans += N - 1 - i - counter[ai]
  print(ans)


if __name__ == '__main__':
    solve()
