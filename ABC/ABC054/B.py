import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]
    
    def check(y, x):
        res = True
        for dy in range(M):
            for dx in range(M):
                if A[y + dy][x + dx] != B[dy][dx]:
                    res = False
                    break
            if not res:
                break
        return res
    
    for sy in range(N - M + 1):
        for sx in range(N - M + 1):
            if check(sy, sx):
                print('Yes')
                exit()
    print('No')


if __name__ == '__main__':
    solve()
