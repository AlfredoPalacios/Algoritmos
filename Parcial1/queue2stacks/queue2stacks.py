class Queue(object):
    def __init__(self):
        self.stackin=[]
        self.stackout=[]
    def enqueue(self,y):
        self.stackin.append(y)
    def dequeue(self):
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()

fila=Queue()
a="holacomoestas"
for i in a:
    fila.enqueue(i)
for i in a:
    print(fila.dequeue())