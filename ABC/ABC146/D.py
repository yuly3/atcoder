import sys
sys.setrecursionlimit(10**7)

N = int(input())
edge = [[] for _ in range(N)]
v_dic = {}
b_l = []
for i in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edge[a].append(b)
    if a not in v_dic:
        v_dic[a] = 1
    else:
        v_dic[a] += 1
    if b not in v_dic:
        v_dic[b] = 1
    else:
        v_dic[b] += 1
    b_l.append(b)
colors = [0 for _ in range(N)]


def bfs(p_node, p_color):
    children_node = edge[p_node]
    c_color = 1
    for child_node in children_node:
        if c_color == p_color:
            c_color += 1
        colors[child_node] = c_color
        bfs(child_node, c_color)
        c_color += 1


def solve():
    bfs(0, 0)

    print(max(v_dic.values()))
    for b in b_l:
        print(colors[b])


if __name__ == '__main__':
    solve()
