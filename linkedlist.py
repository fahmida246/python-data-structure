class Node:
    def __init__(self,data):
        self.data = data
        self.next = 0
    
class linkedlist:
    def __init__(self):
        self.head=0
    def insertatbeg(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insertatlast(self,data):
        newnode = Node(data)
        temp = self.head
        while(temp.next!=0):
            temp = temp.next
        temp.next = newnode
    
    def insertatpos(self,pos,data):
        newnode = Node(data)
        temp = self.head
        i= 0
        while(i<pos-1):
            temp = temp.next
            i=i+1
        newnode.next = temp.next
        temp.next = newnode
    def deleteatfirst(self):
        temp= self.head
        self.head = temp.next
    
    def deletelast(self):
        temp = self.head 
        while(temp.next!=0):
            prev = temp
            temp = temp.next
        prev.next = 0

    def deletepos(self,pos):
        temp = self.head
        i =0
        while(i<pos-1):
            temp=temp.next
            i=i+1
        prevnode = temp.next
        temp.next = prevnode.next
        del prevnode
    
    def display(self):
        temp=self.head
        while(temp!=0):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    llist= linkedlist()
    llist.insertatbeg(1)
    llist.insertatbeg(4)
    llist.insertatbeg(4)
    llist.insertatpos(3,50)
    llist.insertatlast(8)
    llist.insertatlast(9)
    llist.display()
    llist.deleteatfirst()
    print('after delete')
    llist.display()
    print('after delete')
    llist.deletelast()
    llist.display()
    print('after delete')
    llist.deletepos(2)
    llist.display()