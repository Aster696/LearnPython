class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def displayNode(self):
        temp = self.head
        while temp:
            print(temp.data, end=" > ")
            temp = temp.next
        print("None")

li = singlyLinkedList()
li.append(10)
li.append(20)
li.append(30)
li.append(40)
li.displayNode()