import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = rl().split()
    K = int(K)
    
    if K == 0:
        print(int(N))
        return
    
    ans = 0
    a = [int(ni) for ni in N]
    for _ in range(K):
        a.sort()
        g2 = int(''.join(map(str, a)))
        a.reverse()
        g1 = int(''.join(map(str, a)))
        ans = g1 - g2
        a = [int(ni) for ni in str(ans)]
    print(ans)


if __name__ == '__main__':
    solve()
