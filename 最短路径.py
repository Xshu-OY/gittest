
# 迪杰斯特拉（Djikstra）算法


# dijkstra算法实现，图和路由的源点作为函数的输入，最短路径最为输出
MAX_value=99999
def dijkstra(graph,src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中所有节点
    visited=[]  # 表示已经路由到最短路径的节点集合
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance={src:0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i]=graph[src][i]  # 初始化
    print("最初每个节点到顶点0的距离（节点号：距离）")
    print(distance)
    path={src:{src:[]}}  # 记录源节点到每个节点的路径
    k=pre=src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance=new_distance
                    graph[src][d]=new_distance  # 进行距离更新
                    k=d
                    pre=v
        distance[k]=mid_distance  # 最短路径
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
        print("输出节点的添加过程（[添加节点],[剩余节点]）")
        print(visited,nodes)  # 输出节点的添加过程
    return distance,path
if __name__ == '__main__':
    graph_list = [[0,2,3, MAX_value,MAX_value,MAX_value,MAX_value],
                    [2,0,4,9,5,MAX_value,MAX_value],
                    [3,4,0,MAX_value,1,7,MAX_value],
                    [MAX_value,9,MAX_value, 0, 6, MAX_value,11],
                    [MAX_value,5,1,6,0,8,15],
                    [MAX_value,MAX_value,7,MAX_value,8,0,13],
                    [MAX_value,MAX_value,MAX_value,11,15,13,0]]

    distance,path= dijkstra(graph_list, 0)  # 查找从源点0开始带其他节点的最短路径
    print("运行结果：每个节点到顶点0的距离（节点号：距离）")
    print(distance,"\n")
    print("运行结果：每个节点到顶点0的经过节点路径（节点号：[经过节点号]）")
    print(path,"\n")


"""
最初每个节点到顶点0的距离（节点号：距离）
{0: 0, 1: 2, 2: 3, 3: 99999, 4: 99999, 5: 99999, 6: 99999}
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1] [2, 3, 4, 5, 6]
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1, 2] [3, 4, 5, 6]
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1, 2, 4] [3, 5, 6]
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1, 2, 4, 5] [3, 6]
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1, 2, 4, 5, 3] [6]
输出节点的添加过程（[添加节点],[剩余节点]）
[0, 1, 2, 4, 5, 3, 6] []
运行结果：每个节点到顶点0的距离（节点号：距离）
{0: 0, 1: 2, 2: 3, 3: 10, 4: 4, 5: 10, 6: 19} 
运行结果：每个节点到顶点0的经过节点路径（节点号：[经过节点号]）
{0: {0: [], 1: [1], 2: [2], 4: [2, 4], 5: [2, 5], 3: [2, 4, 3], 6: [2, 4, 6]}}

"""
