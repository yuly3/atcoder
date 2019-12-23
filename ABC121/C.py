from operator import itemgetter


def solve():
    N, M = map(int, input().split())
    AB = [[0, 0] for _ in range(N)]
    for i in range(N):
        AB[i][0], AB[i][1] = map(int, input().split())

    AB.sort(key=itemgetter(0))

    ans, cnt = 0, 0
    for i in range(N):
        if M <= cnt + AB[i][1]:
            ans += AB[i][0] * (M - cnt)
            break
        else:
            ans += AB[i][0] * AB[i][1]
            cnt += AB[i][1]
    print(ans)


if __name__ == '__main__':
    solve()
