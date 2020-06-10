import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = list(map(int, rl().split()))
    b = list(map(int, rl().split()))
    
    d = sum(b) - sum(a)
    cnt = 0
    for i in range(N):
        if a[i] < b[i]:
            cnt += (b[i] - a[i] + 1) // 2
    if cnt <= d:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
