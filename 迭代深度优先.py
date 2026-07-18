
# 迭代深度优先
from collections import deque
def dfs_iter(G, v):
    visited = set()
    s = [v]
    while s:
        u = s.pop()
        if u not in visited:
            print(u," ",end="")
            visited.add(u)
            s.extend(G[u])
print('迭代深度优先dfs')
dfs_iter(G, 0)

"""
迭代深度优先dfs
0  3  4  6  1  5  7  2  

"""

