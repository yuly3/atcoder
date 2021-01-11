import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A, B = [], []
    for _ in range(N):
        ai, bi = map(int, rl().split())
        A.append(ai)
        B.append(bi)
    
    t = sum(A)
    s = [2 * A[i] + B[i] for i in range(N)]
    s.sort(reverse=True)
    
    p = 0
    ans = 0
    for si in s:
        p += si
        ans += 1
        if t < p:
            print(ans)
            return


if __name__ == '__main__':
    solve()
