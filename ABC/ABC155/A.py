def solve():
    ABC = list(map(int, input().split()))
    abc = set(ABC)
    if len(abc) == 2:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
