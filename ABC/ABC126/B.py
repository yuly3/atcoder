def solve():
    s = input()
    first_harf = int(s[:2])
    second_harf = int(s[2:])

    if first_harf == 0 or first_harf > 12:
        if second_harf == 0 or second_harf > 12:
            print('NA')
        else:
            print('YYMM')
    else:
        if second_harf == 0 or second_harf > 12:
            print('MMYY')
        else:
            print('AMBIGUOUS')

if __name__ == '__main__':
    solve()