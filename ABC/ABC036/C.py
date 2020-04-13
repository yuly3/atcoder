import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = [int(rl()) for _ in range(N)]
    b = sorted(a)
    
    compress = {b[0]: 0}
    idx = 0
    for i in range(1, N):
        if b[i] != b[i - 1]:
            idx += 1
            compress[b[i]] = idx
    
    for ai in a:
        print(compress[ai])


if __name__ == '__main__':
    solve()
