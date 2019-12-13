def solve():
    N, K, Q = map(int, input().split())
    point = [K for _ in range(N)]

    for _ in range(Q):
        answer = int(input()) - 1
        point[answer] += 1

    for i in range(N):
        if point[i] > Q:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()
