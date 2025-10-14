# creating a Node

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append Node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    # Traversing The List (printing All Nodes)

    def traverse(self):
        if not self.head:
            print("singly Linked List is Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()

    # Inserting a Node at a Specific Position

    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count += 1
            new_node.next = curr
            if prev_node:
                prev_node.next = new_node

    # Deleting The head Node(first Node)

    def delete_head(self):
        if not self.head:
            print("Cannot delete. singly linked list already empty!")
        else:
            self.head = self.head.next

    # Deleting a Node by Value

    def delete(self, val):
        temp = self.head
        if temp and temp.val == val:
            self.head = temp.next
            return
        prev = None
        found = False
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next
        if found:
            prev.next = temp.next
        else:
            print("Node Not Found!")


sll = SinglyLinkedList()

# Append nodes
sll.append(100)
sll.append(200)
sll.append(50)
sll.append(20)
sll.traverse()

# Insert nodes
sll.insert_at(43, 0)      # Insert 43 at the beginning
sll.traverse()

sll.insert_at(400, 3)     # Insert 400 at position 3
sll.traverse()            # Output: 43 100 200 400 50 20

sll.delete_head()
sll.traverse()

sll.delete(2000)
sll.traverse()
