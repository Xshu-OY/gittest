# 先序遍历递归
def  PreOrder(self ,root):
    if root == None:
        return
    print (root.elem)
    self.PreOrder(root.lchild)   
    self.PreOrder(root.rchild)   


# 中序遍历代码
def  InOrder(self ,root):
    if root == None:
        return
    self.InOrder(root.lchild)  
    print (root.elem)
    self.InOrder(root.rchild)  



# 后序遍历代码
def  PostOrder(self ,root):
    if root == None:
        return
    self.PostOrder(root.lchild)  
    self.PostOrder(root.rchild)  
    print (root.elem)



# 层序遍历代码

def breath_travel(self):
    if root == None:
        return
    queue=[]
    queue.append(root)
    while queue:
        node =queue.pop(0)
        print (node.elem),
        if node.lchild != None:
            queue.append(node.lchild)
        if node.rchild != None:
            queue.append(node.rchild)


# 二叉树创建代码
def createBiTree(self, root):
    data = input()
    if data is "#":            #如果当前元素为'#', 则认为其为 None
        return None
    else:
        root.data = data
        root.lchild = self. createBiTree(root.lchild)         //构造左子树
        root.rchild = self. createBiTree(root.rchild)        //构造右子树
    return root
