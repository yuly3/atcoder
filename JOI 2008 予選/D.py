from collections import defaultdict
from copy import deepcopy


def solve():
    m = int(input())
    p_xy = [[0, 0] for _ in range(m)]
    for i in range(m):
        p_xy[i] = list(map(int, input().split()))
    n = int(input())
    cx_dict, cy_dict = defaultdict(int), defaultdict(int)
    c_xy = [[0, 0] for _ in range(n)]
    for i in range(n):
        cx, cy = map(int, input().split())
        cx_dict[cx] += 1
        cy_dict[cy] += 1
        c_xy[i] = [cx, cy]
    
    for cx, cy in c_xy:
        dx, dy = cx - p_xy[0][0], cy - p_xy[0][1]
        tmp_x, tmp_y = deepcopy(cx_dict), deepcopy(cy_dict)
        tmp_x[cx] -= 1
        tmp_y[cy] -= 1
        flg = True
        for px, py in p_xy[1::]:
            if tmp_x[px + dx] == 0 or tmp_y[py + dy] == 0:
                flg = False
                break
            tmp_x[px + dx] -= 1
            tmp_y[py + dy] -= 1
        if flg:
            print(dx, dy)
            exit()


if __name__ == '__main__':
    solve()
