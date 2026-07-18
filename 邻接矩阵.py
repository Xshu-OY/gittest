import networkx as nx               #调用networkx
import matplotlib.pyplot as plt         #调用matplotlib，绘制图
class Graph_Matrix:   #邻接矩阵Adjacency Matrix
    def __init__(self, vertices=[], matrix=[]):  
        self.matrix = matrix
        self.edges_dict = {}  # {(tail, head):weight}
        self.edges_array = []  # (tail, head, weight)
        self.vertices = vertices
        self.num_edges = 0
        if len(matrix) > 0:   #创建边的列表
            if len(vertices) != len(matrix):
                raise IndexError
            self.edges = self.getAllEdges()
            self.num_edges = len(self.edges)
        elif len(vertices) > 0:   #节点 列表
            self.matrix = [[0 for col in range(len(vertices))] for row in range(len(vertices))]
        self.num_vertices = len(self.matrix)
    def isOutRange(self, x):   #越界
        try:
            if x >= self.num_vertices or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")
    def isEmpty(self):   #是否为空
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices == 0
    def add_vertex(self, key):   #添加 结点
        if key not in self.vertices:
            self.vertices[key] = len(self.vertices) + 1
        # 添加一个节点意味着 添加行和列, 对每一行都 添加一列
        for i in range(self.getVerticesNumbers()):
            self.matrix[i].append(0)
        self.num_vertices += 1
        nRow = [0] * self.num_vertices
        self.matrix.append(nRow)
    def getVertex(self, key):    #返回 节点
        pass
    def add_edges_from_list(self, edges_list):  # 边列表: [(tail, head, weight),()]
        for i in range(len(edges_list)):
            self.add_edge(edges_list[i][0], edges_list[i][1], edges_list[i][2], )
    def add_edge(self, tail, head, cost=0):  #添加 边
        if tail not in self.vertices:
            self.add_vertex(tail)
        if head not in self.vertices:
            self.add_vertex(head)
        self.matrix[self.vertices.index(tail)][self.vertices.index(head)] = cost
        self.edges_dict[(tail, head)] = cost
        self.edges_array.append((tail, head, cost))
        self.num_edges = len(self.edges_dict)
    def getEdges(self, V):     # 返回边
        pass
    def getVerticesNumbers(self):   #返回节点数目
        if self.num_vertices == 0:
            self.num_vertices = len(self.matrix)
        return self.num_vertices
    def getAllVertices(self):    #返回 所有的 节点
        return self.vertices
    def getAllEdges(self):       #返回 所有的 边
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if 0 < self.matrix[i][j] < float('inf'):
                    self.edges_dict[self.vertices[i], self.vertices[j]] = self.matrix[i][j]
                    self.edges_array.append([self.vertices[i], self.vertices[j], self.matrix[i][j]])
        return self.edges_array
    def __repr__(self):
        return str(''.join(str(i) for i in self.matrix))
    def to_do_vertex(self, i):
        print('vertex: %s' % (self.vertices[i]))
    def to_do_edge(self, w, k):
        print('edge tail: %s, edge head: %s, weight: %s' % (self.vertices[w], self.vertices[k], str(self.matrix[w][k])))
def create_undirected_matrix(my_graph):
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    matrix = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
              [0, 0, 1, 0, 1, 0, 0, 0],  # b
              [0, 0, 0, 1, 0, 0, 0, 0],  # c
              [0, 0, 0, 0, 1, 0, 0, 0],  # d
              [0, 0, 0, 0, 0, 1, 0, 0],  # e
              [0, 0, 1, 0, 0, 0, 1, 1],  # f
              [0, 0, 0, 0, 0, 1, 0, 1],  # g
              [0, 0, 0, 0, 0, 1, 1, 0]]  # h

    my_graph = Graph_Matrix(nodes, matrix)
    print(my_graph)
    return my_graph
def draw_undircted_graph(my_graph):
    G = nx.Graph()  # 建立一个空的无向图G
    for node in my_graph.vertices:    #添加  节点
        G.add_node(str(node))
    for edge in my_graph.edges:       #添加  边
        G.add_edge(str(edge[0]), str(edge[1]))
    print("nodes:", G.nodes())  # 输出全部的节点
    print("edges:", G.edges())  # 输出全部的边
    print("number of edges:", G.number_of_edges())  # 输出边的数量
    nx.draw(G, with_labels=True)
    plt.savefig("undirected_graph.png")
    plt.show()
if __name__=='__main__':
    my_graph = Graph_Matrix()
    create_graph=create_undirected_matrix(my_graph)
    draw_undircted_graph(create_graph)



"""
[0, 1, 1, 1, 1, 1, 0, 0]
[0, 0, 1, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 0, 1, 1, 0]
nodes: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
edges: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'c'), ('b', 'e'), ('c', 'd'), ('c', 'f'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('f', 'h'), ('g', 'h')]
number of edges: 14

"""