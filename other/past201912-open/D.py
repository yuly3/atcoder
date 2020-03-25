import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    N = int(rl())
    A = [int(rl()) for _ in range(N)]
    arr = [False] * N
    
    x, y = -1, -1
    for ai in A:
        if arr[ai - 1]:
            y = ai
        else:
            arr[ai - 1] = True
    for i in range(N):
        if not arr[i]:
            x = i + 1
    if x == -1:
        print('Correct')
    else:
        print(y, x)


if __name__ == '__main__':
    solve()
