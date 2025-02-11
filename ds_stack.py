from data_structures import SinglyLinkedListNode

class Stack:
    def __init__(self, value):
        newNode = SinglyLinkedListNode(value)
        self.top = newNode

    def push(self, value):
        newNode = SinglyLinkedListNode(value)
        if self.top is None:
            self.top = newNode

        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            return None
        
        else:
            nodeToReturn = self.top
            self.top = self.top.next
            nodeToReturn.next = None
            return nodeToReturn