from math import floor


def solve():
    A, B = map(int, input().split())
    for i in range(1, 10000):
        if A == floor(i * 0.08) and B == floor(i * 0.1):
            print(i)
            exit()
    print(-1)


if __name__ == '__main__':
    solve()
