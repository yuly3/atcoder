import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, R, N = map(int, rl().split())
    if R == 1:
        print(A if A <= 10 ** 9 else 'large')
        return
    
    ans = A
    cnt = 0
    while cnt < N - 1:
        if 10 ** 9 < ans:
            print('large')
            return
        ans *= R
        cnt += 1
    print(ans if ans <= 10 ** 9 else 'large')


if __name__ == '__main__':
    solve()
