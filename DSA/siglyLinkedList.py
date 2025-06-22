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

    def update(self, old_value, data):
        temp = self.head
        while temp:
            if(old_value == temp.data):
                temp.data = data
                print('Data updated succuffully')
                break
            temp = temp.next

    def search(self, data):
        temp = self.head
        index = 0
        while temp:
            if temp.data == data:
                print("Found value: ", data, " at position: ", index)
                return True
            temp = temp.next
            index += 1
            
        print("Value not found")
        return False


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

li.update(30, 88)
li.displayNode()

li.search(88)
