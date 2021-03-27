import sys

import numpy as np

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def rotation(xy, r_axis, t, deg=False):
    if deg:
        t = np.deg2rad(t)
    xy = np.array(xy)
    r_axis = np.array(r_axis)
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    return np.dot(R, xy - r_axis) + r_axis


def solve():
    N = int(rl())
    x0, y0 = map(int, rl().split())
    x2, y2 = map(int, rl().split())
    
    cx = (x0 + x2) / 2
    cy = (y0 + y2) / 2
    xy1 = rotation((x0, y0), (cx, cy), 2 * np.pi / N)
    x1, y1 = map(float, xy1)
    print(x1, y1)


if __name__ == '__main__':
    solve()
