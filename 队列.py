class Queue(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):                #判断队列是否为空
        return self.items==[]
    def enqueue(self,item):             #入队列
        self.items.insert(0,item)
    def dequeue(self):                 #出队列
        return self.items.pop()
    def size(self):                     #队列元素个数
        return len(self.items)
if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())
    print(queue.size())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.is_empty())
print(queue.size())


