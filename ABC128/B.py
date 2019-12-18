from operator import itemgetter


def solve():
    N = int(input())
    SP = [['', 0, 0] for _ in range(N)]
    for i in range(N):
        S, P = map(str, input().split())
        P = -int(P)
        SP[i] = [S, P, i+1]
    
    SP.sort(key=itemgetter(0, 1))
    for i in range(N):
        print(SP[i][2])


if __name__ == '__main__':
    solve()
