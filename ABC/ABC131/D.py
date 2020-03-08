from operator import itemgetter


def solve():
    N = int(input())
    AB = [[0, 0] for _ in range(N)]
    for i in range(N):
        AB[i] = list(map(int, input().split()))
    AB = sorted(AB, key=itemgetter(1))

    t = 0
    for i in range(N):
        t += AB[i][0]
        if t <= AB[i][1]:
            continue
        else:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    solve()