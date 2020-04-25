import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    b = list(map(int, rl().split()))
    
    ans = []
    for _ in range(N):
        j = -1
        for i in range(len(b)):
            if b[i] == i + 1:
                j = i
        if j == -1:
            print(-1)
            exit()
        del b[j]
        ans.append(j + 1)
    ans.reverse()
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
