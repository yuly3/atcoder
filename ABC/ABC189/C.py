import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    ans = 0
    for left in range(N):
        min_a = A[left]
        for right in range(left, N):
            min_a = min(min_a, A[right])
            ans = max(ans, (right - left + 1) * min_a)
    print(ans)


if __name__ == '__main__':
    solve()
