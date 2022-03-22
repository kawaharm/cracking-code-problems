# RETURN KTH TO LAST ELEMENT
# Implement an algorithm to find the kth to last element of a singly linked list


"""
Clarifying Questions
- is the length of the list known?

"""
# Clarifying question


# This is an input class. Do not edit.
from ast import Return
import unittest


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

    def return_kth_to_last(self, k):
        """
        # Return if empty list
        curr = self.head
        if curr is None:
            return

        # Find length of list
        length = 0
        while curr:
            length += 1
            curr = curr.next

        i = 1
        while i < k:
            curr = curr.prev
            i += 1

        return curr
        """
        # Set up two pointers
        p1 = self.head
        p2 = self.head

        # Move p1 k nodes down
        for i in range(k):
            if p1 is None:
                return
            p1 = p1.next

        # Move p1 and p2 at same pace. When p1 hits end of list,
        # p2 will be at kth element
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value


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
    ll.insertAfter(n6, n7)
    print('Linked List: ', ll)

 # // Test Cases
print(n6)
print(n4)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (3, 4),
        (4, 3)
    ]

    def test_return_kth(self):
        for [test_int, expected] in self.data:
            actual = ll.return_kth_to_last(test_int)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
