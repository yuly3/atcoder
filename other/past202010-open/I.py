import sys
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = list(map(int, rl().split()))
    
    sum_a = sum(a)
    half = sum_a / 2
    
    a *= 2
    acc_a = [0] + list(accumulate(a))
    
    ans = 10 ** 18
    for left in range(N):
        right = bisect_left(acc_a, half + acc_a[left])
        ans = min(ans, abs(sum_a - 2 * (acc_a[right] - acc_a[left])))
    print(ans)


if __name__ == '__main__':
    solve()
