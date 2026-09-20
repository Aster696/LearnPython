class Node:
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def appendAtBegning(self, data):
        node = Node(data, self.head)
        self.head = node

    def appendAtEnd(self, data):
        node = Node(data, self.head)
        self.next = node

    def print(self):

        if self.head is None:
            print('List is empty')
            return;

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.appendAtBegning(4)
    ll.appendAtBegning(6)
    ll.appendAtBegning(2)
    ll.appendAtEnd(7)

    ll.print()