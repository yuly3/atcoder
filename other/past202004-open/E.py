import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = [0] * N
    for i in range(1, N + 1):
        j = i
        x = 0
        cnt = 0
        while x != i:
            x = A[j - 1]
            j = x
            cnt += 1
        ans[i - 1] = cnt
    print(*ans)


if __name__ == '__main__':
    solve()
