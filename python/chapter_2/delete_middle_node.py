"""
DELETE MIDDLE NODE
- Implement and algorithm to delete a node in the middle (ie. any node except first and last node,
  not necessarily the exact middle) of a singly linked list, given only access to that node.

- EXAMPLE:
    - input: node "c" from a -> b -> c -> d -> e -> f
    - output: nothing returned but list changes to a -> b -> d -> e -> f

Clarifying Questions:
    1. Are all vales unique (no duplicates)?
    2. Assume input node will not be first or last
"""


# This is an input class. Do not edit.
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # Need this function to obtain Node value when printing
    # For singly linked list only
    def __str__(self):
        return f'{self.value}'


# Feel free to add new properties and methods to the class.
class SinglyLinkedList:
    def __init__(self):
        self.head = None

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

    def remove(self, node):
        # If node is head, then make the next node the new head
        if node == self.head:
            self.head == self.head.next
        # If node is tail, then make the prev node the new tail
        if node == self.tail:
            self.tail == self.tail.prev
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        # Change node's next and prev node's pointer
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def delete_middle_node(self, node):
        curr = self.head
        if curr is None:
            return

        # Iterate through until reach last node
        while curr.next is not None:
            # Delete middle node if value equal to input node value
            if curr.next.value == node.value:
                curr.next = curr.next.next
                return
            curr = curr.next


# __name__ , __init__, __str__, ... are class methods
# Below is asking if we are on main function
if __name__ == '__main__':
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")
    n5 = Node("e")
    n6 = Node("f")

    # Initialize doubly linked list
    ll = SinglyLinkedList()
    ll.setHead(n1)
    ll.insertAfter(n1, n2)
    ll.insertAfter(n2, n3)
    ll.insertAfter(n3, n4)
    ll.insertAfter(n4, n5)
    ll.insertAfter(n5, n6)

# Test Cases
print('Linked List before delete middle node: ', ll)
ll.delete_middle_node(n3)
print('Linked List after delete middle node: ', ll)
