def solve():
    A, B = map(int, input().split())
    if A < 10 and B < 10:
        print(A*B)
    else:
        print(-1)

if __name__ == '__main__':
    solve()
