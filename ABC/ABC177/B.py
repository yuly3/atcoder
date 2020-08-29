import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    T = rl().rstrip()
    
    ans = 1001
    for i in range(len(S) - len(T) + 1):
        cnt = len(T)
        for j in range(len(T)):
            cnt -= S[i + j] == T[j]
        ans = min(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
