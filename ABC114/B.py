def solve():
    S = input()
    
    N = len(S)
    ans = 1000
    for i in range(N-2):
        num = int(S[i:i+3])
        ans = min(ans, abs(753-num))
    print(ans)


if __name__ == '__main__':
    solve()
