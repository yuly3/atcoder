import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    M, K = map(int, rl().split())
    
    if M == 1:
        if 1 <= K:
            print(-1)
        else:
            print(0, 0, 1, 1)
        exit()
    
    if 1 << M <= K:
        print(-1)
        exit()
    
    ans = []
    for i in range(1 << M):
        if i != K:
            ans.append(i)
    ans.append(K)
    for i in range((1 << M) - 1, -1, -1):
        if i != K:
            ans.append(i)
    ans.append(K)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()
