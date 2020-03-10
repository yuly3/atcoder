def solve():
    _ = int(input())
    A = list(map(int, input().split()))
    
    kind = set(A)
    if len(kind) % 2 == 0:
        print(len(kind) - 1)
    else:
        print(len(kind))


if __name__ == '__main__':
    solve()
