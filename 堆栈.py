class Stack(object):
    def __init__(self):          #初始化
        self.items=[]
    def is_empty(self):       #判断栈是否为空
        return self.items==[]
    def push(self,item):             # 加入元素
        self.items.append(item)
    def pop(self):                #弹出元素
        return self.items.pop()
    def peek(self):             # 返回栈顶元素
        return self.items[len(self.items)-1]
    def size(self):                #返回栈的大小
        return len(self.items)
if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())
    stack.push(1)
    print(stack.peek())
    stack.push(2)
    print(stack.peek())
    stack.push(3)
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.peek())
    stack.pop()
    print(stack.is_empty())
    print(stack.size())




