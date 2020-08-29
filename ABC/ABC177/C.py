import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    MOD = 10 ** 9 + 7
    
    sum_a = sum(A)
    ans = 0
    for ai in A:
        sum_a -= ai
        ans += ai * sum_a
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
