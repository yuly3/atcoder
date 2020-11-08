import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    pow3 = [1]
    while pow3[-1] < 10 ** 18:
        pow3.append(pow3[-1] * 3)
    
    pow5 = 1
    B = 0
    while pow5 < 10 ** 18:
        A = bisect_left(pow3, N - pow5)
        if pow3[A] == N - pow5 and A != 0 and B != 0:
            print(A, B)
            return
        pow5 *= 5
        B += 1
    print(-1)


if __name__ == '__main__':
    solve()
