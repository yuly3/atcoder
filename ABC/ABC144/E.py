import numpy as np


def solve():
    N, K = map(int, input().split())
    a_l = np.array(input().split(), int)
    b_l = np.array(input().split(), int)
    a_l.sort()
    b_l.sort()
    b_l = b_l[::-1]

    sum_a = a_l.sum()
    left, right = -1, 10**13
    while left + 1 < right:
        mid = (left + right) // 2
        if sum_a - np.minimum(a_l, mid // b_l).sum() <= K:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == '__main__':
    solve()