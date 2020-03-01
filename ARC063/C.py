def solve():
    S = input()
    
    ans = 0
    p_char = S[0]
    for char in S[1:]:
        if p_char != char:
            ans += 1
            p_char = char
    print(ans)


if __name__ == '__main__':
    solve()
