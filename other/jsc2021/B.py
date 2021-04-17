import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _, _ = map(int, rl().split())
    A = set(map(int, rl().split()))
    B = set(map(int, rl().split()))
    
    ans = []
    for i in range(1, 10 ** 3 + 1):
        if (i in A) ^ (i in B):
            ans.append(i)
    print(*ans)


if __name__ == '__main__':
    solve()
