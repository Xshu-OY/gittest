
# 哈夫曼树

# 树节点类构建
class TreeNode(object):
    def __init__(self, data):
        self.val = data[0]           #节点的值
        self.priority = data[1]       #节点的优先度
        self.leftChild = None       #节点的左子结点
        self.rightChild = None     #节点的右子结点
        self.code = ""            #节点值的编码
# 创建树节点队列函数
def creatnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q
# 为队列添加节点元素，并保证优先度从大到小排列
def addQ(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]
# 节点队列类定义
class nodeQeuen(object):
    def __init__(self, code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)
    def addNode(self,node):           #添加节点函数
        self.que = addQ(self.que, node)
        self.size += 1
    def popNode(self):        #弹出节点函数
        self.size -= 1
        return self.que.pop(0)
# 各个字符在字符串中出现的次数，即计算优先度
def freChar(string):
    d ={}
#定义字典，遍历文本中的每一个字母，若字母不在字典里，说明是第一次出现，定义该字母为键，键值为1；若已有，将其相应的键值加一。遍历后就会得到每个字母出现的次数。
    for c in string:
        if not c in d:
            d[c] = 1
        else:
            d[c] += 1
    return sorted(d.items(),key=lambda x:x[1])
# 创建哈夫曼树
def creatHuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()

codeDic1 = {}        #用于编码
codeDic2 = {}         #用于解码
# 由哈夫曼树得到哈夫曼编码表
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x+'0')
# 二叉树的中序遍历，每递归到深一层的时候，就在后面多加一个‘0’（左子树）或‘1’（右子树）。
        head.code += x
        if head.val:
            codeDic2[head.code] = head.val
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x+'1')
# 字符串编码
def TransEncode(string):
    global codeDic1
    transcode = ""
    for c in string:
        transcode += codeDic1[c]
    return transcode
# 字符串解码
def TransDecode(StringCode):
    global codeDic2
    code = ""
    ans = ""
    for ch in StringCode:
        code += ch
        if code in codeDic2:
            ans += codeDic2[code]
            code = ""
    return ans
# 举例
string = "AAGGDCCCDDDGFBBBFFGGDDDDGGGEFFDDCCCCDDFGAAA"
t = nodeQeuen(freChar(string))
tree = creatHuffmanTree(t)
HuffmanCodeDic(tree, '')
print(codeDic1,codeDic2)
a = TransEncode(string)
print(a)
aa = TransDecode(a)
print(aa)
print(string == aa)



