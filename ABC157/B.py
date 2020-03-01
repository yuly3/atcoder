def solve():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())
    b = [int(input()) for _ in range(N)]
    
    bingo = [[False] * 3 for _ in range(3)]
    for bi in b:
        for i in range(3):
            for j in range(3):
                if A[i][j] == bi:
                    bingo[i][j] = True
    
    for i in range(3):
        cnt = 0
        for j in range(3):
            cnt += bingo[i][j]
        if cnt == 3:
            print('Yes')
            exit()
    for i in range(3):
        cnt = 0
        for j in range(3):
            cnt += bingo[j][i]
        if cnt == 3:
            print('Yes')
            exit()
    cnt = 0
    for i in range(3):
        cnt += bingo[i][i]
    if cnt == 3:
        print('Yes')
        exit()
    cnt = 0
    for i, j in [[0, 2], [1, 1], [2, 0]]:
        cnt += bingo[i][j]
    if cnt == 3:
        print('Yes')
        exit()
    print('No')


if __name__ == '__main__':
    solve()
