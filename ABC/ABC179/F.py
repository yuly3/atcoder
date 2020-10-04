import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    
    left = top = N
    row, col = [N] * (N + 1), [N] * (N + 1)
    
    ans = (N - 2) ** 2
    for _ in range(Q):
        com, x = map(int, rl().split())
        if com == 1:
            if x < left:
                for i in range(x, left):
                    col[i] = top
                left = x
            ans -= col[x] - 2
        else:
            if x < top:
                for i in range(x, top):
                    row[i] = left
                top = x
            ans -= row[x] - 2
    print(ans)


if __name__ == '__main__':
    solve()
