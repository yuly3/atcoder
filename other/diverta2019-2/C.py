import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    A.sort()
    
    ope = [[] for _ in range(N - 1)]
    for i in range(N - 2):
        if 0 <= A[i + 1]:
            ope[i] = [A[0], A[i + 1]]
            A[0] -= A[i + 1]
        else:
            ope[i] = [A[-1], A[i + 1]]
            A[-1] -= A[i + 1]
    ope[N - 2] = [A[-1], A[0]]
    
    ans = A[-1] - A[0]
    print(ans)
    for x, y in ope:
        print(x, y)


if __name__ == '__main__':
    solve()
