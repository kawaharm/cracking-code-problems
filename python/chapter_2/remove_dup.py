# REMOVE DUPLICATES
# remove duplicates of an unsorted linked list


# This is an input class. Do not edit.
from ast import Return


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    # Need this function to obtain Node value when printing
    # For singly linked list only
    def __str__(self):
        return f'{self.value}'


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        # defining a blank res variable
        result = ""

        # initializing ptr to head
        ptr = self.head

        # traversing and adding it to result
        while ptr:
            result += str(ptr.value) + " -> "
            ptr = ptr.next

        # removing trailing commas
        result = result.strip(" -> ")

        # chen checking if
        # anything is present in res or not
        if len(result):
            return "[" + result + "]"
        else:
            return "[]"

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # We do not need to insert node if already in head and tail
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # in case this node is in another linked list
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # if node is head of Linked List...
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # in case this node is in another linked list
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        # if node is tail of Linked List...
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # If node is head, then make the next node the new head
        if node == self.head:
            self.head == self.head.next
        # If node is tail, then make the prev node the new tail
        if node == self.tail:
            self.tail == self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        # return True if value found
        # return False if node = None or value not found
        return node is not None

    def removeNodeBindings(self, node):
        # Change node's next and prev node's pointer
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def remove_dups(self):
        # Define current node
        current = self.head
        # Use hash table
        dup_dict = {}

        # Return if empty head
        if current is None:
            return

        while current:
            # Remove node if already in hash table
            if current.value in dup_dict:
                self.remove(current)
            # Add value if not in hash table
            else:
                dup_dict[current.value] = 1
            # Move to next node
            current = current.next


# __name__ , __init__, __str__, ... are class methods
# Below is asking if we are on main function
if __name__ == '__main__':
    n1 = Node(2)
    n2 = Node(7)
    n3 = Node(7)
    n4 = Node(3)
    n5 = Node(4)
    n6 = Node(2)
    n7 = Node(3)

    # Initialize doubly linked list
    ll = DoublyLinkedList()
    ll.setHead(n1)
    ll.insertAfter(n1, n2)
    ll.insertAfter(n2, n3)
    ll.insertAfter(n3, n4)
    ll.insertAfter(n4, n5)
    ll.insertAfter(n5, n6)
    print('Linked List: ', ll)

    # Test remove_dups
    ll.remove_dups()
    print('Linked List after remove duplicates: ', ll)
