from collections import defaultdict


def solve():
    N = int(input())
    if N == 1:
        print(1)
        exit()
    xy = [[0, 0] for _ in range(N)]
    for i in range(N):
        xy[i][0], xy[i][1] = map(int, input().split())
    
    dxy = defaultdict(int)
    for i in range(N - 1):
        for j in range(i + 1, N):
            dxy[(xy[i][0] - xy[j][0], xy[i][1] - xy[j][1])] += 1
            dxy[(xy[j][0] - xy[i][0], xy[j][1] - xy[i][1])] += 1
    
    zeros = max(dxy.values())
    print(N - zeros)


if __name__ == '__main__':
    solve()
