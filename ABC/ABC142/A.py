def solve():
    N = int(input())
    count = 0

    for i in range(1, N + 1):
        if i % 2 == 1:
            count += 1

    print(count / N)


if __name__ == '__main__':
    solve()
