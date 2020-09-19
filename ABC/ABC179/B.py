import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    D = [list(map(int, rl().split())) for _ in range(N)]
    
    for i in range(N - 2):
        if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and D[i + 2][0] == D[i + 2][1]:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    solve()
