import sys
rline = sys.stdin.readline


def solve():
    H, W = map(int, input().split())
    
    if H == 1 or W == 1:
        print(1)
        exit()
    
    if H % 2 == 1:
        if W % 2 == 1:
            print(((H + 1) // 2) * ((W + 1) // 2) + (H // 2) * (W // 2))
        else:
            print(((H + 1) // 2) * (W // 2) + (H // 2) * (W // 2))
    else:
        if W % 2 == 1:
            print(((W + 1) // 2) * (H // 2) + (W // 2) * (H // 2))
        else:
            print((W // 2) * H)


if __name__ == '__main__':
    solve()
