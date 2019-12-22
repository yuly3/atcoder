def solve():
    A = int(input())
    B = int(input())
    for i in range(1, 4):
        if i != A and i != B:
            print(i)


if __name__ == '__main__':
    solve()
