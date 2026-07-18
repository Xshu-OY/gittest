



# 广度优先遍历
from collections import deque
G = [
    {1, 2, 3},  # 0
    {0, 4, 6},  # 1
    {0, 3},  # 2
    {0, 2, 4},  # 3
    {1, 3, 5, 6},  # 4
    {4, 7},  # 5
    {1, 4},  # 6
    {5, }     #7
]
print(G)
def bfs(G, v):
    q = deque([v])
    # 同样需要申明一个集合来存放已经访问过的顶点，也可以用列表
    visited = {v}
    while q:
        u = q.popleft()
        print(u," ",end="")
        for w in G[u]:
            if w not in visited:
                q.append(w)
                visited.add(w)
print('广度深度优先bfs')
bfs(G, 0)


"""
[{1, 2, 3}, {0, 4, 6}, {0, 3}, {0, 2, 4}, {1, 3, 5, 6}, {4, 7}, {1, 4}, {5}]
广度深度优先bfs
0  1  2  3  4  6  5  7  

"""







