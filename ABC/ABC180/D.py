import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y, A, B = map(int, rl().split())
    
    ans = (Y - X - 1) // B
    cnt = 0
    while X < -(-Y // A):
        cnt += 1
        X *= A
        ans = max(ans, cnt + (Y - X - 1) // B)
    print(ans)


if __name__ == '__main__':
    solve()
