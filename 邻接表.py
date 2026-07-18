

# 邻接表

class Vertex:    #顶点类
    def __init__(self,name):
        self.name = name
        self.next = []
class Graph:
    def __init__(self):
        self.vertexList = {}
def addVertex(self,vertex):          #图中添加一个顶点vertex
        if vertex in self.vertexList:
            return
        self.vertexList[vertex] = Vertex(vertex)
def addEdge(self,fromVertex,toVertex):   #添加从顶点fromVertex和顶点toVertex的边
        if fromVertex == toVertex:
            return
        if fromVertex not in self.vertexList:
            print("vertexList has no ",fromVertex)
            return
        if toVertex not in self.vertexList:
            print("vertexList has no ", toVertex)
            return
        if(toVertex not in self.vertexList[fromVertex].next):
            self.vertexList[fromVertex].next.append(toVertex)
        if(fromVertex not in self.vertexList[toVertex].next):
            self.vertexList[toVertex].next.append(fromVertex)
def removeVertex(self,vertex):                   #图中删除一个顶点vertex
        if vertex in self.vertexList:
            removed = self.vertexList.pop(vertex)
            removed = removed.name
            for key, vertex in self.vertexList.items():
                if removed in vertex.next:
                    vertex.next.remove(removed)
def removeEdge(self,fromVertex,toVertex):    #删除从fromVertex到toVertex的边          
        if fromVertex not in self.vertexList:
            if fromVertex not in self.vertexList:
                print("vertexList has no ", fromVertex)
                return
            if toVertex not in self.vertexList:
                print("vertexList has no ", toVertex)
                return
        if fromVertex in self.vertexList[toVertex].next:
            self.vertexList[fromVertex].next.remove(toVertex)
            self.vertexList[toVertex].next.remove(fromVertex)
if __name__ == "__main__":
    G = Graph()
    for i in range(1,8):
            G.addVertex(i)
    for i in range(1,7):
            G.addEdge(i,i+1)
    for i,g in G.vertexList.items():
            print(i,g.next)
    print("删除节点2")
    G.removeVertex(2)
    for i,g in G.vertexList.items():
            print(i,g.next)
    print("删除节点4与节点3之间的边")
    G.removeEdge(4,3)
    for i,g in G.vertexList.items():
            print(i,g.next)



"""
1 [2]
2 [1, 3]
3 [2, 4]
4 [3, 5]
5 [4, 6]
6 [5, 7]
7 [6]
删除节点2
1 []
3 [4]
4 [3, 5]
5 [4, 6]
6 [5, 7]
7 [6]
删除节点4与节点3之间的边
1 []
3 []
4 [5]
5 [4, 6]
6 [5, 7]
7 [6] 

"""

