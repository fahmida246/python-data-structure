class Node:
    def __init__(self,data):
        self.data = data
        self.next = 0

class queue:
    def __init__(self):
        self.top =0
    def enqueue(self,data):
        newnode = Node(data)
        temp = self.top
        newnode.next = temp
        self.top = newnode
    def deque(self):
        i = 0
        temp = self.top
        while(temp.next!=0):
            prev = temp
            temp = temp.next
            i = i+1
        prev.next=0

    def display(self):
        temp=self.top
        while(temp!=0):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    llist= queue()
    llist.enqueue(1)
    llist.enqueue(4)
    llist.enqueue(5)
    llist.deque()
    llist.display()



