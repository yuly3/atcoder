import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    
    left = [i for i in range(M)]
    right = [2 * M - 1 - v for v in left]
    
    for i in range(M // 2):
        right[i] -= 2 * M + 1
    
    for i in range(M):
        left[i] %= N
        left[i] += 1
        right[i] %= N
        right[i] += 1
    
    for a, b in zip(left, right):
        print(a, b)


if __name__ == '__main__':
    solve()
