class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class linkedlist:
    head=None
    def __init__(self,data):
        self.head=Node(data)
    def add_end(self,data):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(data)
        return temp
    def add_first(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        return temp
    def  delete_first(self):
        temp=self.head
        self.head=self.head.next
        return temp
    def delete_last(self):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=temp
        return temp

        