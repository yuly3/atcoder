def solve():
    S = input()
    
    N = len(S)
    ans, i = 0, 0
    while i < N:
        count = 0
        j = i
        while j < N:
            if S[j] == 'A' or S[j] == 'C' or S[j] == 'G' or S[j] == 'T':
                count += 1
                j += 1
            else:
                break
        i = j + 1
        ans = max(ans, count)
    print(ans)


if __name__ == '__main__':
    solve()
