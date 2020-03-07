def solve():
    N, A, B = map(int, input().split())
    
    ans = A * (N // (A + B)) + min(A, N % (A + B))
    print(ans)


if __name__ == '__main__':
    solve()
