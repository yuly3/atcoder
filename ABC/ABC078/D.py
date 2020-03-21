def solve():
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    
    if N == 1:
        print(abs(a[0] - W))
        exit()
    
    print(max(abs(a[-1] - W), abs(a[-2] - a[-1])))


if __name__ == '__main__':
    solve()
