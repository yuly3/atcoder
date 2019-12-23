def solve():
    A, B, K = map(int, input().split())

    cnt = 0
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                exit()


if __name__ == '__main__':
    solve()
