from data_structures import SinglyLinkedListNode

class Stack:
    def __init__(self, value):
        newNode = SinglyLinkedListNode(value)
        self.top = newNode

    def insert(self, value):
        newNode = SinglyLinkedListNode(value)
        if self.top is None:
            self.top = newNode

        else:
            newNode.next = self.top
            self.top = newNode