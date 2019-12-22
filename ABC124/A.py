def solve():
    A, B = map(int, input().split())
    
    ans = 0
    if A < B:
        ans += B
        B -= 1
    else:
        ans += A
        A -= 1
    ans += max(A, B)
    print(ans)


if __name__ == '__main__':
    solve()
