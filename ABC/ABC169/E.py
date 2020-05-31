import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, rl().split())
    
    A.sort()
    B.sort()
    
    if N % 2 == 0:
        med_a = (A[N // 2 - 1] + A[N // 2]) / 2
        med_b = (B[N // 2 - 1] + B[N // 2]) / 2
        ans = int((med_b - med_a) // 0.5 + 1)
    else:
        med_a = A[N // 2]
        med_b = B[N // 2]
        ans = med_b - med_a + 1
    print(ans)


if __name__ == '__main__':
    solve()
