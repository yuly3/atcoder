def solve():
    a, b = map(str, input().split())
    A = ''.join([a for _ in range(int(b))])
    B = ''.join([b for _ in range(int(a))])
    tmp = sorted([A, B])
    print(tmp[0])


if __name__ == '__main__':
    solve()
