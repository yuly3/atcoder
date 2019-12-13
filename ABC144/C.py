import sys
import random
import math


def is_prime(q, k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q & 1 == 0: return False

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return False
    return True


def solve():
    N = int(input())
    if is_prime(N):
        print(N - 1)
        sys.exit()

    sq = int(math.sqrt(N))
    for i in range(sq, 1, -1):
        if N % i == 0:
            print(i + N // i - 2)
            sys.exit()


if __name__ == '__main__':
    solve()
