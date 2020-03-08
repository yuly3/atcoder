def solve():
    N = int(input())
    for i in range(1000 - N):
        if len(set(str(N + i))) == 1:
            print(N + i)
            exit()


if __name__ == '__main__':
    solve()
