def solve():
    N = int(input())
    S = list(input())
    ans = []
    for s in S:
        ans.append(chr((ord(s) - ord('A') + N) % 26 + ord('A')))
    print(''.join(ans))


if __name__ == '__main__':
    solve()
