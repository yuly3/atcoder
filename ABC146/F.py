def solve():
    N, M = map(int, input().split())
    S = list(input())[::-1]
    ans_l = []

    i = 0
    while i < N:
        for j in range(M, 0, -1):
            if i + j > N:
                continue
            if int(S[i+j]) == 0:
                ans_l.append(j)
                i += j
                break
            if j == 1:
                print(-1)
                exit()

    ans_l = ans_l[::-1]
    print(' '.join(map(str, ans_l)))


if __name__ == '__main__':
    solve()