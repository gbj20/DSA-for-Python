class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
# Insert at head

    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
# Insert at End(append)

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
# Insert a specific position

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

# Traversal Operations
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def traverse_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.val, end=" ")
            current = current.prev
        print()


dll = DoublyLinkedList()
dll.insert_at_head(100)
dll.traverse_forward()

dll.insert_at_head(200)
dll.traverse_forward()

dll.append(500)
dll.traverse_forward()

dll.insert_at(300, 3)
dll.traverse_forward()
 