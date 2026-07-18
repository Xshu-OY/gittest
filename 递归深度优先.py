
# 深度递归优先

from collections import deque
def dfs(G, v, visited=set()):
    print(v," ",end="")
    visited.add(v)  # 用来存放已经访问过的顶点
    # G[v] 是这个顶点的相邻的顶点
    for u in G[v]:
      #这一步很重要，否则进入无限循环，只有当这个顶点没有出现在这个集合中才会访问
        if u not in visited:
            dfs(G, u, visited)
print('递归深度优先dfs')
dfs(G, 0)

"""
递归深度优先 dfs
0  1  4  3  2  5  7  6

"""
