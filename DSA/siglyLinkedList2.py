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
        if(self.isEmpty()):
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def isEmpty(self):
        if self.head == None:
            print("List is empty")
        return self.head == None

    def print(self):
        print("---------------List---------------")
        if(self.isEmpty()):
            return

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    # take user input dynamically
    def addData(self):
        isYes = 'y'
        while isYes[0].lower() == 'y':
            value = input("Enter value: ")
            self.appendAtBegning(value)

            isYes = input("Add new value? press [n/y]: ")

        self.print()


if __name__ == '__main__':
    ll = LinkedList()
    # ll.appendAtBegning(4)
    # ll.appendAtBegning(6)
    # ll.appendAtBegning(2)
    # ll.appendAtEnd(7)
    # ll.appendAtBegning(8)

    # ll.print()
    ll.addData()