class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.item[len(self.item)-1]

    def size(self):
        return len(self.items)
s1=Stack()
s2=Stack()

x=int(input("Enter The Decimal Number: "))
while x!=0:
    y=x%2
    x=x//2
    s1.push(y)

l=[0]
print(s1.size())

while not s1.isEmpty():
    l.append(s1.pop())

print(l)










