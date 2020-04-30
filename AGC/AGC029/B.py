import sys
from bisect import bisect_right
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    pow_of_2 = [1]
    while pow_of_2[-1] < 2 * 10 ** 9:
        pow_of_2.append(pow_of_2[-1] * 2)
    
    A.sort(reverse=True)
    counter = defaultdict(int)
    for ai in A:
        counter[ai] += 1
    
    ans = 0
    for ai in A:
        if counter[ai] == 0:
            continue
        idx = bisect_right(pow_of_2, 2 * ai) - 1
        t = pow_of_2[idx]
        aj = t - ai
        if 1 < counter[aj] or 0 < counter[aj] and ai != aj:
            ans += 1
            counter[ai] -= 1
            counter[aj] -= 1
    print(ans)


if __name__ == '__main__':
    solve()
