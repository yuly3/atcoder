import sys

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    S = input()
    arr = []
    flg = 0
    tmp = ''
    for i in range(len(S)):
        if S[i].isupper():
            if not flg:
                flg = 1
                tmp += S[i]
            else:
                tmp += S[i]
                arr.append(tmp.lower())
                tmp = ''
                flg = 0
        else:
            tmp += S[i]
    
    arr.sort()
    for i in range(len(arr)):
        arr[i] = list(arr[i])
        arr[i][0] = arr[i][0].upper()
        arr[i][-1] = arr[i][-1].upper()
    
    for i in range(len(arr)):
        print(''.join(arr[i]), end='')
    print()


if __name__ == '__main__':
    solve()
